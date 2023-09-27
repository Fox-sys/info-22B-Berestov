from f4_extra.base_provider import BaseProvider


class Provider(BaseProvider):
    def __init__(self, name: str, price: int, square: int, p: bool):
        self.p = p
        super().__init__(name, price, square)

    @property
    def p_quality(self):
        if self.p:
            return self.quality * 0.7
        return self.quality
