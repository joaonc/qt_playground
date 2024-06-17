# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_message_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_ShowMesssageDialog(object):
    def setupUi(self, ShowMesssageDialog):
        if not ShowMesssageDialog.objectName():
            ShowMesssageDialog.setObjectName(u"ShowMesssageDialog")
        ShowMesssageDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/images/playground_icon_187860_256.png", QSize(), QIcon.Normal, QIcon.Off)
        ShowMesssageDialog.setWindowIcon(icon)
        self.vertical_layout = QVBoxLayout(ShowMesssageDialog)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.message_plain_text_edit = QPlainTextEdit(ShowMesssageDialog)
        self.message_plain_text_edit.setObjectName(u"message_plain_text_edit")

        self.vertical_layout.addWidget(self.message_plain_text_edit)

        self.button_box = QDialogButtonBox(ShowMesssageDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.vertical_layout.addWidget(self.button_box)


        self.retranslateUi(ShowMesssageDialog)
        self.button_box.accepted.connect(ShowMesssageDialog.accept)
        self.button_box.rejected.connect(ShowMesssageDialog.reject)

        QMetaObject.connectSlotsByName(ShowMesssageDialog)
    # setupUi

    def retranslateUi(self, ShowMesssageDialog):
        ShowMesssageDialog.setWindowTitle(QCoreApplication.translate("ShowMesssageDialog", u"Show message", None))
    # retranslateUi

