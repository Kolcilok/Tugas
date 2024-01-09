from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fromku(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo Akses File dengan fungsi Open() @aku_bisa")
        self.labelJudul = QLabel("Akses File dengan fungsi python open()")
        self.labelNamaFile = QLabel("Nama File")
        self.lineEditNamaFile = QLineEdit()
        self.labelDADitulis = QLabel("Data yang akan ditulis")
        self.textEditDADitulis = QTextEdit()
        self.labelDDibaca = QLabel("Data yang dibaca")
        self.textEditDDibaca = QTextEdit()
        self.textEditDDibaca.setReadOnly(True)
        self.labelKosong = QLabel("")
        self.pushButtonTulisD = QPushButton("Tulis Data")
        self.pushButtonTulisD.clicked.connect(self.tulisDataDiklik)
        self.pushButtonBacaD = QPushButton("Baca Data")
        self.pushButtonBacaD.setDisabled(True)
        self.pushButtonBacaD.clicked.connect(self.bacaDataDiklik)

        lay = QGridLayout()
        lay.addWidget(self.lineEditNamaFile, 2, 0, 1, 3)
        lay.addWidget(self.labelDADitulis, 3, 0, 1, 3)
        lay.addWidget(self.textEditDADitulis, 4, 0, 1, 3)
        lay.addWidget(self.labelJudul, 0, 0, 1, 3)
        lay.addWidget(self.labelNamaFile, 1, 0, 1, 3)
        lay.addWidget(self.labelDDibaca, 5, 0, 1, 3)
        lay.addWidget(self.textEditDDibaca, 6, 0, 1, 3)
        lay.addWidget(self.labelKosong, 7, 0, 1, 1)
        lay.addWidget(self.pushButtonTulisD, 7, 1, 1, 1)
        lay.addWidget(self.pushButtonBacaD, 7, 2, 1, 1)
        self.setLayout(lay)

    def tulisDataDiklik(self):
        if len(self.lineEditNamaFile.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama file harus diisi')
            return
        if self.textEditDADitulis.document().isEmpty():
            QMessageBox.critical(
                self, 'Kesalahan', 'Data yang akan ditulis harus diisi!')
            return
        f = open(self.lineEditNamaFile.text(), 'w')
        f.writelines(self.textEditDADitulis.document().toPlainText())
        f.close()
        self.lineEditNamaFile.setDisabled(True)
        self.textEditDADitulis.setDisabled(True)
        self.pushButtonBacaD.setDisabled(False)

    def bacaDataDiklik(self):
        f = open(self.lineEditNamaFile.text(), 'r')
        self.textEditDDibaca.document().setPlainText(
            ''.join(f.readlines()))
        f.close()


if __name__ == "__main__":
    app = QApplication([])
    form = Fromku()
    form.setupUi()
    form.show()
    app.exec()
