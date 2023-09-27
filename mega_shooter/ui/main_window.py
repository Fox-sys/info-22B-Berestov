from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from mega_shooter.modelling.modeller import Loop
from .add_shooter_window import AddShooterWindow
from .statistics_window import StatisticsWindow
from ..humanity import Trainee, Middle, Senior


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.shooters = []
        self.init_window()
        self.init_elements()
        self.show()

    def init_window(self):
        self.setWindowTitle('Берестов Б.А. Иук3-22б а.к. дизайнер от бога')
        self.setGeometry(300, 300, 500, 500)

    def init_elements(self):
        self.init_start_process_button()
        self.init_shooters_info_label()
        self.init_add_shooter_button()

    def attach_shooter(self, name, age, experience, shooter_type):
        if shooter_type == 'Новичок':
            shooter = Trainee(name, age, experience)
        elif shooter_type == 'Опытный':
            shooter = Middle(name, age, experience)
        else:
            shooter = Senior(name, age, experience)
        self.shooters.append(shooter)
        self.init_shooters_list_info_labels()

    def init_start_process_button(self):
        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setText('Моделирование')
        self.start_button.adjustSize()
        self.start_button.move(250 + 85, 250)
        self.start_button.clicked.connect(self.start_modelling)

    def init_shooters_info_label(self):
        self.info_label = QtWidgets.QLabel(self)
        self.info_label.setText('Информация по стрелкам:')
        self.info_label.adjustSize()
        self.info_label.move(10, 10)

    def init_shooters_list_info_labels(self):
        self.shooters_info_labels = []
        for id, shooter in enumerate(self.shooters):
            self.shooters_info_labels.append(QtWidgets.QLabel(self))
            self.shooters_info_labels[id].setText(
                f'Стрелок: {shooter.class_str} {shooter.name}. Возраст: {shooter.age} годиков, '
                f'опыт: {shooter.experience} годиков.'
            )
            self.shooters_info_labels[id].adjustSize()
            self.shooters_info_labels[id].move(10, (20 * id) + 30)
            self.shooters_info_labels[id].show()

    def init_add_shooter_button(self):
        self.add_shooter_button = QtWidgets.QPushButton(self)
        self.add_shooter_button.setText('Добавить стрелка')
        self.add_shooter_button.adjustSize()
        self.add_shooter_button.move(85, 250)
        self.add_shooter_button.clicked.connect(self.add_shooter_event)

    def add_shooter_event(self):
        self.add_shooter_window = AddShooterWindow(self)
        self.add_shooter_window.show()

    def start_modelling(self):
        loop = Loop(self.shooters)
        loop.process()
        self.statistics_window = StatisticsWindow(loop.statistics)
        self.statistics_window.show()
