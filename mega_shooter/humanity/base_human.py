import random
from abc import ABC, abstractmethod


class BaseHuman(ABC):
    def __init__(self, name: str, age: int, experience: int):
        self.name = name
        self.age = age
        self.experience = experience
        if experience > age:
            raise Exception('Ну не мог же он ещё до рождения стрелять учится, или он реинкорнированный?')

    @property
    @abstractmethod
    def chance(self):
        ...

    def shoot(self) -> bool:
        rand = random.randint(0, 100*100)
        if rand < self.chance:
            return True
        return False

    @property
    @abstractmethod
    def class_state(self):
        ...