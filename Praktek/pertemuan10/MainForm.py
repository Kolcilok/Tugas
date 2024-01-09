from PyQt5.QtWidgets import QGridLayout, QPushButton, QLineEdit, QWidget, QApplication, QLabel, QListWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog
from EntryFormPhonebook import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo Buku Telephone @Aku bisa")
        self.move(50, 50)

        self.listKontak = QListWidget()
        self.tombolTambah = QPushButton("Tambah")
        self.tombolHapus = QPushButton("Hapus")
        self.tombolUbah = QPushButton("Ubah")
        self.tombolKosongkan = QPushButton("Kosongkan")
        self.tombolKeluar = QPushButton("Keluar")

        box = QHBoxLayout()
        box.addWidget(self.tombolTambah)
        box.addWidget(self.tombolHapus)
        box.addWidget(self.tombolUbah)
        box.addWidget(self.tombolKosongkan)
        box.addWidget(self.tombolKeluar)

        vBox = QVBoxLayout()
        vBox.addWidget(self.listKontak)
        vBox.addLayout(box)

        layout = QVBoxLayout()
        layout.addLayout(vBox)

        self.setLayout(layout)
        self.tombolTambah.clicked.connect(self.tombolTambahDiklik)
        self.tombolUbah.clicked.connect(self.tombolUbahDiklik)
        self.tombolHapus.clicked.connect(self.tombolHapusDiklik)
        self.tombolKosongkan.clicked.connect(self.listKontak.clear)
        self.tombolKeluar.clicked.connect(self.close)

    def tombolTambahDiklik(self):
        self.EntryForm = EntryFormPhonebook()
        if self.EntryForm.exec() == QDialog.accepted:
            self.listKontak.addItem(
                self.EntryForm.lineEditNama.text()+' - '+self.EntryForm.lineEditTelephone.text()
            )

    def tombolUbahDiklik(self):
        if self.listKontak.currentRow() < 0:
            return
        self.EntryForm = EntryFormPhonebook()
        s = str(self.listKontak.currentItem().text())
        idx = s.index('-')
        self.EntryForm.lineEditNama.setText(s[:(idx-1)])
        self.EntryForm.lineEditTelephone.setText(s[:(idx-1)])

        if self.EntryForm.exec() == QDialog.accepted:
            self.listKontak.currentItem().setText(
                self.EntryForm.lineEditName.text()+' - '+self.EntryForm.lineEditTelephone.text()
            )

    def tombolHapusDiklik(self):
        row = self.listKontak.currentRow()
        if row >= 0:
            self.listKontak.takeItem(row)


if __name__ == '__main__':
    app = QApplication([])
    form = MainForm()
    form.show()
    app.exec()
