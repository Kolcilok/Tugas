from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QCheckBox, QFrame
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QCheckBox @aku_bisa")
        self.setGeometry(30, 100, 300, 150)
        self.label1 = QLabel(" <b> Demo QCheckBox</b>")
        self.label2 = QLabel("================================")
        self.labelSoal = QLabel("Syahadat ada dua, yaitu: ")
        self.checkBTauhid = QCheckBox()
        self.checkBShalat = QCheckBox()

        self.checkBTauhid.setText("Tauhid")

        self.checkBShalat.setText("Shalat")
        self.checkBRasul = QCheckBox()

        self.checkBRasul.setText("Rasul")

        self.checkBZakat = QCheckBox()

        self.checkBZakat.setText("Zakat")
        hbox = QHBoxLayout()
        hbox.addWidget(self.checkBTauhid)
        hbox.addWidget(self.checkBShalat)
        hbox.addWidget(self.checkBRasul)
        hbox.addWidget(self.checkBZakat)
        garisH = QFrame()
        garisH.setFrameShape(QFrame.HLine)
        garisH.setFrameShadow(QFrame.Sunken)
        self.pBOK = QPushButton("OK")
        self.pBOK.clicked.connect(self.OkDiklik)
        self.pBKeluar = QPushButton("Keluar")
        self.pBKeluar.clicked.connect(self.close)
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.pBOK)
        hbox2.addWidget(self.pBKeluar)
        lay = QVBoxLayout()
        lay.addWidget(self.label1)

        lay.addWidget(self.label2)
        lay.addWidget(self.labelSoal)
        lay.addLayout(hbox)
        lay.addWidget(garisH)

        lay.addLayout(hbox2)

        lay.addLayout(hbox2)
        self.setLayout(lay)

    def OkDiklik(self):
        pilihan = []
        if self.checkBTauhid.isChecked():
            pilihan.append("Tauhid")
        if self.checkBShalat.isChecked():
            pilihan.append("Shalat")
        if self.checkBRasul.isChecked():
            pilihan.append("Rasul")
        if self.checkBZakat.isChecked():
            pilihan.append("Zakat")
        if pilihan == ["Tauhid", "Rasul"]:

            QMessageBox.information(
                self, "Informasi @aku_bisa", repr(pilihan)+"\nAnda Benar")
        else:
            QMessageBox.information(
                self, "Informasi @aku_bisa", repr(pilihan)+"\nAnda Salah")


if __name__ == "__main__":

    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
