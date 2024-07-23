# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_AnimationDialog(object):
    def setupUi(self, AnimationDialog):
        if not AnimationDialog.objectName():
            AnimationDialog.setObjectName(u"AnimationDialog")
        AnimationDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AnimationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.animation_label = QLabel(AnimationDialog)
        self.animation_label.setObjectName(u"animation_label")

        self.verticalLayout.addWidget(self.animation_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_button = QPushButton(AnimationDialog)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setMinimumSize(QSize(0, 100))
        icon = QIcon()
        icon.addFile(u":/images/play_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.play_button)

        self.stop_button = QPushButton(AnimationDialog)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 100))
        icon1 = QIcon()
        icon1.addFile(u":/images/stop_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AnimationDialog)

        QMetaObject.connectSlotsByName(AnimationDialog)
    # setupUi

    def retranslateUi(self, AnimationDialog):
        AnimationDialog.setWindowTitle(QCoreApplication.translate("AnimationDialog", u"Animation", None))
        self.animation_label.setText(QCoreApplication.translate("AnimationDialog", u"Animation", None))
        self.play_button.setText(QCoreApplication.translate("AnimationDialog", u"Play", None))
        self.stop_button.setText(QCoreApplication.translate("AnimationDialog", u"Stop", None))
    # retranslateUi

