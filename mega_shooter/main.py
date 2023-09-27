from PyQt5.QtWidgets import QApplication

from mega_shooter.ui.main_window import MainWindow
import sys


def start():
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
