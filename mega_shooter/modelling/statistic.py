from dataclasses import dataclass

from mega_shooter.humanity.base_human import BaseHuman


@dataclass
class Statistic:
    shooter: BaseHuman
    attempts: int
    success: bool
