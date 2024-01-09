from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon


class FormLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Demo QTextEdit @aku_bisa")
        self.setGeometry(30, 100, 300, 150)
        self.label1 = QLabel("           Demo QTextEdit")
        self.label2 = QLabel("===========================")
        self.labelHP = QLabel('No. HP')
        self.LineEditHP = QLineEdit()
        self.labelPesan = QLabel('Pesan')
        self.LineEditPesan = QTextEdit()

        garisH = QFrame()
        garisH.setFrameShadow(QFrame.Sunken)
        garisH.setFrameShape(QFrame.HLine)
        icon1 = QIcon("images.jpg")
        self.pushButtonKirim = QPushButton("Kirim")
        self. pushButtonKirim.setIcon(icon1)
        icon2 = QIcon("images.jpg")
        self.pushButtonBatal = QPushButton("Batal")
        self.pushButtonBatal . setIcon(icon2)
        hbox = QHBoxLayout()
        hbox. addStretch()
        hbox. addWidget(self. pushButtonKirim)
        hbox. addWidget(self. pushButtonBatal)
        layout = QVBoxLayout()
        layout.addWidget(self. labelHP)
        layout.addWidget(self. LineEditHP)
        layout.addWidget(self. labelPesan)
        layout.addWidget(self.LineEditPesan)
        layout.addWidget(garisH)
        layout.addLayout(hbox)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    form = FormLabel()
    form.show()
    app.exec_()
