from enum import StrEnum

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QStyleFactory

from ui.forms.ui_settings_dialog import Ui_SettingsDialog


class Settings(StrEnum):
    Style = 'Style'


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.settings = QSettings()

        # styles = [style for style in QStyleFactory.keys() if style[0].isupper()]
        styles = QStyleFactory.keys()
        current_theme: str = self.settings.value(Settings.Style, styles[0], str)  # type: ignore
        self.theme_combo_box.addItems(styles)
        self.theme_combo_box.setCurrentIndex(styles.index(current_theme))

    def accept(self):
        self.settings.setValue(Settings.Style, self.theme_combo_box.currentText())

        super().accept()
