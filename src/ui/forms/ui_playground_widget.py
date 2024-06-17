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
from . import resources_rc

class Ui_PlaygroundWidget(object):
    def setupUi(self, PlaygroundWidget):
        if not PlaygroundWidget.objectName():
            PlaygroundWidget.setObjectName(u"PlaygroundWidget")
        PlaygroundWidget.resize(328, 299)
        icon = QIcon()
        icon.addFile(u":/images/playground_icon_187860_256.png", QSize(), QIcon.Normal, QIcon.Off)
        PlaygroundWidget.setWindowIcon(icon)
        self.input_line_edit = QLineEdit(PlaygroundWidget)
        self.input_line_edit.setObjectName(u"input_line_edit")
        self.input_line_edit.setGeometry(QRect(40, 30, 113, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_line_edit.sizePolicy().hasHeightForWidth())
        self.input_line_edit.setSizePolicy(sizePolicy)
        self.message_button = QPushButton(PlaygroundWidget)
        self.message_button.setObjectName(u"message_button")
        self.message_button.setGeometry(QRect(190, 30, 100, 32))
        self.output_plain_text_edit = QPlainTextEdit(PlaygroundWidget)
        self.output_plain_text_edit.setObjectName(u"output_plain_text_edit")
        self.output_plain_text_edit.setGeometry(QRect(40, 70, 251, 181))
        self.show_messages_button = QPushButton(PlaygroundWidget)
        self.show_messages_button.setObjectName(u"show_messages_button")
        self.show_messages_button.setGeometry(QRect(169, 260, 121, 32))
        sizePolicy.setHeightForWidth(self.show_messages_button.sizePolicy().hasHeightForWidth())
        self.show_messages_button.setSizePolicy(sizePolicy)

        self.retranslateUi(PlaygroundWidget)

        QMetaObject.connectSlotsByName(PlaygroundWidget)
    # setupUi

    def retranslateUi(self, PlaygroundWidget):
        PlaygroundWidget.setWindowTitle(QCoreApplication.translate("PlaygroundWidget", u"Qt Playground", None))
        self.message_button.setText(QCoreApplication.translate("PlaygroundWidget", u"Message", None))
        self.show_messages_button.setText(QCoreApplication.translate("PlaygroundWidget", u"Show Messages", None))
    # retranslateUi

