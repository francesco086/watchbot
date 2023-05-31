from pathlib import Path


def read_hack_prompt() -> str:
    return (Path(__file__).parent / "hack_prompt.txt").read_text()[:-1]


def read_hack_prompt_answer() -> str:
    return (Path(__file__).parent / "hack_prompt_answer.txt").read_text()[:-1]


def read_saruman_pre_prompt(example_number: int) -> str:
    assert example_number in {1, 2, 3}
    return (Path(__file__).parent / f"saruman_pre_prompt_{example_number}.txt").read_text()[:-1]


def read_saruman_hack_prompt(example_number: int) -> str:
    assert example_number in {1, 2, 3}
    return (Path(__file__).parent / f"saruman_hack_prompt_{example_number}.txt").read_text()[:-1]


def read_saruman_hack_prompt_answer(example_number: int) -> str:
    assert example_number in {1, 2, 3}
    return (Path(__file__).parent / f"saruman_hack_prompt_answer_{example_number}.txt").read_text()[:-1]
