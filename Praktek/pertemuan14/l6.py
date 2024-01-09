import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 450)
        self.move(300, 300)
        self.setWindowTitle('Latihan QFileDialog.getSave FileName()@aku_bisa')
        self.textEdit = QTextEdit()
        self.saveButton = QPushButton('Simpan')
        self.fileLabel = QLabel('Nama file : ')
        hbox = QHBoxLayout()
        hbox.addWidget(self.saveButton)
        hbox.addStretch()
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(hbox)
        layout.addWidget(self.fileLabel)
        self.setLayout(layout)
        self.saveButton.clicked.connect(self.saveButtonClick)

    def saveButtonClick(self):
        import os
        fileName = QFileDialog.getSaveFileName(self,
                                               'Simpan file', os.curdir,
                                               'Python Code (*.py);; Ruby Code (*.rb)', '*.py')
        if not fileName[0]:
            return
        self.fileLabel.setText('Nama file: ' + fileName[0])
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIODevice.WriteOnly):
            return
        stream = QTextStream(fileHandle)
        stream << self.textEdit.document().toPlainText()
        stream.flush()
        fileHandle.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.setupUi()
    form.show()
    app.exec()
