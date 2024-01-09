from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget


class MainForm_h97(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Tampilan QVBoxLayout")
        self.move(300, 300)
        self.resize(500, 100)

        self.tombol1 = QPushButton("Tombol 1")
        self.tombol2 = QPushButton("Tombol 2")
        self.tombol3 = QPushButton("Tombol 3")
        self.tombol4 = QPushButton("Tombol 4")
        layout = QVBoxLayout()
        layout.addWidget(self.tombol1)
        layout.addWidget(self.tombol2)
        layout.addWidget(self.tombol3)
        layout.addWidget(self.tombol4)
        self.setLayout(layout)
