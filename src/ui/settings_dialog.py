from PySide6.QtWidgets import QDialog

from ui.forms.ui_settings_dialog import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
