import logging
from typing import cast

from PySide6.QtCore import QCoreApplication, QSettings
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QStyleFactory

import src.config as config
import src.update.update as update
from src.ui.animation_dialog import AnimationDialog
from src.ui.forms.ui_playground_main_window import Ui_PlaygroundMainWindow
from src.ui.settings_dialog import Settings, SettingsDialog
from src.ui.show_message_dialog import ShowMessageDialog


class PlaygroundMainWindow(QMainWindow, Ui_PlaygroundMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.app = cast(QApplication, QApplication.instance())

        # UI bindings
        self.message_button.clicked.connect(self.send_message)
        self.show_messages_button.clicked.connect(self.show_message)
        self.action_animation.triggered.connect(self.show_animation)
        self.action_settings.triggered.connect(self.settings)
        self.action_quit.triggered.connect(self.close)
        self.action_check_for_updates.triggered.connect(self.check_for_updates)
        self.action_about.triggered.connect(self.about)
        self.action_about_qt.triggered.connect(self.about_qt)

        # Set `QSettings` defaults so `QSettings()` can be used anywhere.
        # As opposed to setting the values each time `QSettings` is instantiated
        QCoreApplication.setOrganizationName(config.ORGANIZATION_NAME)
        QCoreApplication.setOrganizationDomain(config.ORGANIZATION_DOMAIN)
        QCoreApplication.setApplicationName(config.APPLICATION_NAME)

        self.set_style()

    def send_message(self):
        input_text = self.input_line_edit.text()
        self.output_plain_text_edit.appendPlainText(input_text)
        self.input_line_edit.clear()

    def show_message(self):
        dialog = ShowMessageDialog()
        dialog.message_plain_text_edit.setPlainText(self.output_plain_text_edit.toPlainText())
        result = dialog.exec()
        print(result)

    def show_animation(self):
        dialog = AnimationDialog(config.ASSETS_DIR / 'images' / 'button.gif')
        dialog.exec()

    # noinspection PyMethodMayBeStatic
    def settings(self):
        dialog = SettingsDialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            self.set_style()

    def set_style(self):
        settings = QSettings()
        style = settings.value(Settings.Style)
        self.app.setStyle(QStyleFactory.create(style))  # type: ignore
        logging.debug(f'Style `{style}` applied.')

    def check_for_updates(self):
        need_update, version_update = update.check_update()
        if need_update:
            QMessageBox.information(
                self,
                'App update',
                f'Version {version_update} available. It will be installed when exiting this app.',
            )
        else:
            QMessageBox.information(self, 'App update', 'No new version available.')

    def about(self):
        QMessageBox.information(
            self,
            'About Qt Playground',
            f'Codebase to learn Qt by example.\nv {config.version}',
        )

    # noinspection PyMethodMayBeStatic
    def about_qt(self):
        QApplication.aboutQt()
