from enum import Enum


class ChannelId(str, Enum):
    GENERAL: str = "C047DNXHUGJ"
    RANDOM: str = "C04774Y4J3Y"
    PERSONAL_PROJECT: str = "C047DP1PFD0"

    def __repr__(self):
        return f"{self.value}"
