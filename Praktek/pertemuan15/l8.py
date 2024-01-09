
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout
import pymysql


class Formku(QWidget):
    def setupUi(self):
        self.setWindowTitle("Belajar Database @aku_bisa")
        self.labelJudul = QLabel("Belajar CRUD @aku_bisa")
        self.labelND = QLabel("Nama Depan")
        self.lineEditND = QLineEdit()
        self.labelNB = QLabel("Nama Belakang")
        self.lineEditNB = QLineEdit()
        self.labelAl = QLabel("Alamat")
        self.textEditAl = QTextEdit()
        self.labelHP = QLabel("No HP")
        self.lineEditHP = QLineEdit()
        self.pushButtonCek = QPushButton("Cek Nama Depan")
        self.pushButtonSimpan = QPushButton("Simpan")
        self.pushButtonUbah = QPushButton("Ubah")
        self.pushButtonHapus = QPushButton("Hapus")
        self.pushButtonBersih = QPushButton("Bersihkan")
        self.pushButtonCekkoneksi = QPushButton("Cek Koneksi")
        grid = QGridLayout()
        grid.addWidget(self.labelJudul, 0, 0, 1, 2)
        grid.addWidget(self.labelND, 1, 0)
        grid.addWidget(self.lineEditND, 1, 1)
        grid.addWidget(self.labelNB, 2, 0)
        grid.addWidget(self.lineEditNB, 2, 1)
        grid.addWidget(self.labelAl, 3, 0)
        grid.addWidget(self.textEditAl, 3, 1)
        grid.addWidget(self.labelHP, 4, 0)
        grid.addWidget(self.lineEditHP, 4, 1)
        grid.addWidget(self.pushButtonCekkoneksi, 1, 2)
        grid.addWidget(self.pushButtonCek, 2, 2)
        grid.addWidget(self.pushButtonSimpan, 5, 0)
        grid.addWidget(self.pushButtonUbah, 5, 1)
        grid.addWidget(self.pushButtonHapus, 5, 2)
        grid.addWidget(self.pushButtonBersih, 5, 3)

        self.setLayout(grid)
        self.pushButtonCekkoneksi.clicked.connect(self.konekdb)
        self.pushButtonCek.clicked.connect(self.tampil)
        self.pushButtonSimpan.clicked.connect(self.simpan)
        self.pushButtonUbah.clicked.connect(self.ubah)
        self.pushButtonHapus.clicked.connect(self.hapus)
        self.pushButtonBersih.clicked.connect(self.hapusinput)

    def konekdb(self):
        con = pymysql.connect(db='testdb', user='root', passwd='',
                              host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if (cur):
            print("Koneksi berhasil")
            QMessageBox.information(self, 'Informasi', 'Koneksi berhasil')
        else:
            print("Koneksi gagal")
            QMessageBox.information(self, 'Informasi', 'Koneksi gagal')
        print(cur)
        print(type(cur))

    def simpan(self):
        namadepan = self.lineEditND.text()
        namabelakang = self.lineEditNB.text()
        alamat = self.textEditAl.toPlainText()
        nohp = self.lineEditHP.text()
        if (len(self.lineEditND.text().strip()) == 0 or
            len(self.lineEditNB.text().strip()) == 0 or
            len(self.textEditAl.toPlainText().strip()) == 0 or
                len(self.lineEditHP.text().strip()) == 0):
            QMessageBox.critical(self, "Pesan Kesalahan",
                                 "Data belum lengkap. Silakan diisi semua!")

        else:
            insert = (namadepan, namabelakang, alamat, nohp)
            print(insert)
            con = pymysql.connect(db='testdb', user='root', passwd='',
                                  host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO bukualamat (namadepan, namabelakang, alamat, nohp)" +\
                "VALUES"+str(insert)
            data = cur.execute(sql)
        if (data):
            QMessageBox.information(self, "Informasi", "Data tersimpan")
        else:
            QMessageBox.information(self, "Informasi", "Data gagal tersimpan")

    def tampil(self):
        namadepan = self.lineEditND.text()
        con = pymysql.connect(db='testdb', user='root', passwd='',
                              host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "SELECT * FROM bukualamat WHERE namadepan='"+str(namadepan)+"'"
        cur.execute(sql)
        data = cur.fetchall()
        if (data):
            for a in data:
                self.lineEditNB.setText("" + a[1])
                self.textEditAl.setText("" + a[2])
                self.lineEditHP.setText("" + a[3])
        else:
            QMessageBox.information(self, "informasi", "data kosong!")

    def ubah(self):
        namadepan = self.lineEditND()
        namabelakang = self.lineEditNB.text()
        alamat = self.textEditAl.toPlainText()
        nohp = self.lineEditHP.text()

        con = pymysql.connect(db='testdb', user='root', passwd='',
                              host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql-"""UPDATE bukualamat SET namabelakang=%s,
        alamat-xs,
        nohp-%s
        WHERE namadepan=%s"""
        val = (namabelakang, alamat, nohp, namadepan)
        data = cur.execute(sql, val)
        if (data):
            QMessageBox.information(
                self, "Informasi", "Sukses... Data berhasil diubah!")
        else:
            QMessageBox.information(
                self, "Informasi", "Gagal... Data gagal diubah!")

    def hapus(self):
        namadepan = self.lineEditND.text()
        con = pymysql.connect(db='testdb', user='root', passwd='',
                              host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM bukualamat WHERE namadepan=%%s"
        data = cur.execute(sql, (namadepan))
        if (data):
            QMessageBox.information(
                self, "informasi", "Sukses.... Data berhasil dihapus")
        else:
            QMessageBox.information(
                self, "informasi", "Gagal.... Data gagal dihapus")
        self.hapusinput()

    def hapusinput(self):
        self.lineEditND.clear()
        self.lineEditNB.clear()
        self.textEditAl.clear()
        self.lineEditHP.clear()


if __name__ == '__main__':
    app = QApplication([])
    form = Formku()
    form.setupUi()
    form.show()
    app.exec()
