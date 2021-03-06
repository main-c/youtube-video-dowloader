# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Format_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 392)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 5)
        self.format_combox_2 = QtWidgets.QFontComboBox(Dialog)
        self.format_combox_2.setMaximumSize(QtCore.QSize(182, 25))
        self.format_combox_2.setObjectName("format_combox_2")
        self.gridLayout_2.addWidget(self.format_combox_2, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 6, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.splitter_2, 7, 4, 1, 1)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setScaledContents(False)
        self.title.setWordWrap(True)
        self.title.setIndent(-1)
        self.title.setOpenExternalLinks(True)
        self.title.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 4)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 5)
        self.duration = QtWidgets.QLabel(Dialog)
        self.duration.setObjectName("duration")
        self.gridLayout_2.addWidget(self.duration, 1, 1, 1, 1)
        self.extension_combox = QtWidgets.QFontComboBox(Dialog)
        self.extension_combox.setEditable(False)
        self.extension_combox.setObjectName("extension_combox")
        self.gridLayout_2.addWidget(self.extension_combox, 2, 3, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 647, 198))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.high_def_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button.setObjectName("high_def_button")
        self.gridLayout.addWidget(self.high_def_button, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        self.high_def_button_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button_2.setObjectName("high_def_button_2")
        self.gridLayout_4.addWidget(self.high_def_button_2, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 2, 1, 1)
        self.high_def_button_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button_3.setObjectName("high_def_button_3")
        self.gridLayout_5.addWidget(self.high_def_button_3, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 0, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 0, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 2, 1, 1)
        self.high_def_button_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button_4.setObjectName("high_def_button_4")
        self.gridLayout_6.addWidget(self.high_def_button_4, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem12, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 0, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem13, 0, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem14, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 0, 2, 1, 1)
        self.high_def_button_5 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button_5.setObjectName("high_def_button_5")
        self.gridLayout_7.addWidget(self.high_def_button_5, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem15, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_8.addWidget(self.label_19, 0, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem16, 0, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem17, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 0, 2, 1, 1)
        self.high_def_button_6 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.high_def_button_6.setObjectName("high_def_button_6")
        self.gridLayout_8.addWidget(self.high_def_button_6, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 4, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 6, 4, 1, 1)
        self.link = QtWidgets.QLabel(Dialog)
        self.link.setOpenExternalLinks(True)
        self.link.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.link.setObjectName("link")
        self.gridLayout_2.addWidget(self.link, 1, 2, 1, 2)
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setMaximumSize(QtCore.QSize(67, 61))
        self.image.setStyleSheet("background-image: url(\"jksqdbkjqsd\");")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../../../../../../.designer/backup/img/play(1).png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 0, 0, 2, 1)

        self.retranslateUi(Dialog)
        self.format_combox_2.currentTextChanged['QString'].connect(self.scrollArea.update)
        self.pushButton_2.clicked.connect(Dialog.exec)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.format_combox_2.setCurrentText(_translate("Dialog", "Ubuntu"))
        self.label_4.setText(_translate("Dialog", "Format :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Download"))
        self.title.setText(_translate("Dialog", "PyQt5 QTableWidget tutorial: Load data from SQL table into Table Widget [Python, SQLite, PyQT5]"))
        self.duration.setText(_translate("Dialog", "24:3"))
        self.label_5.setText(_translate("Dialog", "1084p"))
        self.label_7.setText(_translate("Dialog", "45.6 Mb"))
        self.high_def_button.setText(_translate("Dialog", "High Quality"))
        self.high_def_button_2.setText(_translate("Dialog", "Normal Quality"))
        self.label_9.setText(_translate("Dialog", "45.6 Mb"))
        self.label_8.setText(_translate("Dialog", "720p"))
        self.label_11.setText(_translate("Dialog", "480p"))
        self.high_def_button_3.setText(_translate("Dialog", "Normal Quality"))
        self.label_12.setText(_translate("Dialog", "45.6 Mb"))
        self.label_16.setText(_translate("Dialog", "45.6 Mb"))
        self.label_15.setText(_translate("Dialog", "360p"))
        self.high_def_button_4.setText(_translate("Dialog", "Low Resolution"))
        self.label_17.setText(_translate("Dialog", "45.6 Mb"))
        self.label_18.setText(_translate("Dialog", "240p"))
        self.high_def_button_5.setText(_translate("Dialog", "Low Resolution"))
        self.label_19.setText(_translate("Dialog", "45.6 Mb"))
        self.label_20.setText(_translate("Dialog", "144p"))
        self.high_def_button_6.setText(_translate("Dialog", "Low Resolution"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.link.setText(_translate("Dialog", "https://youtu.be/YySB6tkjZ7Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Format_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
