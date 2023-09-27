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

    sys.exit(app.exec_())
