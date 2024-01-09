from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QPushButton dengan QIcon @aku_bisa")
        self.setGeometry(30, 100, 300, 150)
        self.label1 = QLabel(
            "QPushButton untuk menampilkan Icon dari kelas QIcon modul QtGui")
        self.label2 = QLabel("==========================================")
        icon1 = QIcon("images.jpg")
        self.pBTambah = QPushButton("Tambah")
        self.pBTambah.setIcon(icon1)
        self.pBTambah.setParent(self)
        self.pBTambah.setGeometry(30, 30, 90, 20)
        icon2 = QIcon("images.jpg")
        self.pBUbah = QPushButton("Pengaturan")
        self.pBUbah.setIcon(icon2)
        self.pBUbah.setParent(self)
        self.pBUbah.setGeometry(30, 70, 90, 20)
        icon2 = QIcon("icon1bendera.gif")
        self.pBHapus = QPushButton("OK")
        self.pBHapus.setIcon(icon2)
        self.pBHapus.setParent(self)
        self.pBHapus.setGeometry(30, 110, 90, 20)


if __name__ == '__main__':
    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
