from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget


class MainForm_h103(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Tampilan QGridLayout")
        self.move(300, 300)
        self.resize(500, 100)

        self.tombol1 = QPushButton("Tombol 1")
        self.tombol2 = QPushButton("Tombol 2")
        self.tombol3 = QPushButton("Tombol 3")
        self.tombol4 = QPushButton("Tombol 4")
        self.tombol5 = QPushButton("Tombol 5")
        self.tombol6 = QPushButton("Tombol 6")
        layout = QGridLayout()
        layout.addWidget(self.tombol1, 0, 0)
        layout.addWidget(self.tombol2, 0, 1)
        layout.addWidget(self.tombol3, 0, 2)
        layout.addWidget(self.tombol4, 1, 0)
        layout.addWidget(self.tombol5, 1, 1, 1, 2)
        layout.addWidget(self.tombol6, 2, 0, 1, 3)
        self.setLayout(layout)
