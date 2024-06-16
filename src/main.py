import sys

from PySide6.QtWidgets import QApplication

from src.ui.playground_widget import PlaygroundWidget


def main(argv: list | None = None):
    app = QApplication(argv or [])
    main_form = PlaygroundWidget()
    main_form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
