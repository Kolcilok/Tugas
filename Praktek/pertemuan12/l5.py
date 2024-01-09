
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class formSpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Praktikum 5: QListWidget @aku_bisa")
        self.label = QLabel("Nama Anda")
        self.lineEditNama = QLineEdit()
        self.listWidgetKiri = QListWidget()
        self.listWidgetKanan = QListWidget()
        self.pushButtonTambah = QPushButton("Tambah")
        self.pushButtonKanan = QPushButton(">")
        self.pushButtonKananS = QPushButton(">>")
        self.pushButtonKiri = QPushButton("<")
        self.pushButtonKiriS = QPushButton("<<")
        vbox = QVBoxLayout()
        vbox.addWidget(self.pushButtonTambah)
        vbox.addWidget(self.pushButtonKanan)
        vbox.addWidget(self.pushButtonKananS)
        vbox.addWidget(self.pushButtonKiri)
        vbox.addWidget(self.pushButtonKiriS)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lineEditNama)
        vbox2.addWidget(self.listWidgetKiri)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox2)

        hbox.addLayout(vbox)

        grid = QGridLayout()

        grid.addWidget(self.label, 0, 0, 1, 1)
        grid.addLayout(hbox, 1, 0, 1, 2)
        grid.addWidget(self.listWidgetKanan, 1, 2)
        self.setLayout(grid)
        self.pushButtonTambah.clicked.connect(self.tambahDiklik)
        self.pushButtonKanan.clicked.connect(self.kananDiklik)

        self.pushButtonKananS.clicked.connect(self.kananSDiklik)
        self.pushButtonKiri.clicked.connect(self.kiriDiklik)
        self.pushButtonKiriS.clicked.connect(self.kiriSDiklik)

    def tambahDiklik(self):
        if len(self.lineEditNama.text()) == 0:
            return
        item = self.lineEditNama.text()
        self.listWidgetKiri.addItem(item)
        self.lineEditNama.clear()
        self.lineEditNama.setFocus()

    def kananDiklik(self):
        if self.listWidgetKiri.currentRow() < 0:
            return
        self.listWidgetKanan.addItem(self.listWidgetKiri.currentItem().text())
        self.listWidgetKiri.takeItem(self.listWidgetKiri.currentRow())

    def kananSDiklik(self):
        for indeks in range(self.listWidgetKiri.count()):
            self.listWidgetKanan.addItem(
                self.listWidgetKiri.item(indeks).text())
        self.listWidgetKiri.clear()

    def kiriDiklik(self):
        if self.listWidgetKanan.currentRow() < 0:
            return
        self.listWidgetKiri.addItem(self.listWidgetKanan.currentItem().text())
        self.listWidgetKanan.takeItem(self.listWidgetKanan.currentRow())

    def kiriSDiklik(self):
        for indeks in range(self.listWidgetKanan.count()):
            self.listWidgetKiri.addItem(
                self.listWidgetKanan.item(indeks).text())
        self.listWidgetKanan.clear()


if __name__ == '__main__':
    app = QApplication([])
    form = formSpinBox()
    form.show()
    app.exec_()
