from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QDialog

from ui.forms.ui_animation_dialog import Ui_AnimationDialog


class AnimationDialog(QDialog, Ui_AnimationDialog):
    def __init__(self, gif_path):
        super().__init__()
        self.setupUi(self)

        self.movie = QMovie(str(gif_path))
        self.animation_label.setMovie(self.movie)
        self.movie.start()
