from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QFrame
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo Qlabel,QlineEdit dai")
        self.setGeometry(30, 100, 500, 200)
        self.labelBilangan1 = QLabel("Masukka Bilangan pertama")
        self.lineEditB1 = QLineEdit()
        self.labelBilangan2 = QLabel("massukkan Bilangan kedua")
        self.lineEditB2 = QLineEdit()
        self.labelHasilPerhitungan = QLabel("Hasil perhitungan")
        self.lineEditHP = QLineEdit()
        vboxKiri = QVBoxLayout()
        vboxKiri.addWidget(self.labelBilangan1)
        vboxKiri.addWidget(self.lineEditB1)
        vboxKiri.addWidget(self.labelBilangan2)
        vboxKiri.addWidget(self.lineEditB2)
        vboxKiri.addWidget(self.labelHasilPerhitungan)
        vboxKiri.addWidget(self.lineEditHP)
        garisV = QFrame()
        garisV.setFrameShadow(QFrame.Sunken)
        garisV.setFrameShape(QFrame.VLine)
        self.pushButtonTambah = QPushButton("&Tambah")
        self.pushButtonKurang = QPushButton("&Kurang")
        self.pushButtonKali = QPushButton("&Kali")
        self.pushButtonBagi = QPushButton("&Bagi")
        self.pushButtonTambah.clicked.connect(self.fungsiTambah)
        self.pushButtonKurang.clicked.connect(self.fungsiKurang)
        self.pushButtonKali.clicked.connect(self.fungsiKali)
        self.pushButtonBagi.clicked.connect(self.fungsiBagi)
        vboxKanan = QVBoxLayout()
        vboxKanan.addWidget(self.pushButtonTambah)
        vboxKanan.addWidget(self.pushButtonKurang)
        vboxKanan.addWidget(self.pushButtonKali)
        vboxKanan.addWidget(self.pushButtonBagi)
        layout = QHBoxLayout()
        layout.addLayout(vboxKiri)
        layout. addWidget(garisV)
        layout. addLayout(vboxKanan)
        self.setLayout(layout)

    def hitung(self, operator):
        b1 = int(self.lineEditB1.text())
        b2 = int(self.lineEditB2.text())
        if (operator == '+'):
            h = b1+b2
        elif (operator == '-'):
            h = b1 - b2
        elif (operator == '*'):
            h = b1 * b2
        else:
            h = b1/b2

        self.lineEditHP.setText(str(h))

    def fungsiTambah(self):
        self.hitung('+')

    def fungsiKurang(self):
        self.hitung('-')

    def fungsiKali(self):
        self.hitung('*')

    def fungsiBagi(self):
        self.hitung('/')


if __name__ == '__main__':
    app = QApplication([])
    Form = FormLabel()
    Form.show()
    app.exec_()
