from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QDialog

from src.ui.forms.ui_animation_dialog import Ui_AnimationDialog


class AnimationDialog(QDialog, Ui_AnimationDialog):
    def __init__(self, gif_path):
        super().__init__()
        self.setupUi(self)

        # UI bindings
        self.movie = QMovie(str(gif_path))
        self.animation_label.setMovie(self.movie)
        self.play_button.clicked.connect(self.animation_start)
        self.stop_button.clicked.connect(self.animation_stop)

        self.animation_start()

    def animation_start(self):
        self.movie.start()

    def animation_stop(self):
        self.movie.stop()
