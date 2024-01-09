from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class formSpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):

        self.labelGen = QLabel("Bilangan Genap")

        self.listWidgetGen = QListWidget()

        self.progressBar = QProgressBar()

        self.setWindowTitle("Praktikum 6: QListWidget @aku_bisa")
        self.labelGan = QLabel("Bilangan Ganjil")
        self.listWidgetGan = QListWidget()

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.pushButton = QPushButton("Mulai...")
        grid = QGridLayout()
        grid.addWidget(self.labelGan, 0, 0)
        grid.addWidget(self.listWidgetGan, 1, 0)

        grid.addWidget(self.labelGen, 0, 1)
        grid.addWidget(self.listWidgetGen, 1, 1)
        grid.addWidget(self.progressBar, 2, 0, 1, 2)
        grid.addWidget(self.pushButton, 3, 0, 1, 2)
        self.setLayout(grid)
        self.pushButton.clicked.connect(self.pBDiklik)

    def pBDiklik(self):
        self.progressBar.setValue(0)
        for i in range(1, 100):
            QApplication.processEvents()
            if i % 2 == 1:
                self.listWidgetGan.addItem(str(i))
            else:
                self.listWidgetGen.addItem(str(i))
            self.progressBar.setValue(self.progressBar.value()+1)


if __name__ == '__main__':
    app = QApplication([])
    form = formSpinBox()
    form.show()
    app.exec_()
