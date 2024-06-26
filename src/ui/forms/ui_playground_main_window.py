# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playground_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_PlaygroundMainWindow(object):
    def setupUi(self, PlaygroundMainWindow):
        if not PlaygroundMainWindow.objectName():
            PlaygroundMainWindow.setObjectName(u"PlaygroundMainWindow")
        PlaygroundMainWindow.resize(267, 348)
        icon = QIcon()
        icon.addFile(u":/images/playground_icon_187860_256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        PlaygroundMainWindow.setWindowIcon(icon)
        self.action_about = QAction(PlaygroundMainWindow)
        self.action_about.setObjectName(u"action_about")
        icon1 = QIcon()
        icon1.addFile(u":/images/about_icon_512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_about.setIcon(icon1)
        self.action_quit = QAction(PlaygroundMainWindow)
        self.action_quit.setObjectName(u"action_quit")
        icon2 = QIcon()
        icon2.addFile(u":/images/cancel-close-cross-delete_icon_114048_512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_quit.setIcon(icon2)
        self.action_check_for_updates = QAction(PlaygroundMainWindow)
        self.action_check_for_updates.setObjectName(u"action_check_for_updates")
        self.action_about_qt = QAction(PlaygroundMainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        icon3 = QIcon()
        icon3.addFile(u":/images/about_qt_icon_512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_about_qt.setIcon(icon3)
        self.central_widget = QWidget(PlaygroundMainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontal_layout_1 = QHBoxLayout()
        self.horizontal_layout_1.setObjectName(u"horizontal_layout_1")
        self.input_line_edit = QLineEdit(self.central_widget)
        self.input_line_edit.setObjectName(u"input_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_line_edit.sizePolicy().hasHeightForWidth())
        self.input_line_edit.setSizePolicy(sizePolicy)

        self.horizontal_layout_1.addWidget(self.input_line_edit)

        self.message_button = QPushButton(self.central_widget)
        self.message_button.setObjectName(u"message_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.message_button.sizePolicy().hasHeightForWidth())
        self.message_button.setSizePolicy(sizePolicy1)

        self.horizontal_layout_1.addWidget(self.message_button)


        self.verticalLayout.addLayout(self.horizontal_layout_1)

        self.output_plain_text_edit = QPlainTextEdit(self.central_widget)
        self.output_plain_text_edit.setObjectName(u"output_plain_text_edit")

        self.verticalLayout.addWidget(self.output_plain_text_edit)

        self.show_messages_button = QPushButton(self.central_widget)
        self.show_messages_button.setObjectName(u"show_messages_button")
        sizePolicy1.setHeightForWidth(self.show_messages_button.sizePolicy().hasHeightForWidth())
        self.show_messages_button.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.show_messages_button)

        PlaygroundMainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(PlaygroundMainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 267, 33))
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        PlaygroundMainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(PlaygroundMainWindow)
        self.status_bar.setObjectName(u"status_bar")
        PlaygroundMainWindow.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(PlaygroundMainWindow)
        self.tool_bar.setObjectName(u"tool_bar")
        PlaygroundMainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tool_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_check_for_updates)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_file.addAction(self.action_quit)
        self.tool_bar.addAction(self.action_quit)

        self.retranslateUi(PlaygroundMainWindow)

        QMetaObject.connectSlotsByName(PlaygroundMainWindow)
    # setupUi

    def retranslateUi(self, PlaygroundMainWindow):
        PlaygroundMainWindow.setWindowTitle(QCoreApplication.translate("PlaygroundMainWindow", u"MainWindow", None))
        self.action_about.setText(QCoreApplication.translate("PlaygroundMainWindow", u"About", None))
        self.action_quit.setText(QCoreApplication.translate("PlaygroundMainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("PlaygroundMainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_check_for_updates.setText(QCoreApplication.translate("PlaygroundMainWindow", u"&Check for updates", None))
        self.action_about_qt.setText(QCoreApplication.translate("PlaygroundMainWindow", u"About &Qt", None))
        self.message_button.setText(QCoreApplication.translate("PlaygroundMainWindow", u"Message", None))
        self.show_messages_button.setText(QCoreApplication.translate("PlaygroundMainWindow", u"Show Messages", None))
        self.menu_help.setTitle(QCoreApplication.translate("PlaygroundMainWindow", u"&Help", None))
        self.menu_file.setTitle(QCoreApplication.translate("PlaygroundMainWindow", u"&File", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("PlaygroundMainWindow", u"toolBar", None))
    # retranslateUi

