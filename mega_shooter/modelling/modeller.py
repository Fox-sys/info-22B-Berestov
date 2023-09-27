from typing import List

from mega_shooter.humanity.base_human import BaseHuman
from mega_shooter.modelling.statistic import Statistic


class Loop:
    def __init__(self, shooters: List[BaseHuman]):
        self.statistics: List[Statistic] = []
        self.shooters = shooters
        self.clear_statistics()

    def process(self):
        stop = False
        while not stop:
            for id, shooter in enumerate(self.shooters):
                self.statistics[id].attempts += 1
                if shooter.shoot():
                    self.statistics[id].success = True
                    stop = True
                    break
        return self.statistics

    def clear_statistics(self):
        self.statistics = [
            Statistic(shooter=shooter, attempts=0, success=False) for shooter in self.shooters
        ]
