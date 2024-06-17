from PySide6.QtWidgets import QMainWindow

from src.ui.forms.ui_playground_main_window import Ui_PlaygroundMainWindow
from src.ui.show_message_dialog import ShowMessageDialog


class PlaygroundMainWindow(QMainWindow, Ui_PlaygroundMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI bindings
        self.message_button.clicked.connect(self.send_message)
        self.show_messages_button.clicked.connect(self.show_message)

    def send_message(self):
        input_text = self.input_line_edit.text()
        self.output_plain_text_edit.appendPlainText(input_text)
        self.input_line_edit.clear()

    def show_message(self):
        dialog = ShowMessageDialog()
        dialog.message_plain_text_edit.setPlainText(self.output_plain_text_edit.toPlainText())
        result = dialog.exec()
        print(result)
