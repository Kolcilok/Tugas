from PyQt5.QtWidgets import QWidget, QPushButton


class FormLain_h93(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle("Form Lain")
        self.tombol = QPushButton()
        self.tombol.setText("Tutup")
        self.tombol.move(50, 40)
        self.tombol.setParent(self)
        self.tombol.clicked.connect(self.tombolDiklik)

    def tombolDiklik(self):
        self.close()
