# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playground_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
from . import resources_rc

class Ui_PlaygroundMainWindow(object):
    def setupUi(self, PlaygroundMainWindow):
        if not PlaygroundMainWindow.objectName():
            PlaygroundMainWindow.setObjectName(u"PlaygroundMainWindow")
        PlaygroundMainWindow.resize(800, 600)
        self.action_about = QAction(PlaygroundMainWindow)
        self.action_about.setObjectName(u"action_about")
        self.central_widget = QWidget(PlaygroundMainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.input_line_edit = QLineEdit(self.central_widget)
        self.input_line_edit.setObjectName(u"input_line_edit")
        self.input_line_edit.setGeometry(QRect(120, 100, 113, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_line_edit.sizePolicy().hasHeightForWidth())
        self.input_line_edit.setSizePolicy(sizePolicy)
        self.message_button = QPushButton(self.central_widget)
        self.message_button.setObjectName(u"message_button")
        self.message_button.setGeometry(QRect(400, 120, 100, 32))
        self.output_plain_text_edit = QPlainTextEdit(self.central_widget)
        self.output_plain_text_edit.setObjectName(u"output_plain_text_edit")
        self.output_plain_text_edit.setGeometry(QRect(150, 180, 251, 181))
        self.show_messages_button = QPushButton(self.central_widget)
        self.show_messages_button.setObjectName(u"show_messages_button")
        self.show_messages_button.setGeometry(QRect(390, 390, 121, 32))
        sizePolicy.setHeightForWidth(self.show_messages_button.sizePolicy().hasHeightForWidth())
        self.show_messages_button.setSizePolicy(sizePolicy)
        PlaygroundMainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(PlaygroundMainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 800, 33))
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        PlaygroundMainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(PlaygroundMainWindow)
        self.status_bar.setObjectName(u"status_bar")
        PlaygroundMainWindow.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(PlaygroundMainWindow)

        QMetaObject.connectSlotsByName(PlaygroundMainWindow)
    # setupUi

    def retranslateUi(self, PlaygroundMainWindow):
        PlaygroundMainWindow.setWindowTitle(QCoreApplication.translate("PlaygroundMainWindow", u"MainWindow", None))
        self.action_about.setText(QCoreApplication.translate("PlaygroundMainWindow", u"About", None))
        self.message_button.setText(QCoreApplication.translate("PlaygroundMainWindow", u"Message", None))
        self.show_messages_button.setText(QCoreApplication.translate("PlaygroundMainWindow", u"Show Messages", None))
        self.menu_help.setTitle(QCoreApplication.translate("PlaygroundMainWindow", u"Help", None))
    # retranslateUi
