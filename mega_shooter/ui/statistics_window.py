from typing import List

from PyQt5 import QtWidgets

from mega_shooter.modelling.statistic import Statistic


class StatisticsWindow(QtWidgets.QWidget):
    def __init__(self, statistics):
        super().__init__()
        self.statistics: List[Statistic] = statistics
        self.init_window()
        self.init_layout()
        self.init_close_button()
        self.show_info()

    def init_layout(self):
        self.info_label = QtWidgets.QLabel(self)
        self.info_label.setText('Окно статистики')
        self.info_label.move(10, 10)

    def init_window(self):
        self.setWindowTitle('Окно статистики')
        self.setGeometry(500, 300, 500, 500)

    def show_info(self):
        self.statistics_labels = []
        for id, statistic in enumerate(self.statistics):
            self.statistics_labels.append(QtWidgets.QLabel(self))
            self.statistics_labels[id].setText(
                f'Статистика по {statistic.shooter.name}: '
                f'Выстрелов - {statistic.attempts}, попал: {"Да" if statistic.success else "Нет"}'
            )
            self.statistics_labels[id].move(10, (20 * id) + 30)
            self.statistics_labels[id].adjustSize()

    def close_button_event(self):
        self.close()

    def init_close_button(self):
        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setText('Закрыть')
        self.start_button.adjustSize()
        self.start_button.move(190, 400)
        self.start_button.clicked.connect(self.close_button_event)
