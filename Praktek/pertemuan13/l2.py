
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *


class AddForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(350, 150)
        self.move(320, 280)
        self.setWindowTitle('Tambah Data')
        self.label1 = QLabel('Bahasa Pemrograman')
        self.languageEdit = QLineEdit()
        self.label2 = QLabel("Nama Pencipta")
        self.nameEdit = QLineEdit()
        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.languageEdit, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


class MainForm(QWidget):
    lastRecordNumber = -1

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(450, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QDialog.accept() dan QDialog.reject()')
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(0)
        self.setColumnAndHeaders()
        self.addButton = QPushButton('Tambah')
        self.deleteButton = QPushButton('Hapus')
        self.exitButton = QPushButton('Keluar')
        vbox = QVBoxLayout()
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.deleteButton)
        vbox.addStretch()
        vbox.addWidget(self.exitButton)

        layout = QHBoxLayout()
        layout.addWidget(self.tablewidget)
        layout.addLayout(vbox)
        self.setLayout(layout)
        self.addButton.clicked.connect(self.addButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.exitButton.clicked.connect(self.exitButtonClick)

    def setColumnAndHeaders(self):
        self.tablewidget.setColumnCount(2)
        columnHeaders = ['Bahasa Pemrograman', 'Nama Pencipta']
        self.tablewidget.setHorizontalHeaderLabels(columnHeaders)

    def addRow(self, row, itemLabels=[]):
        for i in range(2):
            item = QTableWidgetItem()
            item.setText(itemLabels[i])
        self.tablewidget.setItem(row, i, item)

    def addButtonClick(self):
        if MainForm.lastRecordNumber == self.tablewidget.rowCount()-1:
            self.tablewidget.setRowCount(self.tablewidget.rowCount()+1)
        form = AddForm()
        if form.exec_() == QDialog.Accepted:
            MainForm.lastRecordNumber += 1
            language = form.languageEdit.text()
            name = form.nameEdit.text()
            data = [language, name]
            self.addRow(MainForm.lastRecordNumber, data)

    def deleteButtonClick(self):
        tableData = []
        for i in range(0, self.tablewidget.rowCount()):
            language = self.tablewidget.item(i, 0).text()
            name = self.tablewidget.item(i, 1).text()
            tableData.append([language, name])
        row = self.tablewidget.currentRow()
        del tableData[row]
        MainForm.lastRecordNumber -= 1
        self.tablewidget.clear()

        self.setColumnAndHeaders()
        self.tablewidget.setRowCount(len(tableData))
        for i in range(0, len(tableData)):
            data = tableData[i]
            self.addRow(i, data)

    def exitButtonClick(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.setupUi()
    form.show()
    app.exec_()
