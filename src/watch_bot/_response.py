from pydantic import BaseModel


class WatchBotResponse(BaseModel):
    should_stop: bool
    reason: str
