# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converterUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(14)
        MainAppWindow.setFont(font)
        self.centralwidget = QWidget(MainAppWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainAppFrame = QFrame(self.centralwidget)
        self.mainAppFrame.setObjectName(u"mainAppFrame")
        self.mainAppFrame.setFrameShape(QFrame.StyledPanel)
        self.mainAppFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.mainAppFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.mainAppFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.mainAppFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.movFolderButton = QPushButton(self.frame_5)
        self.movFolderButton.setObjectName(u"movFolderButton")

        self.gridLayout_5.addWidget(self.movFolderButton, 0, 1, 1, 1)

        self.conversionButton = QPushButton(self.frame_5)
        self.conversionButton.setObjectName(u"conversionButton")

        self.gridLayout_5.addWidget(self.conversionButton, 0, 2, 1, 1)

        self.exrFolderButton = QPushButton(self.frame_5)
        self.exrFolderButton.setObjectName(u"exrFolderButton")

        self.gridLayout_5.addWidget(self.exrFolderButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.mainAppFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.conversionLogTextEdit = QPlainTextEdit(self.frame_8)
        self.conversionLogTextEdit.setObjectName(u"conversionLogTextEdit")

        self.gridLayout_8.addWidget(self.conversionLogTextEdit, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.gridLayout_9.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.mainAppFrame, 0, 0, 1, 1)

        MainAppWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainAppWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainAppWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainAppWindow)

        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"Converter v0.1", None))
        self.label.setText(QCoreApplication.translate("MainAppWindow", u"EXR to MOV Converter V0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainAppWindow", u"Controls:", None))
        self.movFolderButton.setText(QCoreApplication.translate("MainAppWindow", u"MOV Folder", None))
        self.conversionButton.setText(QCoreApplication.translate("MainAppWindow", u"Convert", None))
        self.exrFolderButton.setText(QCoreApplication.translate("MainAppWindow", u"EXR Sequence Folder", None))
        self.label_4.setText(QCoreApplication.translate("MainAppWindow", u"Log:", None))
    # retranslateUi

