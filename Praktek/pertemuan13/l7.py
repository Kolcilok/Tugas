from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FormKu(QWidget):
    def setupUi(self):
        self.setWindowTitle("Demo QTImer @aku_bisa")
        self.labelJudul = QLabel("Demo QTimer @aku_bisa")
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        font = QFont()
        font.setFamily("Forte")
        font.setPixelSize(30)
        self.label = QLabel()
        self.label.setFont(font)
        lay = QHBoxLayout()
        lay.addWidget(self.label)
        self.setLayout(lay)
        self.timer.timeout.connect(self.timerTimer)

    def timerTimer(self):
        currentTime = QTime.currentTime()
        self.label.setText(currentTime.toString())


if __name__ == "__main__":
    app = QApplication([])
    form = FormKu()
    form.setupUi()
    form.show()
    app.exec()
