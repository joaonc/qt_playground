from PySide6.QtWidgets import QWidget

from src.ui.forms.main_ui import Ui_mainForm

class MainForm(QWidget):
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
