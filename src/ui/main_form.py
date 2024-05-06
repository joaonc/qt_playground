from PySide6.QtWidgets import QWidget

from src.ui.forms.main_ui import Ui_mainForm
from ui.forms.show_message_ui import Ui_showMesssageDialog


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)

        # UI bindings
        self.ui.messagePushButton.clicked.connect(self.send_message)
        self.ui.showMessagesPushButton.clicked.connect(self.show_message)

    def send_message(self):
        input_text = self.ui.inputLineEdit.text()
        self.ui.outputPlainTextEdit.appendPlainText(input_text)
        self.ui.inputLineEdit.clear()

    def show_message(self):
        dialog = Ui_showMesssageDialog()
        dialog.setupUi(self)
        dialog.messagePlainTextEdit.setPlainText(self.ui.outputPlainTextEdit.toPlainText())
