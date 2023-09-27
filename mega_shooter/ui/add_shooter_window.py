from PyQt5 import QtWidgets


class AddShooterWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_window()
        self.init_add_button()
        self.init_inputs()

    def init_inputs(self):
        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.move(10, 10)
        self.name_input.setPlaceholderText('Имя')
        self.name_input.setFixedWidth(100)
        self.age_input = QtWidgets.QLineEdit(self)
        self.age_input.move(120, 10)
        self.age_input.setPlaceholderText('Возраст')
        self.age_input.setFixedWidth(100)
        self.experience_input = QtWidgets.QLineEdit(self)
        self.experience_input.move(230, 10)
        self.experience_input.setPlaceholderText('Опыт')
        self.experience_input.setFixedWidth(100)
        self.shooter_type = QtWidgets.QComboBox(self)
        self.shooter_type.addItem('Новичок')
        self.shooter_type.addItem('Опытный')
        self.shooter_type.addItem('Ветеран')
        self.shooter_type.move(340, 10)
        self.shooter_type.setFixedWidth(100)


    def init_window(self):
        self.setWindowTitle('Добавить стрелка')
        self.setGeometry(500, 300, 500, 200)

    def add_button_event(self):
        self.main_window.attach_shooter(
            self.name_input.text(),
            int(self.age_input.text()),
            int(self.experience_input.text()),
            self.shooter_type.currentText()
        )
        self.close()

    def init_add_button(self):
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setText('Добавить')
        self.add_button.adjustSize()
        self.add_button.move(190, 150)
        self.add_button.clicked.connect(self.add_button_event)
