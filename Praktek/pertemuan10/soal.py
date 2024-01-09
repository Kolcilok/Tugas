from PyQt5.QtWidgets import QGridLayout, QPushButton, QLineEdit, QWidget, QApplication, QLabel, QListWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo Buku Telephone @Aku bisa")
        self.move(50, 50)

        self.listKontak = QListWidget()
        self.tombol1 = QPushButton("tombol1")
        self.tombol2 = QPushButton("tombol2")
        self.tombol3 = QPushButton("tombol3")
        self.tombol4 = QPushButton("tombol4")
        self.tombol5 = QPushButton("tombol5")
        self.tombol6 = QPushButton("tombol6")
        self.tombol7 = QPushButton("tombol7")
        self.tombol8 = QPushButton("tombol8")
        self.labelNama = QLabel("Nama")
        self.labelAlamat = QLabel("Alamat")
        self.labelTelephone = QLabel("Telephone")
        self.Nama = QLineEdit()
        self.Alamat = QLineEdit()
        self.Telephone = QLineEdit()

        box = QGridLayout()
        box.addWidget(self.tombol1, 0, 0)
        box.addWidget(self.tombol2, 0, 1)
        box.addWidget(self.tombol3, 0, 2)
        box.addWidget(self.tombol4, 0, 3)
        box.addWidget(self.tombol5, 0, 4)
        box.addWidget(self.tombol6, 1, 0)
        box.addWidget(self.tombol7, 1, 1)

        box.addWidget(self.tombol8, 2, 0, 2, 2)

        box.addWidget(self.labelNama, 1, 2)
        box.addWidget(self.Nama, 1, 3, 1, 2)

        box.addWidget(self.labelAlamat, 2, 2)
        box.addWidget(self.Alamat, 2, 3, 1, 2)
        box.addWidget(self.labelTelephone, 3, 2)
        box.addWidget(self.Telephone, 3, 3, 3, 2)

        vBox = QVBoxLayout()
        vBox.addLayout(box)

        layout = QVBoxLayout()
        layout.addLayout(vBox)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    form = MainForm()
    form.show()
    app.exec()
