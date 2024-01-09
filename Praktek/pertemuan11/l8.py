from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QCombobox @aku_bisa")
        self.setGeometry(30, 100, 300, 150)
        self.label1 = QLabel("<b> Demo QComboBox</b>")
        self.label2 = QLabel("===========================")
        self.comboB = QComboBox()

        for i in range(1, 11):
            self.comboB.addItem(f"pilihan ke-{i}")

        self.pBAmbilTeks = QPushButton("Ambl Teks")
        self.pBAmbilTeks.clicked.connect(self.AmbilTeksDiklik)
        lay = QHBoxLayout()
        lay.addWidget(self.comboB)
        lay.addWidget(self.pBAmbilTeks)
        self.setLayout(lay)

    def AmbilTeksDiklik(self):
        QMessageBox.information(
            self, "Informasi @aku bisa", "<b>Anda Memilih:</b>"+self.comboB.currentText())


if __name__ == '__main__':
    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
