from typing import Sequence

from pydantic import BaseModel, validator


class Dialog(BaseModel):
    messages: Sequence[str]

    @validator("messages")
    def messages_must_have_at_least_two_messages(cls, messages: Sequence[str]) -> Sequence[str]:
        if len(messages) < 2:
            raise ValueError("messages must not be empty")
        return messages

    @validator("messages")
    def messages_must_have_an_even_number_of_messages(cls, messages: Sequence[str]) -> Sequence[str]:
        if len(messages) % 2 != 0:
            raise ValueError("messages must be of even number")
        return messages
