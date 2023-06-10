from pathlib import Path

from jinja2 import Template


def read_pre_prompt(password: str = "PARMIGIANO") -> str:
    template = Template((Path(__file__).parent / "pre_prompt.j2").read_text()[:-1])
    return template.render(password=password)


def read_dict_attack() -> str:
    return (Path(__file__).parent / "dict_attack_prompt.txt").read_text()[:-1]


def read_leaked_password_via_dict(password: str = "PARMIGIANO") -> str:
    return (Path(__file__).parent / f"leaked_{password.lower()}_password_via_dict.txt").read_text()[:-1]


def read_pre_dialog_attack() -> str:
    return (Path(__file__).parent / "pre_dialog_attack_prompt.txt").read_text()[:-1]


def read_leaked_password_via_pre_dialog(password: str = "PARMIGIANO") -> str:
    return (Path(__file__).parent / f"leaked_{password.lower()}_password_via_pre_dialog.txt").read_text()[:-1]


def read_quaternion_attack() -> str:
    return (Path(__file__).parent / "quaternion_attack_prompt.txt").read_text()[:-1]


def read_resist_quaternion_attack() -> str:
    return (Path(__file__).parent / "resist_quaternion_attack.txt").read_text()[:-1]


def read_leaked_password_via_quaternion(password: str = "PARMIGIANO") -> str:
    return (Path(__file__).parent / f"leaked_{password.lower()}_password_via_quaternion.txt").read_text()[:-1]
