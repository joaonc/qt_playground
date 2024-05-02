import sys

from PySide6.QtWidgets import QApplication, QWidget

from src.ui.forms.main_ui import Ui_mainForm


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        ui = Ui_mainForm()
        ui.setupUi(self)


def main(argv):
    app = QApplication(argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
