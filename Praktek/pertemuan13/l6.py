
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FormKu(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo QDir @aku_bisa")
        self.labelJudul = QLabel("Demo QDir terkait DIRECTORY @aku_bisa")
        self.groupBox1 = QGroupBox("MEMBUAT DIREKTORI")
        self.labelND = QLabel("Nama direktori yang akan dibuat")
        self.lineEditND = QLineEdit("Folderku")
        self.pushButtonBuatD = QPushButton("Buat Direktori")
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.labelND)
        vbox1.addWidget(self.lineEditND)
        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(self.pushButtonBuatD)
        vbox1.addLayout(hbox1)
        self.groupBox1.setLayout(vbox1)
        self.groupBox2 = QGroupBox("MENGUBAH NAMA DIRECTORY")
        self.labelNDLama = QLabel("Nama Direktori Lama")
        self.lineEditNDLama = QLineEdit("Folderku")
        self.labelNDBaru = QLabel("Nama Direktori Baru")

        self.lineEditNDBaru = QLineEdit("FolderBaruku")
        self.pushButtonUbahND = QPushButton("Ubah Nama Direktori")
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.pushButtonUbahND)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.labelNDLama)
        vbox2.addWidget(self.lineEditNDLama)
        vbox2.addWidget(self.labelNDBaru)
        vbox2.addWidget(self.lineEditNDBaru)
        vbox2.addLayout(hbox2)
        self.groupBox2.setLayout(vbox2)
        self.groupBox3 = QGroupBox("MENGHAPUS DIREKTORI")
        self.labelNDDihapus = QLabel("Nama direktor yang akan dihapus")
        self.lineEditNDDihapus = QLineEdit("FolderBaruku")
        self.pushButtonHapusD = QPushButton("Hapus Direktori")
        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addWidget(self.pushButtonHapusD)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.labelNDDihapus)
        vbox3.addWidget(self.lineEditNDDihapus)
        vbox3.addLayout(hbox3)

        self.pushButtonBuatD.clicked.connect(self.pbBuatDDiklik)
        self.pushButtonUbahND.clicked.connect(self.pbUbahNDDiklik)
        self.pushButtonHapusD.clicked.connect(self.pbHapusDDiklik)
        self.direktori = QDir()
        self.groupBox3.setLayout(vbox3)
        lay = QVBoxLayout()
        lay.addWidget(self.groupBox1)
        lay.addWidget(self.groupBox2)
        lay.addWidget(self.groupBox3)
        self.setLayout(lay)

    def pbBuatDDiklik(self):
        print('Direktori dibuat')
        if len(self.lineEditND.text().strip()) == 0:
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Nama direktori harus diisi!")
            self.lineEditND.setFocus()
        return
        if self.direktori.exists(self.lineEditND.text()):
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 f"Nama direktori {self.lineEditND.text()} sudah ada.\nGanti nama yang lain!")
        self.lineEditND.setFocus()
        return
        namaDirektori = self.lineEditND.text()

        if self.direktori.mkdir(namaDirektori):
            QMessageBox.information(self, "Informasi",
                                    f"Direktori dengan nama {namaDirektori} berhasil dibuat")
        else:
            QMessageBox.information(self, "Informasi",
                                    f"Direktori dengan nama {namaDirektori} gagal dibuat")

    def pbUbahNDDiklik(self):
        if len(self.lineEditNDBaru.text().strip()) == 0:
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Nama direktori baru harus diisi")
            self.lineEditNDBaru.setFocus()
        return
        if len(self.lineEditNDLama.text().strip()) == 0:
            QMessageBox.critical(self, "Pesan Kesalahn",
                                 "Nama direktori lama harus diisi")
            self.lineEditNDLama.setFocus()
        return
        if not self.direktori.exists(self.lineEditNDLama.text()):
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Nama direktori lama tidak ditemukan")
            self.lineEditNDLama.setFocus()
        return
        dirlama = self.lineEditNDLama.text()
        dirBaru = self.lineEditNDBaru.text()
        if self.direktori.rename(dirLama, dirBaru):
            QMessageBox.information(
                self, "Informasi", "Direktori lama berhasil diubah")
        else:
            QMessageBox.information(
                self, "Informasi", "Direktori lama gagal diubah")

    def pbHapusDDiklik(self):
        if len(self.lineEditNDDihapus.text().strip()) == 0:
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Nama direktori yang akan dihapus harus d ")
        if not self.direktori.exists(self.lineEditNDDihapus.text()):
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Nama direktori tidak ditemukan")
            dirDihapus = self.lineEditNDDihapus.text()
        if self.direktori.rmdir(dirDihapus):
            QMessageBox.information(
                self, "Informasi", "Direktori berhasil dihapus!")
        else:
            QMessageBox.information(
                self, "Informasi", "Direktori gagal dihapus!")


if __name__ == "__main__":
    app = QApplication([])
    form = FormKu()
    form.setupUi()
    form.show()
    app.exec()
