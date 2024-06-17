from PySide6.QtWidgets import QDialog

from src.ui.forms.ui_show_message_dialog import Ui_ShowMesssageDialog


class ShowMessageDialog(QDialog, Ui_ShowMesssageDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
