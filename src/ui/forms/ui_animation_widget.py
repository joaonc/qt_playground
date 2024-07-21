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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_AnimationWidget(object):
    def setupUi(self, AnimationWidget):
        if not AnimationWidget.objectName():
            AnimationWidget.setObjectName(u"AnimationWidget")
        AnimationWidget.resize(400, 300)
        self.animation_label = QLabel(AnimationWidget)
        self.animation_label.setObjectName(u"animation_label")
        self.animation_label.setGeometry(QRect(100, 100, 49, 16))

        self.retranslateUi(AnimationWidget)

        QMetaObject.connectSlotsByName(AnimationWidget)
    # setupUi

    def retranslateUi(self, AnimationWidget):
        AnimationWidget.setWindowTitle(QCoreApplication.translate("AnimationWidget", u"Form", None))
        self.animation_label.setText(QCoreApplication.translate("AnimationWidget", u"TextLabel", None))
    # retranslateUi

