from enum import Enum

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QStyleFactory

from src.ui.forms.ui_settings_dialog import Ui_SettingsDialog
from src.utils import OsData, OsName


class Settings(str, Enum):  # Can be `StrEnum` on python 3.11+
    Style = 'Style'


_styles = {style: OsData(style) for style in QStyleFactory.keys()} | {
    'Windows': OsData('Windows Classic', os_include=[OsName.Windows]),
    'windows11': OsData('Windows 11', os_include=[OsName.Windows]),
    'windowsvista': OsData('Windows Vista', os_include=[OsName.Windows]),
}
"""
Keys: Qt stored name for the style.

Values: Instance of ``OsData`` with a friendly name for the style in ``data`` and the OS platforms
the style applies to.
"""


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings = QSettings()

        for style_qt_name, os_data in _styles.items():
            if os_data.applies():
                style_friendly_name = os_data.data
                self.theme_combo_box.addItem(style_friendly_name, style_qt_name)

    def accept(self):
        style_qt = next(
            k for k, v in _styles.items() if v.data == self.theme_combo_box.currentText()
        )
        self.settings.setValue(Settings.Style, style_qt)

        super().accept()
