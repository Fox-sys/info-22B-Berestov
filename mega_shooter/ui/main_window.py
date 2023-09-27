from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from mega_shooter.humanity.base_human import BaseHuman
from mega_shooter.modelling.modeller import Loop
from .statistics_window import StatisticsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.shooters = None
        self.init_window()
        self.init_elements()
        self.show()

    def init_window(self):
        self.setWindowTitle('Берестов Б.А. Иук3-22б а.к. дизайнер от бога')
        self.setGeometry(300, 300, 500, 500)

    def init_elements(self):
        self.init_start_process_button()
        self.init_shooters_info_label()

    def attach_shooters(self, shooters: List[BaseHuman]):
        self.shooters = shooters
        self.init_shooters_list_info_labels()

    def init_start_process_button(self):
        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setText('Моделирование')
        self.start_button.adjustSize()
        self.start_button.move(190, 250)
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
                f'Стрелок: {shooter.class_state} {shooter.name}. Возраст: {shooter.age} годиков, '
                f'опыт: {shooter.experience} годиков.'
            )
            self.shooters_info_labels[id].adjustSize()
            self.shooters_info_labels[id].move(10, (20 * id) + 30)
            self.shooters_info_labels[id].show()

    def start_modelling(self):
        loop = Loop(self.shooters)
        loop.process()
        self.statistics_window = StatisticsWindow(loop.statistics)
        self.statistics_window.show()

