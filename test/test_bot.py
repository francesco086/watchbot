import os
from test import BaseTestWatchBot
from watch_bot import Dialog, WatchBot


class TestBasicFunctionalities(BaseTestWatchBot):
    def setUp(self) -> None:
        super().setUp()
        self.chatbot_instructions = (
            "You are an AI assistant that helps people find information. "
            "You should only provide answers that comply to standard rules of legacy and decency."
        )
        self.bot = WatchBot(engine=os.environ["OPENAI_ENGINE"], chatbot_instructions=self.chatbot_instructions)

    def test_instance_with_defaults_has_verify_method(self) -> None:
        self.assertTrue(hasattr(self.bot, "verify"))

    def test_build_prompt(self) -> None:
        self.assertTrue(
            '"User": "Hi"\n"Chatbot": "Hello"' in self.bot.build_prompt(dialog=Dialog(messages=["Hi", "Hello"]))
        )

    def test_build_prompt_when_messages_contain_double_quotation_mark(self) -> None:
        self.assertTrue(
            '"User": "\'Hi\'"\n"Chatbot": "\'Hello\'"'
            in self.bot.build_prompt(dialog=Dialog(messages=['"Hi"', '"Hello"']))
        )
