from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# kelas turunan dari QThread


class ThreadKu(QThread):
    def __init__(self, name, listWidget):
        super().__init__()
        self.name = name
        self.listWidget = listWidget
        # override metode run()

    def run(self):
        for i in range(1, 100):
            self.listWidget.addItem(self.name+' :'+str(i))


class KelasUtama (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        # membuat objek dari kelas QThread
        self.thread1 = ThreadKu('Thread 1', self.listWidget)
        self.thread2 = ThreadKu('Thread 2', self.listWidget)

    def setupUi(self):
        self.setWindowTitle("Demo QThread @panjul")
        self.labelJudul = QLabel("Demo QThread @panjul")
        self.listWidget = QListWidget()
        self.pushBMulai = QPushButton("Mulai")
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.pushBMulai)
        lay = QVBoxLayout()
        lay.addWidget(self.listWidget)
        lay.addLayout(hbox)
        self.setLayout(lay)
        self.pushBMulai.clicked.connect(self.pushBMulaiDiklik)

    def pushBMulaiDiklik(self):
        QApplication.processEvents()
        self.thread1.start()
        self.thread2.start()


if __name__ == '__main__':
    app = QApplication([])
    form = KelasUtama()
    form.show()
    app.exec()
