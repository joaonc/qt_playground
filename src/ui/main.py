import sys

from PySide6.QtWidgets import QApplication, QWidget


def main():
    # Need one (and only one) `QApplication` instance per application.
    # Pass in `sys.argv` to allow command line arguments for the app.
    # If command line arguments re not used, `QApplication([])` works too.
    app = QApplication(sys.argv)
    window = QWidget()  # Create a Qt widget, which will be our window.
    window.show()  # Windows are hidden by default.

    # Start the event loop.
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
