from PyQt5.QtWidgets import QGridLayout, QPushButton, QLineEdit, QWidget, QApplication


class MainForm_h105(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Mendemontrasikan Signal & slot")
        self.move(300, 300)
        self.resize(500, 100)

        self.tombolBersih = QPushButton("Bersihkan")
        self.tombolTutup = QPushButton("Tutup")
        self.lineEdit = QLineEdit("Tulis Disini untuk Demo Signal & slot")
        layout = QGridLayout()
        layout.addWidget(self.tombolBersih, 1, 0)
        layout.addWidget(self.tombolTutup, 1, 1)
        layout.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.setLayout(layout)
        self.tombolBersih.clicked.connect(self.lineEdit.clear)


if __name__ == '__main__':
    app = QApplication([])
    form = MainForm_h105()
    form.show()
    app.exec()
