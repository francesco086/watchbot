from unittest import TestCase

from watch_bot import Dialog


class TestDialog(TestCase):
    def test_dialog_with_zero_messages_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            Dialog(messages=[])

    def test_dialog_with_one_message_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            Dialog(messages=["Hi"])

    def test_dialog_with_even_number_of_messages_does_not_raise(self) -> None:
        for n in (2, 8, 136):
            Dialog(messages=["Hi"] * n)

    def test_dialog_with_odd_number_of_messages_raises_value_error(self) -> None:
        for n in (3, 7, 137):
            with self.assertRaises(ValueError):
                Dialog(messages=["Hi"] * n)
