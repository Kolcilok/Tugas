from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class formSpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(
            "Praktikum 2: QDateEdit,QTimeEdit, QDateTimeEdit @aku_bisa")
        self.labelW = QLabel("Waktu")
        self.timeEditW = QTimeEdit()
        self.timeEditW.setDisplayFormat("hh.mm")
        self.timeEditW.setTime(QTime.currentTime())
        self.labelHT = QLabel("Hari Tanggal")
        self.dateEditHT = QDateEdit()
        self.dateEditHT.setDate(QDate.currentDate())
        self.labelHTW = QLabel("Hari Tanggal & waktu")
        self.dateTimeEditHTW = QDateTimeEdit()
        self.dateTimeEditHTW.setDisplayFormat("dddd,dd MM yyyy hh.mm")
        self.dateTimeEditHTW. setDateTime(QDateTime.currentDateTime())
        self.labelContoh = QLabel("QDateTimeEdit Python PyQt5!")
        self.labelContoh. setFont(QFont("Dejavu Sans", 18))
        self.pushButtonOk = QPushButton("OK")

        self.pushButtonOk.clicked.connect(self. fungsiOkDiklik)

        grid = QGridLayout()
        grid.addWidget(self.labelW, 0, 0)
        grid.addWidget(self .timeEditW, 0, 1)
        grid.addWidget(self. labelHT, 1, 0)
        grid.addWidget(self.dateEditHT, 1, 1)
        grid.addWidget(self.labelHTW, 2, 0)
        grid.addWidget(self.dateTimeEditHTW, 2, 1)
        grid.addWidget(self.labelContoh, 3, 0, 1, 2)
        grid.addWidget(self. pushButtonOk, 4, 1)
        self.setLayout(grid)

    def fungsiOkDiklik(self):
        QMessageBox.information(self, "Informasi", "Hari Ini Menunjukan : " +
                                "Waktu : "+self.timeEditW.time().toString()+"\n" +
                                "Hari : "+self.dateEditHT.date().toString()+"\n" +
                                "Waktu Lengkap : "+self.dateTimeEditHTW.dateTime().toString()+"\n")


if __name__ == "__main__":
    app = QApplication([])
    form = formSpinBox()
    form.show()
    app.exec_()
