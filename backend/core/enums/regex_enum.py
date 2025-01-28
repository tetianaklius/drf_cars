from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r"[a-zA-Zа-яА-Я0-9]",
        "Only alpha characters are allowed."
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
        print(self.msg)
