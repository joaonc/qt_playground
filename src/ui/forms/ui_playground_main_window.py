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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
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
        self.menu_help.setTitle(QCoreApplication.translate("PlaygroundMainWindow", u"Help", None))
    # retranslateUi

