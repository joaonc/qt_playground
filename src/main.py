import sys

from PySide6.QtWidgets import QApplication

from ui.main_form import MainForm


def main(argv: list | None = None):
    app = QApplication(argv or [])
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
