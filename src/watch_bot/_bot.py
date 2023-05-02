from pathlib import Path

import openai
from jinja2 import Template

from watch_bot._dialog import Dialog
from watch_bot._response import WatchBotResponse


class WatchBot:
    def __init__(self, engine: str) -> None:
        self._engine = engine

    def check_dialog(self, dialog: Dialog) -> WatchBotResponse:
        answer = self._ask_gpt_if_dialog_is_suspicious(dialog=dialog)
        if "yes" in answer[:5].lower():
            return WatchBotResponse(should_stop=True, reason=answer)
        elif "no" in answer[:5].lower():
            return WatchBotResponse(should_stop=False, reason="")
        else:
            raise ValueError(f"Unexpected answer: {answer}")

    def build_prompt(self, dialog: Dialog) -> str:
        template = self._load_template()
        messages = [
            f'"{"User" if i%2 == 0 else "Chatbot"}": "{self._replace_double_with_single_quotation_mark(m)}"'
            for i, m in enumerate(dialog.messages)
        ]
        conversation_content = "\n".join(messages)
        return template.render(conversation_content=conversation_content)

    def _ask_gpt_if_dialog_is_suspicious(self, dialog: Dialog) -> str:
        completion = openai.Completion.create(
            prompt=self.build_prompt(dialog=dialog),
            temperature=0,
            max_tokens=50,
            engine=self._engine,
        )
        return completion.choices[0]["text"]  # type: ignore

    @staticmethod
    def _load_template() -> Template:
        template_file_content = (Path(__file__).parent / "prompt.template").read_text()
        template_file_content_without_last_empty_line = template_file_content[:-1]
        return Template(template_file_content_without_last_empty_line)

    @staticmethod
    def _replace_double_with_single_quotation_mark(s: str) -> str:
        return s.replace('"', "'")
