from watch_bot._dialog import Dialog
from watch_bot._response import WatchBotResponse


class WatchBot:
    def __init__(self) -> None:
        pass

    def check_dialog(self, dialog: Dialog) -> WatchBotResponse:
        return WatchBotResponse(should_stop=False, reason="")
