from PySide6.QtWidgets import QWidget

from src.ui.forms.ui_playground_widget import Ui_PlaygroundWidget
from src.ui.forms.ui_show_message import Ui_ShowMesssageDialog


class PlaygroundWidget(QWidget, Ui_PlaygroundWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI bindings
        self.messagePushButton.clicked.connect(self.send_message)
        self.showMessagesPushButton.clicked.connect(self.show_message)

    def send_message(self):
        input_text = self.inputLineEdit.text()
        self.outputPlainTextEdit.appendPlainText(input_text)
        self.inputLineEdit.clear()

    def show_message(self):
        dialog = Ui_ShowMesssageDialog()
        dialog.setupUi(self)
        dialog.messagePlainTextEdit.setPlainText(self.outputPlainTextEdit.toPlainText())
