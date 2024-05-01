# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_mainMainWindow(object):
    def setupUi(self, mainMainWindow):
        if not mainMainWindow.objectName():
            mainMainWindow.setObjectName(u"mainMainWindow")
        mainMainWindow.resize(528, 474)
        self.centralwidget = QWidget(mainMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.textLineEdit = QLineEdit(self.centralwidget)
        self.textLineEdit.setObjectName(u"textLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLineEdit.sizePolicy().hasHeightForWidth())
        self.textLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.textLineEdit, 0, 0, 1, 1)

        self.okPushButton = QPushButton(self.centralwidget)
        self.okPushButton.setObjectName(u"okPushButton")
        sizePolicy.setHeightForWidth(self.okPushButton.sizePolicy().hasHeightForWidth())
        self.okPushButton.setSizePolicy(sizePolicy)
        self.okPushButton.setFlat(False)

        self.gridLayout.addWidget(self.okPushButton, 2, 3, 1, 1)

        self.viewTextPushButton = QPushButton(self.centralwidget)
        self.viewTextPushButton.setObjectName(u"viewTextPushButton")
        sizePolicy.setHeightForWidth(self.viewTextPushButton.sizePolicy().hasHeightForWidth())
        self.viewTextPushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.viewTextPushButton, 0, 1, 1, 1)

        mainMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 37))
        mainMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainMainWindow)
        self.okPushButton.clicked.connect(mainMainWindow.close)

        QMetaObject.connectSlotsByName(mainMainWindow)
    # setupUi

    def retranslateUi(self, mainMainWindow):
        mainMainWindow.setWindowTitle(QCoreApplication.translate("mainMainWindow", u"MainWindow", None))
        self.okPushButton.setText(QCoreApplication.translate("mainMainWindow", u"Ok", None))
        self.viewTextPushButton.setText(QCoreApplication.translate("mainMainWindow", u"View Text", None))
    # retranslateUi

