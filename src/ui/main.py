import sys

from PySide6.QtWidgets import QApplication, QWidget

from src.ui.forms.main_ui import Ui_mainForm


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)

        # UI bindings
        self.ui.messagePushButton.clicked.connect(self.send_message)

    def send_message(self):
        input_text = self.ui.inputLineEdit.text()
        self.ui.outputPlainTextEdit.appendPlainText(input_text)
        self.ui.inputLineEdit.clear()


def main(argv: list | None = None):
    app = QApplication(argv or [])
    my_app = MyApp()

    # # Access components
    # print(my_app.messagePushButton.text())

    my_app.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
