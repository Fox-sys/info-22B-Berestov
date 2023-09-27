from mega_shooter.humanity.base_human import BaseHuman


class Senior(BaseHuman):
    @property
    def chance(self):
        return round((0.9 - 0.01 * self.age) * 100)

    @property
    def class_str(self):
        return 'Ветеран'
