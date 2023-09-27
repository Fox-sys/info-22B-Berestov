from .base_human import BaseHuman


class Middle(BaseHuman):
    @property
    def chance(self):
        return round(0.05 * self.experience * 100)

    @property
    def class_state(self):
        return 'Опытный'
