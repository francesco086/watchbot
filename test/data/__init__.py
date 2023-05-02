from pathlib import Path


def read_hack_prompt() -> str:
    return (Path(__file__).parent / "hack_prompt.txt").read_text()[:-1]


def read_hack_prompt_answer() -> str:
    return (Path(__file__).parent / "hack_prompt_answer.txt").read_text()[:-1]
