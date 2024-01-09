from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QLineEdit, QWidget, QGridLayout


class EntryFormPhonebook(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Tambah/ Ubah Kontak @aku_bisa")
        self.labelNama = QLabel("Nama Lengkap")
        self.labelHp = QLabel("Nomor Telephone")
        self.lineEditNama = QLineEdit()
        self.lineEditTelephone = QLineEdit()
        self.tombolOk = QPushButton("Ok")
        self.tombolBatal = QPushButton("Batal")

        layout = QGridLayout()
        layout.addWidget(self.labelNama, 0, 0)
        layout.addWidget(self.lineEditNama, 0, 1, 1, 2)
        layout.addWidget(self.labelHp, 1, 0)
        layout.addWidget(self.lineEditTelephone, 1, 1, 1, 2)
        layout.addWidget(self.tombolOk, 2, 1, 1, 1)
        layout.addWidget(self.tombolBatal, 2, 2, 1, 1)
        self.setLayout(layout)
        self.tombolOk.clicked.connect(self.accept)
        self.tombolBatal.clicked.connect(self.reject)


if __name__ == '__main__':
    app = QApplication([])
    form = EntryFormPhonebook()
    form.show()
    app.exec()
