from enum import Enum

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QStyleFactory

from src.ui.forms.ui_settings_dialog import Ui_SettingsDialog


class Settings(str, Enum):  # Can be `StrEnum` on python 3.11+
    Style = 'Style'


_styles = {style: style for style in QStyleFactory.keys()} | {
    'Windows': 'Windows Classic',
    'windows11': 'Windows 11',
    'windowsvista': 'Windows Vista',
}
"""Qt stored name (keys) / Style friendly name (values)"""


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings = QSettings()

        for style_qt, style_friendly in _styles.items():
            self.theme_combo_box.addItem(style_friendly, style_qt)

    def accept(self):
        style_qt = next(k for k, v in _styles.items() if v == self.theme_combo_box.currentText())
        self.settings.setValue(Settings.Style, style_qt)

        super().accept()
