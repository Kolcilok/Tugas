from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFontComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont


class FormLabel(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QFontComboBox @aku_bisa")
        self.setGeometry(30, 100, 500, 150)
        self.label1 = QLabel(" <b> Demo QFontComboBox</b>")
        self.label2 = QLabel("============================")
        self.fontComboB = QFontComboBox()
        self.fontComboB.setEditable(False)
        self.fontComboB.activated.connect(self.fontComboBDiaktivasi)
        self.labelFont = QLabel("Astaghfirullaha wa'atuubu ilaih...")
        self.labelFont.setFont(QFont('Dejavu Sans', 21))

        lay = QVBoxLayout()
        lay.addWidget(self.label1)
        lay.addWidget(self.label2)
        lay.addWidget(self.fontComboB)
        lay.addWidget(self.labelFont)
        self.setLayout(lay)

    def fontComboBDiaktivasi(self):
        self.labelFont.setFont(QFont(self.fontComboB.currentText(), 23))


if __name__ == "__main__":

    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
