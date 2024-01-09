from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Formku(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo Akses File dengan kelas QFile @aku bisa")
        self.labelJudul = QLabel("Akses File dengan QFile @aku_bisa")
        self.labelNamaFile = QLabel("Nama File")
        self.lineEditNamaFile = QLineEdit()
        self.labelDADitulis = QLabel("Data yang akan ditulis")
        self.textEditDADitulis = QTextEdit()
        self.labelDDibaca = QLabel("Data yang dibaca")
        self.textEditDDibaca = QTextEdit()
        self.textEditDDibaca.setReadOnly(True)
        self.labelKosong = QLabel("")
        self.pushButtonTulisD = QPushButton("Tulis Data")
        self.pushButtonBacaD = QPushButton("Baca Data")
        self.pushButtonBacaD.setDisabled(True)
        lay = QGridLayout()
        lay.addWidget(self.labelJudul, 0, 0, 1, 3)
        lay.addWidget(self.labelNamaFile, 1, 0, 1, 3)
        lay.addWidget(self.lineEditNamaFile, 2, 0, 1, 3)
        lay.addWidget(self.labelDADitulis, 3, 0, 1, 3)
        lay.addWidget(self.textEditDADitulis, 4, 0, 1, 3)
        lay.addWidget(self.labelDDibaca, 5, 0, 1, 3)
        lay.addWidget(self.textEditDDibaca, 6, 0, 1, 3)
        lay.addWidget(self.labelKosong, 7, 0, 1, 1)
        lay.addWidget(self.pushButtonTulisD, 7, 1, 1, 1)
        lay.addWidget(self.pushButtonBacaD, 7, 2, 1, 1)
        self.setLayout(lay)
        self.pushButtonTulisD.clicked.connect(self.pBTulisDataDiklik)
        self.pushButtonBacaD.clicked.connect(self.pBBacaDataDiklik)

    def pBTulisDataDiklik(self):
        if len(self.lineEditNamaFile.text().strip()) == 0:
            QMessageBox.critical(self, 'Pesan Kesalahan',
                                 'Nama file harus diisi')
            return
        if self.textEditDADitulis.document().isEmpty():
            QMessageBox.critical(seif, 'Pesan Kesalahan',
                                 'Data yang akan ditulis harus diisi!')
            return
        # menggunakan QFile
        f = QFile(self.lineEditNamaFile.text())
        if not f.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        inputStream = QTextStream(f)
        inputStream << self.textEditDADitulis.document().toPlainText()
        f.close()
        self.lineEditNamaFile.setDisabled(True)

        self.textEditDADitulis.setDisabled(True)

        self.pushButtonTulisD.setDisabled(True)

        self.pushButtonBacaD.setDisabled(False)

    def pBBacaDataDiklik(self):
        f = QFile(self.lineEditNamaFile.text())
        if not f.open(QIODevice. ReadOnly | QIODevice.Text):
            return
        self.textEditDDibaca.document().setPlainText(
            ''.join(f.readAll()))
        f.close()


if __name__ == "__main__":
    app = QApplication([])
    form = Formku()
    form.setupUi()
    form.show()
    app.exec_()
