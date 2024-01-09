from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class formSpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Praktikum 4: QSlider @aku_bisa")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(47)
        self.slider.setMaximum(101)
        self.slider.setMinimum(-1)
        self.lcd = QLCDNumber()
        self.lcd.display(47)
        self.lcd.setDigitCount(4)
        self.label = QLabel("aku_bisa")
        lay = QVBoxLayout()
        lay.addWidget(self.slider)
        lay.addWidget(self.lcd)
        lay.addWidget(self.label)
        self.setLayout(lay)
        self.slider.sliderMoved.connect(self.sliderDigeser)

    def sliderDigeser(self):
        self.lcd.display(str(self.slider.value()))


if __name__ == '__main__':
    app = QApplication([])
    form = formSpinBox()
    form.show()
    app.exec_()
