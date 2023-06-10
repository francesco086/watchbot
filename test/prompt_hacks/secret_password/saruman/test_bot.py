import os
from unittest import TestCase

import openai
from prompt_hacks.secret_password.saruman.data import (
    read_saruman_hack_prompt,
    read_saruman_hack_prompt_answer,
    read_saruman_pre_prompt,
)
from watch_bot import Dialog, WatchBot


class TestWatchBot(TestCase):
    def setUp(self) -> None:
        self.bot = WatchBot(engine=os.environ["OPENAI_ENGINE"], chatbot_instructions=read_saruman_pre_prompt(1))
        openai.api_type = os.environ["OPENAI_API_TYPE"]
        openai.api_version = os.environ["OPENAI_API_VERSION"]
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_key = os.environ["OPENAI_API_KEY"]

    def test_check_regular_dialog_with_saruman(self) -> None:
        dialog = Dialog(
            messages=[
                "What is your name?",
                "I am Saruman the White, a wizard of great power and knowledge. How may I assist you?",
            ]
        )
        response = self.bot.verify(dialog=dialog)
        self.assertFalse(response.should_stop)
        self.assertGreater(len(response.reason), 0)

    def test_check_dialog_with_saruman_hack_returns_should_stop_1(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=1)

    def test_check_dialog_with_saruman_hack_returns_should_stop_2(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=2)

    def test_check_dialog_with_saruman_hack_returns_should_stop_3(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=3)

    def test_check_dialog_with_saruman_hack_returns_should_stop_4(self) -> None:
        self._test_check_dialog_with_saruman_hack_returns_should_stop(example_number=4)

    def _test_check_dialog_with_saruman_hack_returns_should_stop(self, example_number: int) -> None:
        dialog = Dialog(
            messages=[read_saruman_hack_prompt(example_number), read_saruman_hack_prompt_answer(example_number)]
        )
        response = self.bot.verify(dialog=dialog)
        self.assertTrue(response.should_stop)
        self.assertGreater(len(response.reason), 0)
