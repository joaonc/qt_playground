# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        if not mainForm.objectName():
            mainForm.setObjectName(u"mainForm")
        mainForm.resize(328, 299)
        self.inputLineEdit = QLineEdit(mainForm)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        self.inputLineEdit.setGeometry(QRect(40, 30, 113, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLineEdit.sizePolicy().hasHeightForWidth())
        self.inputLineEdit.setSizePolicy(sizePolicy)
        self.messagePushButton = QPushButton(mainForm)
        self.messagePushButton.setObjectName(u"messagePushButton")
        self.messagePushButton.setGeometry(QRect(190, 30, 100, 32))
        self.outputPlainTextEdit = QPlainTextEdit(mainForm)
        self.outputPlainTextEdit.setObjectName(u"outputPlainTextEdit")
        self.outputPlainTextEdit.setGeometry(QRect(40, 70, 251, 181))
        self.showMessagesPushButton = QPushButton(mainForm)
        self.showMessagesPushButton.setObjectName(u"showMessagesPushButton")
        self.showMessagesPushButton.setGeometry(QRect(169, 260, 121, 32))
        sizePolicy.setHeightForWidth(self.showMessagesPushButton.sizePolicy().hasHeightForWidth())
        self.showMessagesPushButton.setSizePolicy(sizePolicy)

        self.retranslateUi(mainForm)

        QMetaObject.connectSlotsByName(mainForm)
    # setupUi

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QCoreApplication.translate("mainForm", u"Qt Playground", None))
        self.messagePushButton.setText(QCoreApplication.translate("mainForm", u"Message", None))
        self.showMessagesPushButton.setText(QCoreApplication.translate("mainForm", u"Show Messages", None))
    # retranslateUi

