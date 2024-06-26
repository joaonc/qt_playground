# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QWidget)
from . import resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/images/playground_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsDialog.setWindowIcon(icon)
        self.button_box = QDialogButtonBox(SettingsDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setGeometry(QRect(30, 240, 341, 32))
        self.button_box.setOrientation(Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.theme_label = QLabel(SettingsDialog)
        self.theme_label.setObjectName(u"theme_label")
        self.theme_label.setGeometry(QRect(20, 20, 49, 16))
        self.theme_combo_box = QComboBox(SettingsDialog)
        self.theme_combo_box.setObjectName(u"theme_combo_box")
        self.theme_combo_box.setGeometry(QRect(80, 20, 68, 22))

        self.retranslateUi(SettingsDialog)
        self.button_box.accepted.connect(SettingsDialog.accept)
        self.button_box.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.theme_label.setText(QCoreApplication.translate("SettingsDialog", u"Theme", None))
    # retranslateUi

