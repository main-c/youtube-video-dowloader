# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/main-c/Documents/Projets/PythonProjects/youtube-video-downloader/format_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 392)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 5)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setScaledContents(False)
        self.title.setWordWrap(True)
        self.title.setIndent(-1)
        self.title.setOpenExternalLinks(True)
        self.title.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 4)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 6, 0, 1, 4)
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setMaximumSize(QtCore.QSize(67, 61))
        self.image.setStyleSheet("background-image: url(\"https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2F6%2F66%2FUnited_Nations_Decade_of_Education_for_Sustainable_Development.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FUnited_Nations_Decade_of_Education_for_Sustainable_Development&tbnid=RiL8O0nQbd6fFM&vet=12ahUKEwj39Jj5q4L1AhXkhP0HHfAwDaoQMygAegUIARCcAQ..i&docid=_mcW-yUb_lYy0M&w=200&h=200&q=desd&client=ubuntu&ved=2ahUKEwj39Jj5q4L1AhXkhP0HHfAwDaoQMygAegUIARCcAQ\");")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("/home/main-c/Documents/Projets/PythonProjects/youtube-video-downloader/img/play(1).png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 0, 0, 2, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 5)
        self.link = QtWidgets.QLabel(Dialog)
        self.link.setOpenExternalLinks(True)
        self.link.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.link.setObjectName("link")
        self.gridLayout_2.addWidget(self.link, 1, 2, 1, 2)
        self.format_combox_2 = QtWidgets.QFontComboBox(Dialog)
        self.format_combox_2.setMaximumSize(QtCore.QSize(182, 25))
        self.format_combox_2.setEditable(False)
        self.format_combox_2.setMaxVisibleItems(2)
        self.format_combox_2.setMaxCount(2)
        self.format_combox_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
