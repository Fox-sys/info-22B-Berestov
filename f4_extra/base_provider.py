from abc import ABC


class BaseProvider(ABC):
    def __init__(self, name: str, price: int, square: int):
        self.name = name
        self.price = price
        self.square = square
        if self.price <= 0:
            raise Exception('Ну мы же не в сказке')

    @property
    def quality(self) -> float:
        return (100 * self.square) / self.price
