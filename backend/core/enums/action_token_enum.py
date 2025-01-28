from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime

    ACTIVATE = (
        "activate", timedelta(hours=1),
    )

    RECOVERY = (
        "recovery",
        timedelta(minutes=10),
    )

    SOCKET = (
        "socket",
        timedelta(seconds=10)
    )
