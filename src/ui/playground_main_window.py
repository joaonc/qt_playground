from PySide6.QtWidgets import QMainWindow, QMessageBox

import src.config as config
from src.ui.forms.ui_playground_main_window import Ui_PlaygroundMainWindow
from src.ui.show_message_dialog import ShowMessageDialog
import src.update.update as update


class PlaygroundMainWindow(QMainWindow, Ui_PlaygroundMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # UI bindings
        self.message_button.clicked.connect(self.send_message)
        self.show_messages_button.clicked.connect(self.show_message)
        self.action_quit.triggered.connect(self.close)
        self.action_check_for_updates.triggered.connect(self.check_for_updates)
        self.action_about.triggered.connect(self.about)

    def send_message(self):
        input_text = self.input_line_edit.text()
        self.output_plain_text_edit.appendPlainText(input_text)
        self.input_line_edit.clear()

    def show_message(self):
        dialog = ShowMessageDialog()
        dialog.message_plain_text_edit.setPlainText(self.output_plain_text_edit.toPlainText())
        result = dialog.exec()
        print(result)

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
