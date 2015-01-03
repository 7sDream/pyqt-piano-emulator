# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano_emulator.ui'
#
# Created: Sat Jan  3 12:57:27 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(377, 301)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gvPianoBoard = QtGui.QGraphicsView(self.centralwidget)
        self.gvPianoBoard.setGeometry(QtCore.QRect(10, 10, 357, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.gvPianoBoard.setFont(font)
        self.gvPianoBoard.setObjectName(_fromUtf8("gvPianoBoard"))
        self.sliderNoteLength = QtGui.QSlider(self.centralwidget)
        self.sliderNoteLength.setGeometry(QtCore.QRect(70, 120, 81, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.sliderNoteLength.setFont(font)
        self.sliderNoteLength.setMinimum(1)
        self.sliderNoteLength.setMaximum(3)
        self.sliderNoteLength.setPageStep(1)
        self.sliderNoteLength.setOrientation(QtCore.Qt.Horizontal)
        self.sliderNoteLength.setObjectName(_fromUtf8("sliderNoteLength"))
        self.btnAddEmptyNote = QtGui.QPushButton(self.centralwidget)
        self.btnAddEmptyNote.setGeometry(QtCore.QRect(210, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnAddEmptyNote.setFont(font)
        self.btnAddEmptyNote.setObjectName(_fromUtf8("btnAddEmptyNote"))
        self.btnRecord = QtGui.QPushButton(self.centralwidget)
        self.btnRecord.setGeometry(QtCore.QRect(290, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnRecord.setFont(font)
        self.btnRecord.setCheckable(True)
        self.btnRecord.setObjectName(_fromUtf8("btnRecord"))
        self.labSecond = QtGui.QLabel(self.centralwidget)
        self.labSecond.setGeometry(QtCore.QRect(160, 120, 46, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.labSecond.setFont(font)
        self.labSecond.setObjectName(_fromUtf8("labSecond"))
        self.libNoteLength = QtGui.QLabel(self.centralwidget)
        self.libNoteLength.setGeometry(QtCore.QRect(10, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.libNoteLength.setFont(font)
        self.libNoteLength.setObjectName(_fromUtf8("libNoteLength"))
        self.tecRecord = QtGui.QTextEdit(self.centralwidget)
        self.tecRecord.setGeometry(QtCore.QRect(10, 150, 357, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.tecRecord.setFont(font)
        self.tecRecord.setObjectName(_fromUtf8("tecRecord"))
        self.btnLoad = QtGui.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(10, 270, 51, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnLoad.setFont(font)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(70, 270, 51, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(250, 270, 51, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.btnPlay = QtGui.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(310, 270, 51, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.btnPlay.setFont(font)
        self.btnPlay.setObjectName(_fromUtf8("btnPlay"))
        self.leKeyboardPlay = QtGui.QLineEdit(self.centralwidget)
        self.leKeyboardPlay.setGeometry(QtCore.QRect(130, 270, 113, 20))
        self.leKeyboardPlay.setObjectName(_fromUtf8("leKeyboardPlay"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leKeyboardPlay.clear)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tecRecord.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PianoEmulator", None))
        self.btnAddEmptyNote.setText(_translate("MainWindow", "插入空音符", None))
        self.btnRecord.setText(_translate("MainWindow", "录制", None))
        self.labSecond.setText(_translate("MainWindow", "1/2 秒", None))
        self.libNoteLength.setText(_translate("MainWindow", "音符长度", None))
        self.btnLoad.setText(_translate("MainWindow", "载入", None))
        self.btnSave.setText(_translate("MainWindow", "保存", None))
        self.btnClear.setText(_translate("MainWindow", "清空", None))
        self.btnPlay.setText(_translate("MainWindow", "播放", None))

