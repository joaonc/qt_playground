# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playground_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_PlaygroundWidget(object):
    def setupUi(self, PlaygroundWidget):
        if not PlaygroundWidget.objectName():
            PlaygroundWidget.setObjectName(u"PlaygroundWidget")
        PlaygroundWidget.resize(328, 299)
        self.inputLineEdit = QLineEdit(PlaygroundWidget)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        self.inputLineEdit.setGeometry(QRect(40, 30, 113, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLineEdit.sizePolicy().hasHeightForWidth())
        self.inputLineEdit.setSizePolicy(sizePolicy)
        self.messagePushButton = QPushButton(PlaygroundWidget)
        self.messagePushButton.setObjectName(u"messagePushButton")
        self.messagePushButton.setGeometry(QRect(190, 30, 100, 32))
        self.outputPlainTextEdit = QPlainTextEdit(PlaygroundWidget)
        self.outputPlainTextEdit.setObjectName(u"outputPlainTextEdit")
        self.outputPlainTextEdit.setGeometry(QRect(40, 70, 251, 181))
        self.showMessagesPushButton = QPushButton(PlaygroundWidget)
        self.showMessagesPushButton.setObjectName(u"showMessagesPushButton")
        self.showMessagesPushButton.setGeometry(QRect(169, 260, 121, 32))
        sizePolicy.setHeightForWidth(self.showMessagesPushButton.sizePolicy().hasHeightForWidth())
        self.showMessagesPushButton.setSizePolicy(sizePolicy)

        self.retranslateUi(PlaygroundWidget)

        QMetaObject.connectSlotsByName(PlaygroundWidget)
    # setupUi

    def retranslateUi(self, PlaygroundWidget):
        PlaygroundWidget.setWindowTitle(QCoreApplication.translate("PlaygroundWidget", u"Qt Playground", None))
        self.messagePushButton.setText(QCoreApplication.translate("PlaygroundWidget", u"Message", None))
        self.showMessagesPushButton.setText(QCoreApplication.translate("PlaygroundWidget", u"Show Messages", None))
    # retranslateUi

