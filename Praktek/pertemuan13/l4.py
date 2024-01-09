from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Formku(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo Ubah Nama File dengan kelas QFile @aku_bisa")
        self.labelJudul = QLabel("Ubah Nama File dengan QFile @aku_bisa")
        self.labelNFLama = QLabel("Nama file lama")
        self.lineEditNFLama = QLineEdit()
        self.labelNFBaru = QLabel("Nama file baru")
        self.lineEditNFBaru = QLineEdit()
        self.labelKosong = QLabel("")
        self.pushButtonUbahNama = QPushButton("Ubah Nama")

        lay = QGridLayout()

        lay.addWidget(self.labelJudul, 0, 0, 1, 2)

        lay.addWidget(self.labelNFLama, 1, 0)

        lay.addWidget(self.lineEditNFLama, 1, 1)
        lay.addWidget(self.labelNFBaru, 2, 0)
        lay.addWidget(self.lineEditNFBaru, 2, 1)
        lay.addWidget(self.labelKosong, 3, 0)
        lay.addWidget(self.pushButtonUbahNama, 3, 1)
        self.setLayout(lay)
        self.pushButtonUbahNama.clicked.connect(self.pushButtonUbahNamaDiklik)

    def pushButtonUbahNamaDiklik(self):
        if len(self.lineEditNFBaru.text().strip()) == 0 | len(self.lineEditNFLama.text().strip()) == 0:
            QMessageBox.critical(self, 'Pesan Kesalahan',
                                 "Nama file baru dan file lama harus diisi!")
            return
        if not QFile.exists(self.lineEditNFLama.text()):
            return
        fileLama = self.lineEditNFLama.text()
        fileBaru = self.lineEditNFBaru.text()
        if QFile.copy(fileLama, fileBaru):
            QMessageBox.information(self, "informasi",
                                    f"Nama file {fileLama} telah diganti menjadi {fileBaru}")
        else:
            QMessageBox.information(self, "informasi",
                                    f"perubahab nama gagal")


if __name__ == "__main__":
    app = QApplication([])
    form = Formku()
    form.setupUi()
    form.show()
    app.exec()
