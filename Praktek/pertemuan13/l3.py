from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FormKu(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo Menyalin File dengan kelas QFile @aku_bisa")
        self.labelJudul = QLabel("Menyalin File dengan QFile @aku_bisa")
        self.labelFSumber = QLabel("Nama file sumber")
        self.lineEditFSumber = QLineEdit()
        self.labelFTujuan = QLabel("Nama file tujuan")
        self.lineEditFTujuan = QLineEdit()
        self.labelKosong = QLabel("")
        self.pushButtonSalinFile = QPushButton("Salin File")
        lay = QGridLayout()
        lay.addWidget(self.labelJudul, 0, 0, 1, 2)
        lay.addWidget(self.labelFSumber, 1, 0)
        lay.addWidget(self.lineEditFSumber, 1, 1)
        lay.addWidget(self.labelFTujuan, 2, 0)
        lay.addWidget(self.lineEditFTujuan, 2, 1)
        lay.addWidget(self.labelKosong, 3, 0)
        lay.addWidget(self.pushButtonSalinFile, 3, 1)
        self.setLayout(lay)
        self.pushButtonSalinFile.clicked.connect(
            self.pushButtonSalinFileDiklik)

    def pushButtonSalinFileDiklik(self):
        if len(self.lineEditFSumber.text().strip()) == 0 | len(self.lineEditFTujuan.text().strip()) == 0:
            QMessageBox.critical(self, 'Pesan Kesalahan',
                                 "Nama file sumber dan tujuan harus diisi!")
            return
        if not QFile.exists(self.lineEditFSumber.text()):
            return
        fileSumber = self.lineEditFSumber.text()
        fileTujuan = self.lineEditFTujuan.text()
        if QFile.copy(fileSumber, fileTujuan):
            QMessageBox.information(self, "informasi", f"Nama file {
                                    fileSumber} telah disalin")
        else:
            QMessageBox.information(self, "informasi", f"Nama file {
                                    fileSumber} gagal disalin!")


if __name__ == "__main__":
    app = QApplication([])
    form = FormKu()
    form.setupUi()
    form.show()
    app.exec()
