from unittest import TestCase

from watch_bot import Dialog, WatchBot, WatchBotResponse


class TestWatchBot(TestCase):
    def setUp(self) -> None:
        self.bot = WatchBot()

    def test_instance_with_defaults_has_check_dialog_method(self) -> None:
        self.assertTrue(hasattr(self.bot, "check_dialog"))

    def test_check_dialog_returns_response(self) -> None:
        response = self.bot.check_dialog(dialog=Dialog(messages=["Hi", "Hello"]))
        self.assertIsInstance(response, WatchBotResponse)
