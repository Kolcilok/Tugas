# from PyQt6 import QtWidgets, QtGui, QtCore
# app = QtWidgets.QApplication([])

# form = QtWidgets.QWidget()
# form.move(300, 300)
# form.resize(200, 50)
# form.setWindowTitle("minimal form cara 1")

# label = QtWidgets.QLabel()
# label.setText("Contoh label cara 1")
# label.move(50, 20)
# label.setParent(form)
# form.show()
# app.exec()


# from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
# from PyQt6.QtCore import *
# app = QApplication([])

# form = QWidget()
# form.move(300, 300)
# form.resize(200, 50)
# form.setWindowTitle("minimal form cara 2")

# label = QLabel()
# label.setText("Contoh label cara 2")
# label.move(50, 20)
# label.setParent(form)
# form.show()
# app.exec()


# from PyQt6 import QtWidgets as qwd
# app = qwd.QApplication([])

# form = qwd.QWidget()
# form.move(300, 300)
# form.resize(200, 50)
# form.setWindowTitle("minimal form cara 3")

# label = qwd.QLabel()
# label.setText("Contoh label cara 3")
# label.move(50, 20)
# label.setParent(form)
# form.show()
# app.exec()


# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# app = QApplication([])
# form = QWidget()
# form.move(300, 300)
# form.resize(200, 50)
# form.setWindowTitle("minimal form cara 4")
# label = QLabel()
# label.setText("Contoh label cara 4")
# label.move(50, 20)
# label.setParent(form)
# form.show()
# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# if __name__ == '__main__':
#     a = QApplication(sys.argv)
#     form = QWidget()
#     form.setWindowTitle("GUI minimal")
#     form.resize(200, 100)
#     form.move(500, 300)
#     label = QLabel()
#     label.setText("Ini contoh label")
#     label.move(50, 70)
#     label.setParent(form)
#     form.show()
#     a.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# if __name__ == '__main__':
#     a = QApplication(sys.argv)
#     form = QWidget()
#     form.setWindowTitle("GUI minimal")
#     form.resize(200, 100)
#     form.move(500, 300)
#     label = QLabel()
#     label.setText("Ini contoh label")
#     label.move(50, 70)
#     label.setParent(form)
#     form.show()
#     a.exec()


# from PyQt6.QtWidgets import QApplication
# from MinimalForm import *
# if __name__ == '__main__':
#     a = QApplication([])
#     minform = MinimalForm()
#     minform.show()
#     a.exec()

# from PyQt6.QtWidgets import QWidget, QLabel, QApplication


# class MinimalForm(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.resize(300, 100)
#         self.move(300, 300)
#         self.setWindowTitle("Form GUI minimal")
#         self.label = QLabel()
#         self.label.setText("Contoh label dari 2 file")
#         self.label.move(50, 40)
#         self.label.setParent(self)


# if __name__ == '__main__':
#     a = QApplication([])
#     minform = MinimalForm()
#     minform.show()
#     a.exec()


# from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QApplication


# class MainForm(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.resize(300, 100)
#         self.move(300, 300)
#         self.setWindowTitle("Menutup Form")
#         self.tombol = QPushButton()
#         self.tombol.setText("Tutup")
#         self.tombol.move(50, 40)
#         self.tombol.setParent(self)
#         self.tombol.clicked.connect(self.tombolDiklik)

#     def tombolDiklik(self):
#         self.close()


# if __name__ == '__main__':
#     a = QApplication([])
#     minform = MainForm()
#     minform.show()
#     a.exec()

# from PyQt6.QtWidgets import QWidget, QDesktopWidget, QApplication
# from PyQt6.QtWidgets import QApplication, QWidget, QDesktopWidget


# class MainForm(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.resize(300, 100)
#         self.setWindowTitle("Form di tengah")
#         self.setCenter()

#     def setCenter(self):
#         desktop = QDesktopWidget()
#         screenwidth = desktop.screen().width()
#         screenheight = desktop.screen().height()
#         self.setGeometry((screenwidth-self.width())//2,
#                          (screenheight-self.height())//2,
#                          self.width(),
#                          self.height())


# if __name__ == '__main__':
#     a = QApplication([])
#     minform = MainForm()
#     minform.show()
#     a.exec()

# from FormLain_h93 import *
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QGuiApplication


# class MainForm(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.resize(300, 100)
#         self.setWindowTitle("Form di tengah")
#         self.setCenter()

#     def setCenter(self):
#         available_geometry = QGuiApplication.primaryScreen().availableGeometry()
#         screenwidth = available_geometry.width()
#         screenheight = available_geometry.height()
#         self.setGeometry((screenwidth - self.width()) // 2,
#                          (screenheight - self.height()) // 2,
#                          self.width(),
#                          self.height())


# if __name__ == '__main__':
#     app = QApplication([])
#     form = MainForm()
#     form.show()
#     app.exec_()


# class MainForm_h93(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.resize(300, 100)
#         self.move(300, 300)
#         self.setWindowTitle("Form Utama")
#         self.tombol = QPushButton()
#         self.tombol.setText("Tampillkan Form Lain")
#         self.tombol.move(50, 40)
#         self.tombol.setParent(self)
#         self.tombol.clicked.connect(self.tombolDiklik)

#     def tombolDiklik(self):
#         self.form = FormLain_h93()
#         self.form.show()


# if __name__ == '__main__':
#     app = QApplication([])
#     main_form = MainForm_h93()
#     main_form.show()
#     app.exec()

# from PyQt6.QtWidgets import (QPushButton, QLabel, QToolTip, QWidget)
# from PyQt6.QtGui import QFont


# class MainForm_h95(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.setWindowTitle("Menampilkan ToolTip")
#         self.move(300, 300)
#         self.resize(500, 100)

#         QToolTip.setFont(QFont("SanSerif", 10))
#         self.setToolTip("Ini adalah <i>ToolTip</i>")
#         self.tombol = QPushButton("Tombol Keluar")
#         self.tombol.move(50, 50)
#         self.tombol.setParent(self)
#         self.tombol.setToolTip("Ini adalah contoh <b>ToolTip</b>")
#         self.tombol .clicked. connect(self. tomkeluar)

#     def tomkeluar(self):
#         self.close()


# if __name__ == '__main__':
#     app = QApplication([])
#     main_form = MainForm_h95()
#     main_form.show()
#     app.exec()
