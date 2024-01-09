from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


class FormLabel(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QRadioButt @aku_bisa")
        self. setGeometry(30, 100, 300, 150)
        self.label1 = QLabel(" <b> Demo QRadioButton untuk Kalkulator</b>")
        self.label2 = QLabel("============================================")
        self.labelB1 = QLabel("Bilangan Pertama")
        self. lineEditB1 = QLineEdit()
        self. labelB2 = QLabel("Bilangan Kedua")
        self.lineEditB2 = QLineEdit()
        grid = QGridLayout()
        grid. addWidget(self.labelB1, 0, 0)
        grid. addWidget(self.lineEditB1, 0, 1)
        grid. addWidget(self.labelB2, 1, 0)
        grid. addWidget(self.lineEditB2, 1, 1)
        self.rBTambah = QRadioButton("Tambah")
        self.rBKurang = QRadioButton("Kurang")
        self.rBKali = QRadioButton("Kali")
        self.rBBagi = QRadioButton("Bagi")
        hbox = QHBoxLayout()
        hbox.addWidget(self.rBTambah)
        hbox.addWidget(self.rBKurang)
        hbox.addWidget(self.rBKali)
        hbox.addWidget(self.rBBagi)

        self.labelHasil = QLabel("<b>Hasil perhitungan : </b>")
        self.pBHitung = QPushButton("Hitung")

        lay = QVBoxLayout()
        lay.addWidget(self.label1)
        lay.addWidget(self.label2)
        lay.addLayout(grid)
        lay.addLayout(hbox)
        lay.addWidget(self.labelHasil)
        lay.addWidget(self.pBHitung)
        self.setLayout(lay)

        self.rBKurang.clicked.connect(
            lambda: self.labelHasil.setText("<b>Hasil Pengurangan :</b>"))
        self.rBKali.clicked.connect(
            lambda: self.labelHasil.setText("<b>Hasil Perkalian :</b>"))
        self.rBBagi.clicked.connect(
            lambda: self.labelHasil.setText("<b>Hasil Pembagian :</b>"))
        self.pBHitung.clicked.connect(self.hitung)

    def hitung(self):
        a = float(self.lineEditB1.text())
        b = float(self.lineEditB2.text())
        if self.rBTambah.isChecked():
            c = a+b
        elif self.rBKurang.isChecked():
            c-a-b
        elif self.rBKali.isChecked():
            c = ab
        else:
            c = a/b

        index = str(self.labelHasil.text()).index(':')
        s = str(self.labelHasil.text())[:index+1]
        self.labelHasil.setText(f"{s} {c}")


if __name__ == "__main__":
    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
