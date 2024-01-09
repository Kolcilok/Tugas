from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 450)
        self.move(300, 300)
        self.textEdit = QTextEdit()
        self.fontButton = QPushButton()
        self.fontButton = QPushButton('Font')
        self.setWindowTitle('Latihan QFontDialog@aku_bisa')
        hbox = QHBoxLayout()
        hbox.addWidget(self.fontButton)
        hbox.addStretch()
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.fontButton.clicked.connect(self.fontButtonClick)

    def fontButtonClick(self):
        fontTuple = QFontDialog.getFont(
            QFont('Sans Serif', 11), self, 'Pilih font')
        if fontTuple[0]:
            self.textEdit.setCurrentFont(fontTuple[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()
