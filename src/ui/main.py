import sys

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

from src import ASSETS_DIR


def main():
    # Need one (and only one) `QApplication` instance per application.
    # `sys.argv` to allow command line arguments for the app.
    # If command line arguments re not used, `QApplication([])` works too.
    app = QApplication(sys.argv)
    file = QFile(ASSETS_DIR / 'ui/main.ui')
    file.open(QFile.OpenModeFlag.ReadOnly)
    loader = QUiLoader()
    dialog = loader.load(file)
    dialog.show()

    # Start the event loop.
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
