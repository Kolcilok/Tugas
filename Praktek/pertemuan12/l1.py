from PyQt5.QtWidgets import QWidget, QApplication, QFontComboBox, QSpinBox, QLabel, QGridLayout

from PyQt5.QtGui import QFont


class formSpinBox(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Praktikum 1: QSpinBox  @aku_bisa")
        self.labelJH = QLabel("Jenis Huruf")
        self.fontComboBJH = QFontComboBox()
        self.fontComboBJH.setEditable(True)
        self.labelUH = QLabel("Ukuran Huruf")
        self.spinBoxUH = QSpinBox()
        self.spinBoxUH.setRange(7, 32)
        self.spinBoxUH.setValue(12)
        self.spinBoxUH. setSingleStep(1)
        self.labelContoh = QLabel("Aku bisa belajar Python PyQt5!")
        self.labelContoh.setFont(QFont("Dejavu Sans", 18))

        grid = QGridLayout()

        grid.addWidget(self.labelJH, 0, 0)
        grid.addWidget(self.fontComboBJH, 0, 1)
        grid.addWidget(self. labelUH, 1, 0)
        grid.addWidget(self.spinBoxUH, 1, 1)
        grid.addWidget(self.labelContoh, 2, 0, 1, 2)
        self.setLayout(grid)

        self.fontComboBJH.activated.connect(self.fungsiUbahFont)
        self.spinBoxUH.valueChanged.connect(self.fungsiUbahFont)

    def fungsiUbahFont(self):
        self.labelContoh.setFont(
            QFont(self.fontComboBJH.currentText(), self.spinBoxUH.value()))


if __name__ == "__main__":
    app = QApplication([])
    form = formSpinBox()
    form.show()
    app.exec_()
