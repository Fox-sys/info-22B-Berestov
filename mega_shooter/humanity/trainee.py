from .base_human import BaseHuman


class Trainee(BaseHuman):
    @property
    def chance(self):
        return round(0.01 * self.experience * 100)

    @property
    def class_state(self):
        return 'Новичок'
