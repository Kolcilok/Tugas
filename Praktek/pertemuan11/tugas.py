from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 158)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 19, 160, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelBilangan1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelBilangan1.setObjectName("labelBilangan1")
        self.verticalLayout.addWidget(self.labelBilangan1)
        self.lineEditB1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditB1.setObjectName("lineEditB1")
        self.labelBilangan2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lineEditB2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditB1.setObjectName("lineEditB1")
        self.verticalLayout.addWidget(self.lineEditB1)
        self.labelBilangan2.setObjectName("labelBilangan2")
        self.verticalLayout.addWidget(self.labelBilangan2)
        self.lineEditB2.setObjectName("lineEditB2")
        self.verticalLayout.addWidget(self.lineEditB2)
        self.labelHasilPerhitungan = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.lineEditHP = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.labelHasilPerhitungan.setObjectName("labelHasil Perhitungan")
        self.verticalLayout.addWidget(self.labelHasilPerhitungan)

        self.lineEditHP.setObjectName("lineEditHP")
        self.verticalLayout.addWidget(self.lineEditHP)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 20, 81, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButtonTambah = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)

        self.pushButtonTambah.setObjectName("pushButtonTambah")
        self.verticalLayout_2.addWidget(self.pushButtonTambah)

        self.pushButtonKurang = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)

        self.pushButtonKurang.setObjectName("pushButtonKurang")
        self.verticalLayout_2.addWidget(self.pushButtonKurang)
        self.pushButtonkali = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.pushButtonkali.setObjectName("pushButtonkali")
        self.verticalLayout_2.addWidget(self.pushButtonkali)
        self.pushButtonBagi = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.pushButtonBagi.setObjectName("pushButtonBagi")
        self.verticalLayout_2.addWidget(self.pushButtonBagi)
        self.frame = QtWidgets.QFrame(Form)

        self.frame.setGeometry(QtCore.QRect(200, 20, 3, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButtonTambah.clicked.connect(self.fungsiTambah)
        self.pushButtonKurang.clicked.connect(self.fungsiKurang)
        self.pushButtonkali.clicked.connect(self.fungsiKali)

        self.pushButtonBagi.clicked.connect(self.fungsiBagi)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Demo QLabel QD @aku_bisa"))
        self.labelBilangan1.setText(_translate(
            "Form", "Masukkan Bilangan pertama"))
        self.labelBilangan2.setText(_translate(
            "Form", "Masukkan Bilangan kedua"))
        self.labelHasilPerhitungan.setText(
            _translate("Form", "Hasil Perhitungan"))
        self.pushButtonTambah.setText(_translate("Form", "&Tambah"))
        self.pushButtonKurang.setText(_translate("Form", "&Kurang"))
        self.pushButtonkali.setText(_translate("Form", "&Kali"))
        self.pushButtonBagi.setText(_translate("Form", "&Bagi"))

    def hitung(self, operator):
        b1 = float(self.lineEditB1.text())
        b2 = float(self.lineEditB2.text())
        if (operator == '+'):
            h = b1+b2
        elif (operator == '-'):
            h = b1-b2
        elif (operator == '*'):
            h = b1*b2
        else:
            h = b1/b2
        self.lineEditHP.setText(str(h))

    def fungsiTambah(self):
        self.hitung('+')

    def fungsiKurang(self): self.hitung('-')

    def fungsiKali(self):
        self.hitung('*')

    def fungsiBagi(self): self.hitung('/')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
