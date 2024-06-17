import sys

from PySide6.QtWidgets import QApplication

from ui.playground_main_window import PlaygroundMainWindow


def main(argv: list | None = None):
    app = QApplication(argv or [])
    window = PlaygroundMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
