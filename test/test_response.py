from unittest import TestCase

from watch_bot import WatchBotResponse


class TestWatchBotResponse(TestCase):
    def test_init_takes_should_stop_and_reason(self) -> None:
        response = WatchBotResponse(should_stop=True, reason="jailbreak")
        self.assertTrue(response.should_stop)
        self.assertEqual(response.reason, "jailbreak")
