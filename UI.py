# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 540)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(69, 206, 255)")
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.now_time_text = QtWidgets.QLineEdit(self.centralwidget)
        self.now_time_text.setGeometry(QtCore.QRect(710, 320, 330, 181))
        font = QtGui.QFont()
        font.setFamily("Digital-7 Mono")
        font.setPointSize(86)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.now_time_text.setFont(font)
        self.now_time_text.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.now_time_text.setMouseTracking(True)
        self.now_time_text.setAutoFillBackground(False)
        self.now_time_text.setStyleSheet("background-color:rgb(152, 152, 152)")
        self.now_time_text.setFrame(False)
        self.now_time_text.setAlignment(QtCore.Qt.AlignCenter)
        self.now_time_text.setReadOnly(True)
        self.now_time_text.setClearButtonEnabled(False)
        self.now_time_text.setObjectName("now_time_text")
        self.view = QtWidgets.QLabel(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(30, 30, 640, 480))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.view.setFont(font)
        self.view.setFrameShape(QtWidgets.QFrame.Box)
        self.view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.view.setScaledContents(False)
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setObjectName("view")
        self.set_time_Button = QtWidgets.QPushButton(self.centralwidget)
        self.set_time_Button.setEnabled(True)
        self.set_time_Button.setGeometry(QtCore.QRect(700, 240, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.set_time_Button.setFont(font)
        self.set_time_Button.setStyleSheet("background-color:rgb(170, 170, 255);")
        self.set_time_Button.setAutoRepeat(False)
        self.set_time_Button.setAutoExclusive(False)
        self.set_time_Button.setObjectName("set_time_Button")
        self.history = QtWidgets.QLineEdit(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(708, 39, 334, 64))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(14)
        self.history.setFont(font)
        self.history.setStyleSheet("background-color:rgb(152, 152, 152)")
        self.history.setFrame(False)
        self.history.setObjectName("history")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(840, 175, 211, 55))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color:rgb(170, 170, 255);")
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 309, 350, 201))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.history_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.history_2.setGeometry(QtCore.QRect(700, 120, 141, 55))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(18)
        self.history_2.setFont(font)
        self.history_2.setStyleSheet("")
        self.history_2.setFrame(False)
        self.history_2.setObjectName("history_2")
        self.history_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.history_3.setGeometry(QtCore.QRect(700, 175, 141, 55))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(18)
        self.history_3.setFont(font)
        self.history_3.setStyleSheet("")
        self.history_3.setFrame(False)
        self.history_3.setObjectName("history_3")
        self.set_time_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.set_time_Button_2.setEnabled(True)
        self.set_time_Button_2.setGeometry(QtCore.QRect(879, 240, 171, 60))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.set_time_Button_2.setFont(font)
        self.set_time_Button_2.setStyleSheet("background-color:rgb(170, 170, 255);")
        self.set_time_Button_2.setAutoRepeat(False)
        self.set_time_Button_2.setAutoExclusive(False)
        self.set_time_Button_2.setObjectName("set_time_Button_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 30, 351, 81))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.TimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.TimeEdit.setGeometry(QtCore.QRect(840, 120, 211, 55))
        font = QtGui.QFont()
        font.setFamily("Taipei Sans TC Beta")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TimeEdit.setFont(font)
        self.TimeEdit.setStyleSheet("background-color:rgb(170, 170, 255);")
        self.TimeEdit.setFrame(False)
        self.TimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeEdit.setMinimumDate(QtCore.QDate(2022, 7, 18))
        self.TimeEdit.setObjectName("TimeEdit")
        self.label_2.raise_()
        self.label.raise_()
        self.now_time_text.raise_()
        self.view.raise_()
        self.set_time_Button.raise_()
        self.history.raise_()
        self.spinBox.raise_()
        self.history_2.raise_()
        self.history_3.raise_()
        self.set_time_Button_2.raise_()
        self.TimeEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.now_time_text.setText(_translate("MainWindow", "08:00"))
        self.view.setText(_translate("MainWindow", "Camera"))
        self.set_time_Button.setText(_translate("MainWindow", "新增鬧鐘"))
        self.history.setText(_translate("MainWindow", "Show messege here"))
        self.history_2.setText(_translate("MainWindow", "響鈴時間："))
        self.history_3.setText(_translate("MainWindow", "響鈴時長："))
        self.set_time_Button_2.setText(_translate("MainWindow", "查詢當日紀錄"))
        self.TimeEdit.setDisplayFormat(_translate("MainWindow", "M/d hh:mm"))
