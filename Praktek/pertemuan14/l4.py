import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(450, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan QMessageBox @aku_bisa')
        self.tombolAbout = QPushButton('About')
        self.tombolCritical = QPushButton('Critical')
        self.tombolInformation = QPushButton('Information')
        self.tombolQuestion = QPushButton('Question')
        self.tombolWarning = QPushButton('Warning')
        layout = QHBoxLayout()
        layout.addWidget(self.tombolAbout)
        layout.addWidget(self.tombolCritical)
        layout.addWidget(self.tombolInformation)
        layout.addWidget(self.tombolQuestion)
        self.setLayout(layout)
        layout.addWidget(self.tombolWarning)
        self.tombolAbout.clicked.connect(self.tombolAboutClick)
        self.tombolCritical.clicked.connect(self.tombolCriticalClick)
        self.tombolInformation.clicked.connect(self.tombolInformationClick)
        self.tombolQuestion.clicked.connect(self.tombolQuestionClick)
        self.tombolWarning.clicked.connect(self.tombolWarningClick)

    def tombolAboutClick(self):
        QMessageBox.about(self, 'Tentang Program',
                          'Program Kehidupan\n' +
                          'Versi 1.1.1\n' +
                          'Semoga Alloh mudahkan jalan kita semua menuju Jannah-Nya. Aamiin... \n')

    def tombolCriticalClick(self):
        QMessageBox.critical(self, 'Pesan Kesalahan',
                             'Maaf, file ganteng.exe dan cantik.exe tidak ditemukan.\n'
                             'yang ada adalah file turunanGantengBanget.exe dan turunanCantikBanget.exe tapi kalo tanjakan.?:')

    def tombolInformationClick(self):
        QMessageBox.information(self,
                                'Informasi',
                                'Alhamdulillah, proses pengerjaan skripsi telah berhasil dilakukan\n'
                                'Semoga segera lulus ujian, dapet kerjaan, tanpa pacaran dan segera dihalalkan! Aamiin...')

    def tombolQuestionClick(self):
        fileName = 'viruskegalauan.exe'
        response = QMessageBox.question(self, 'Konfirmasi',
                                        'Anda yakin akan menghapus file %s?' % fileName)
        if response == QMessageBox.Yes:
            QMessageBox.about(self, 'Respon',
                              f'Anda memilih tombol Yes. \nAlhamdulillah... {fileName} telah terhapus. @aku_bisa')
        else:
            QMessageBox.about(self, 'Respon',
                              f'Anda memilih tombol No.\nSegera hapus {fileName} tersebut! @aku_bisa')

    def tombolWarningClick(self):
        QMessageBox.warning(self, 'Peringatan',
                            'Operasi ini akan menghapus semua data di dalam disk Anda!\n' +
                            'Tapi tak akan menghapus cintaku padamu wahai isteriku/suamiku! :)')


if __name__ == "__main__":
    app = QApplication([])
    form = MainForm()
    form.setupUi()
    form.show()
    app.exec()
