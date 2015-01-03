__author__ = '7sDream'

import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow
from noteUtils import NoteUtils
from os import path


class Win(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.pianoKeyboard.setPixmap(QtGui.QPixmap('./pianoBoard.bmp'))
        self.ui.pianoKeyboard.mousePressEvent = self.piano_keyboard_clicked

        # noinspection PyUnresolvedReferences
        self.ui.sliderNoteLength.valueChanged.connect(self.slider_changed)
        QtCore.QObject.connect(self.ui.btnAddEmptyNote,
                               QtCore.SIGNAL("clicked()"),
                               self.add_empty_note)
        QtCore.QObject.connect(self.ui.btnPlay,
                               QtCore.SIGNAL("clicked()"),
                               self.play_notes)
        QtCore.QObject.connect(self.ui.btnLoad,
                               QtCore.SIGNAL("clicked()"),
                               self.load_file)
        QtCore.QObject.connect(self.ui.btnSave,
                               QtCore.SIGNAL("clicked()"),
                               self.save_file)

    def piano_keyboard_clicked(self, event):
        text = utils.pos_2_text_and_play(event.x(), event.y(),
                                         self.ui.sliderNoteLength.value())
        self.add_note(text)

    def slider_changed(self, new_value):
        if new_value == 0:
            self.ui.labSecond.setText('1/2 秒')
        elif new_value == 1:
            self.ui.labSecond.setText('1/4 秒')
        elif new_value == 2:
            self.ui.labSecond.setText('1/8 秒')

    def add_empty_note(self):
        self.add_note(utils.get_empty_note_text_by_length(
            self.ui.sliderNoteLength.value()
        ))

    def add_note(self, text):
        if self.ui.btnRecord.isChecked():
            origintext = self.ui.teRecord.toPlainText()
            self.ui.teRecord.insertPlainText(text if origintext == '' else
                                             ',' + text)

    def play_notes(self):
        utils.play_note_texts(self.ui.teRecord.toPlainText())

    def load_file(self):
        filedialog = QtGui.QFileDialog()
        filepath = filedialog.getOpenFileName(self, '载入文件',
                                              path.split(
                                                  path.realpath(__file__))[0],
                                              'text (*.txt)')
        if path.isfile(filepath):
            f = open(filepath, mode='r')
            with f:
                self.ui.teRecord.setPlainText(f.read())
            f.close()

    def save_file(self):
        filedialog = QtGui.QFileDialog()
        filepath = filedialog.getSaveFileName(self, '保存文件',
                                              path.split(
                                                  path.realpath(__file__))[0],
                                              'text (*.txt)')
        if filepath != '':
            f = open(filepath, mode='w')
            with f:
                f.write(self.ui.teRecord.toPlainText())
            f.close()

        messagebox = QtGui.QMessageBox(self)
        messagebox.setText('保存成功')
        messagebox.addButton('确认', QtGui.QMessageBox.AcceptRole)
        messagebox.show()

if __name__ == '__main__':
    utils = NoteUtils()
    App = QtGui.QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(App.exec())