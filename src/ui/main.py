import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.ui.forms.main_window_ui import Ui_MainWindow


def main():
    # Need one (and only one) `QApplication` instance per application.
    # `sys.argv` to allow command line arguments for the app.
    # If command line arguments re not used, `QApplication([])` works too.
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    # Start the event loop.
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
