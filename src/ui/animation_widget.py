from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget

from src.ui.forms.ui_animation_widget import Ui_AnimationWidget


class AnimationWidget(QWidget, Ui_AnimationWidget):
    def __init__(self, gif_path):
        super().__init__()
        self.setupUi(self)

        self.movie = QMovie(str(gif_path))
        self.animation_label.setMovie(self.movie)
        self.movie.start()
