from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Formku (QWidget):

    def setupUi(self):
        self.setWindowTitle("Demo Menghapus File dengan kelas QFile @aku_bisa")
        self.labelJudul = QLabel("Menghapus File dengan QFile @aku_bisa")
        self.labelFDihapus = QLabel("Nama file yang akan dihapus")
        self.lineEditFDihapus = QLineEdit()
        self.labelKosong = QLabel("")
        self.pushButtonHapusFile = QPushButton("Hapus File")
        lay = QGridLayout()
        lay.addWidget(self.labelJudul, 0, 0, 1, 2)
        lay.addWidget(self.labelFDihapus, 1, 0)
        lay.addWidget(self.lineEditFDihapus, 1, 1)
        lay.addWidget(self.labelKosong, 3, 0)
        lay.addWidget(self.pushButtonHapusFile, 3, 1)
        self.setLayout(lay)
        self.pushButtonHapusFile.clicked.connect(
            self.pushButtonHapusFileDiklik)

    def pushButtonHapusFileDiklik(self):
        if len(self.lineEditFDihapus.text().strip()) == 0:
            QMessageBox.critical(self, 'Pesan Kesalahan',
                                 "Nama file yang akan diharus d")
            return
        if not QFile.exists(self.lineEditFDihapus.text()):
            return
        fileDihapus = self.lineEditFDihapus.text()
        if QFile.remove(fileDihapus):
            QMessageBox.information(self, "informasi",
                                    f"Nama file {fileDihapus} telah dihapus")
        else:
            QMessageBox.information(self, "informasi", f"Nama file {
                                    fileDihapus} gagal dihapus!")


if __name__ == "__main__":
    app = QApplication([])
    form = Formku()
    form.setupUi()
    form.show()
    app.exec()
