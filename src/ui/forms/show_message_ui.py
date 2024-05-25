# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_message.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_showMesssageDialog(object):
    def setupUi(self, showMesssageDialog):
        if not showMesssageDialog.objectName():
            showMesssageDialog.setObjectName(u"showMesssageDialog")
        showMesssageDialog.resize(400, 300)
        self.gridLayout = QGridLayout(showMesssageDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.messagePlainTextEdit = QPlainTextEdit(showMesssageDialog)
        self.messagePlainTextEdit.setObjectName(u"messagePlainTextEdit")

        self.gridLayout.addWidget(self.messagePlainTextEdit, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(showMesssageDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(showMesssageDialog)
        self.buttonBox.accepted.connect(showMesssageDialog.accept)
        self.buttonBox.rejected.connect(showMesssageDialog.reject)

        QMetaObject.connectSlotsByName(showMesssageDialog)
    # setupUi

    def retranslateUi(self, showMesssageDialog):
        showMesssageDialog.setWindowTitle(QCoreApplication.translate("showMesssageDialog", u"Dialog", None))
    # retranslateUi

