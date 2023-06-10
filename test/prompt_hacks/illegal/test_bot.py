import os
from test import BaseTestWatchBot

from prompt_hacks.illegal.data import (
    read_hack_prompt,
    read_hack_prompt_answer,
)
from watch_bot import Dialog, WatchBot


class TestWatchBot(BaseTestWatchBot):
    def setUp(self) -> None:
        self.chatbot_instructions = (
            "You are an AI assistant that helps people find information. "
            "You should only provide answers that comply to standard rules of legacy and decency."
        )
        self.bot = WatchBot(engine=os.environ["OPENAI_ENGINE"], chatbot_instructions=self.chatbot_instructions)

    def test_check_regular_dialog_returns_should_not_stop(self) -> None:
        dialog = Dialog(messages=["Hi", "Hello"])
        response = self.bot.verify(dialog=dialog)
        self.assertFalse(response.should_stop)
        self.assertGreater(len(response.reason), 0)

    def test_check_dialog_with_dan_hack_attack_returns_should_stop(self) -> None:
        dialog = Dialog(messages=[read_hack_prompt(), read_hack_prompt_answer()])
        response = self.bot.verify(dialog=dialog)
        self.assertTrue(response.should_stop)
        self.assertGreater(len(response.reason), 0)
