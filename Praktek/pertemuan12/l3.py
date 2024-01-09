from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FormSpinBox(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(
            "Praktikum 3: QCalendarWidget @aku_bisa")
        self.kalendar = QCalendarWidget()
        self.kalendar.setGridVisible(True)
        self.kalendar.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.checkBoxHariPendek = QCheckBox("Hari pendek")
        self.dateEdit = QDateEdit()
        self.dateEdit.setDisplayFormat("dd MM yyyy")
        self.pushBTentukanT = QPushButton("Tentukan Tanggal")
        self.pushBAmbilT = QPushButton("Ambil Tanggal")
        hbox = QHBoxLayout()
        hbox.addWidget(self.dateEdit)
        hbox.addWidget(self.pushBTentukanT)
        hbox.addWidget(self.pushBAmbilT)
        lay = QHBoxLayout()
        lay.addWidget(self.kalendar)
        lay.addWidget(self.checkBoxHariPendek)
        lay.addLayout(hbox)
        self.setLayout(lay)
        self.checkBoxHariPendek.clicked.connect(self.fungsiHariPendek)
        self.pushBTentukanT.clicked.connect(self.fungsiTentukanH)
        self.pushBAmbilT.clicked.connect(self.fungsiAmbilH)

    def fungsiHariPendek(self):
        if self.checkBoxHariPendek.isChecked():
            self.kalender.setHorizontalHeaderFormat(
                QCalendarWidget.ShortDayNames)
        else:
            self.kalender.setHorizontalHeaderFormat(
                QCalendarWidget.LongDayNames)

    def fungsiTentukanH(self):
        self.kalender.setSelectedDate(self.dateEdit.date())

    def fungsiAmbilH(self):
        QMessageBox.information(self, "Informasi dari ku",
                                self.kalender.selectedDate().toString())


if __name__ == "__main__":
    app = QApplication([])
    form = FormSpinBox()
    form.show()
    app.exec_()
