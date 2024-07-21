# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_AnimationWidget(object):
    def setupUi(self, AnimationWidget):
        if not AnimationWidget.objectName():
            AnimationWidget.setObjectName(u"AnimationWidget")
        AnimationWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AnimationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.animation_label = QLabel(AnimationWidget)
        self.animation_label.setObjectName(u"animation_label")

        self.verticalLayout.addWidget(self.animation_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_button = QPushButton(AnimationWidget)
        self.play_button.setObjectName(u"play_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setMinimumSize(QSize(100, 100))
        icon = QIcon()
        icon.addFile(u":/images/play_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.play_button)

        self.stop_button = QPushButton(AnimationWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMinimumSize(QSize(100, 100))
        icon1 = QIcon()
        icon1.addFile(u":/images/stop_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AnimationWidget)

        QMetaObject.connectSlotsByName(AnimationWidget)
    # setupUi

    def retranslateUi(self, AnimationWidget):
        AnimationWidget.setWindowTitle(QCoreApplication.translate("AnimationWidget", u"Form", None))
        self.animation_label.setText(QCoreApplication.translate("AnimationWidget", u"Animation", None))
        self.play_button.setText(QCoreApplication.translate("AnimationWidget", u"Play", None))
        self.stop_button.setText(QCoreApplication.translate("AnimationWidget", u"Stop", None))
    # retranslateUi

