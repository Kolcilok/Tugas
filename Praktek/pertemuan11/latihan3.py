from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QLabel,QLineEdit dan QPushButton @aku_bisa")
        self.setGeometry(30, 100, 500, 320)
        self.label1 = QLabel(
            "QLabel untuk menampilkan Gambar dari kelas QPixmap modul QtGui")
        self.label2 = QLabel("==========================================")
        Pixmap1 = QPixmap("images.jpg")
        self.label3 = QLabel()
        self.label3.setPixmap(Pixmap1)
        self.label1.setParent(self)
        self.label1.setGeometry(30, 30, 400, 10)
        self.label2.setParent(self)
        self.label2.setGeometry(30, 40, 400, 10)
        self.label3.setParent(self)
        self.label3.setGeometry(30, 5, 400, 400)


if __name__ == '__main__':
    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
