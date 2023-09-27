from typing import List

from PyQt5.QtWidgets import QApplication

from mega_shooter.humanity.base_human import BaseHuman
from mega_shooter.humanity import Trainee, Middle, Senior
from mega_shooter.modelling.modeller import Loop
from mega_shooter.ui.main_window import MainWindow
import sys


def start():
    app = QApplication(sys.argv)
    window = MainWindow()

    shooters: List[BaseHuman] = [
        Trainee('Name_1', 17, 1),
        Middle('Name_2', 40, 10),
        Senior('Name_3', 68, 60),
        Middle('Name_4', 39, 9),
        Trainee('Name_5', 50, 4),
        Middle('Name_6', 25, 15),
        Senior('Name_7', 40, 30),
    ]
    window.attach_shooters(shooters)
    window.update()
    sys.exit(app.exec_())
