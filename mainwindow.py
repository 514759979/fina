# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.choose_ptn = QtWidgets.QPushButton(self.centralWidget)
        self.choose_ptn.setGeometry(QtCore.QRect(0, 106, 113, 32))
        self.choose_ptn.setObjectName("choose_ptn")
        self.label_info = QtWidgets.QLabel(self.centralWidget)
        self.label_info.setGeometry(QtCore.QRect(120, 80, 131, 21))
        self.label_info.setObjectName("label_info")
        self.title = QtWidgets.QLabel(self.centralWidget)
        self.title.setGeometry(QtCore.QRect(60, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.start_ptn = QtWidgets.QPushButton(self.centralWidget)
        self.start_ptn.setGeometry(QtCore.QRect(130, 210, 113, 32))
        self.start_ptn.setObjectName("start_ptn")
        self.input_file_path = QtWidgets.QLineEdit(self.centralWidget)
        self.input_file_path.setEnabled(False)
        self.input_file_path.setGeometry(QtCore.QRect(120, 110, 141, 21))
        self.input_file_path.setObjectName("input_file_path")
        self.input_index = QtWidgets.QLineEdit(self.centralWidget)
        self.input_index.setGeometry(QtCore.QRect(120, 140, 141, 21))
        self.input_index.setObjectName("input_index")
        self.imput_col = QtWidgets.QLineEdit(self.centralWidget)
        self.imput_col.setGeometry(QtCore.QRect(120, 170, 141, 21))
        self.imput_col.setObjectName("imput_col")
        self.sheet_index = QtWidgets.QLabel(self.centralWidget)
        self.sheet_index.setGeometry(QtCore.QRect(11, 141, 91, 20))
        self.sheet_index.setObjectName("sheet_index")
        self.column = QtWidgets.QLabel(self.centralWidget)
        self.column.setGeometry(QtCore.QRect(10, 172, 111, 16))
        self.column.setObjectName("column")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 365, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_ptn.setText(_translate("MainWindow", "浏览"))
        self.label_info.setText(_translate("MainWindow", "选择需要过滤的文件"))
        self.title.setText(_translate("MainWindow", "过滤器-南丁格尔出品"))
        self.start_ptn.setText(_translate("MainWindow", "开始"))
        self.sheet_index.setText(_translate("MainWindow", "处理第几张表："))
        self.column.setText(_translate("MainWindow", "处理第几列数据："))

