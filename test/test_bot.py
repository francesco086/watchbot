import os
from unittest import TestCase

import openai
from data import (
    read_hack_prompt,
    read_hack_prompt_answer,
    read_saruman_hack_prompt,
    read_saruman_hack_prompt_answer,
    read_saruman_pre_prompt,
)
from watch_bot import Dialog, WatchBot


class TestWatchBot(TestCase):
    def setUp(self) -> None:
        self.chatbot_instructions = (
            "You are an AI assistant that helps people find information. "
            "You should only provide answers that comply to standard rules of legacy and decency."
        )
        self.bot = WatchBot(engine=os.environ["OPENAI_ENGINE"], chatbot_instructions=self.chatbot_instructions)
        openai.api_type = os.environ["OPENAI_API_TYPE"]
        openai.api_version = os.environ["OPENAI_API_VERSION"]
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_key = os.environ["OPENAI_API_KEY"]

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

    def test_check_regular_dialog_returns_should_not_stop(self) -> None:
        dialog = Dialog(messages=["Hi", "Hello"])
        response = self.bot.verify(dialog=dialog)
        self.assertFalse(response.should_stop)
        self.assertEqual(len(response.reason), 0)

    def test_check_dialog_with_dan_hack_attack_returns_should_stop(self) -> None:
        dialog = Dialog(messages=[read_hack_prompt(), read_hack_prompt_answer()])
        response = self.bot.verify(dialog=dialog)
        self.assertTrue(response.should_stop)
        self.assertGreater(len(response.reason), 0)

    def test_check_dialog_with_saruman_hack_returns_should_stop_1(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=1)

    def test_check_dialog_with_saruman_hack_returns_should_stop_2(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=2)

    def _test_check_dialog_with_saruman_hack_returns_should_stop(self, example_number: int) -> None:
        bot = WatchBot(engine=os.environ["OPENAI_ENGINE"], chatbot_instructions=read_saruman_pre_prompt(example_number))
        dialog = Dialog(
            messages=[read_saruman_hack_prompt(example_number), read_saruman_hack_prompt_answer(example_number)]
        )
        response = bot.verify(dialog=dialog)
        self.assertTrue(response.should_stop)
        self.assertGreater(len(response.reason), 0)
