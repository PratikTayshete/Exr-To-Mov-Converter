# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converterUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(800, 168)
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        Converter.setFont(font)
        Converter.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Converter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exr_folder_path_lineEdit = QLineEdit(self.centralwidget)
        self.exr_folder_path_lineEdit.setObjectName(u"exr_folder_path_lineEdit")
        self.exr_folder_path_lineEdit.setMinimumSize(QSize(669, 28))
        self.exr_folder_path_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(43, 43, 43);\n"
"}")
        self.exr_folder_path_lineEdit.setFrame(False)
        self.exr_folder_path_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.exr_folder_path_lineEdit)

        self.browse_exr_folder_pushButton = QPushButton(self.centralwidget)
        self.browse_exr_folder_pushButton.setObjectName(u"browse_exr_folder_pushButton")
        self.browse_exr_folder_pushButton.setMinimumSize(QSize(105, 0))
        self.browse_exr_folder_pushButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(6, 150, 215);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 118, 210);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.browse_exr_folder_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output_folder_path_lineEdit = QLineEdit(self.centralwidget)
        self.output_folder_path_lineEdit.setObjectName(u"output_folder_path_lineEdit")
        self.output_folder_path_lineEdit.setMinimumSize(QSize(669, 28))
        self.output_folder_path_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(43, 43, 43);\n"
"}")
        self.output_folder_path_lineEdit.setFrame(False)
        self.output_folder_path_lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.output_folder_path_lineEdit)

        self.browse_output_folder_pushButton = QPushButton(self.centralwidget)
        self.browse_output_folder_pushButton.setObjectName(u"browse_output_folder_pushButton")
        self.browse_output_folder_pushButton.setMinimumSize(QSize(105, 0))
        self.browse_output_folder_pushButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(6, 150, 215);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 118, 210);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.browse_output_folder_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.convert_pushButton = QPushButton(self.centralwidget)
        self.convert_pushButton.setObjectName(u"convert_pushButton")
        self.convert_pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(124, 179, 66);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(104, 159, 56);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.convert_pushButton, 2, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)

        Converter.setCentralWidget(self.centralwidget)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"EXR to MOV converter V1.0", None))
        self.browse_exr_folder_pushButton.setText(QCoreApplication.translate("Converter", u"EXR Folder", None))
        self.browse_output_folder_pushButton.setText(QCoreApplication.translate("Converter", u"Output Folder", None))
        self.convert_pushButton.setText(QCoreApplication.translate("Converter", u"Convert", None))
        self.progressBar.setFormat("")
    # retranslateUi

