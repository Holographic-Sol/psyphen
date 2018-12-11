from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog, QAction, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui, QtCore
import sys
import os
import codecs
import subprocess

# Encoding
encode = u'\u5E73\u621015\u200e'

# Subprocess Info
info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

# Threads
timer_thread = ()

# GUI
class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.left = 0
        self.top = 0
        self.width = 30
        self.height = 10
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.initUI()
        
    def initUI(self):
        #UI Geometry
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        timer_thread = timer_threadClass()
        timer_thread.start()

        self.btn1 = QLabel(self)
        self.btn1.move(0, 0)
        self.btn1.resize(10, 10)
        btn1_image_path = './led_on_8x8.png'
        pixmap = QPixmap(btn1_image_path)
        self.btn1.setPixmap(pixmap)

        self.btn2 = QLabel(self)
        self.btn2.move(10, 0)
        self.btn2.resize(10, 10)
        self.btn2.setPixmap(pixmap)

        self.btn3 = QLabel(self)
        self.btn3.move(20, 0)
        self.btn3.resize(10, 10)
        self.btn3.setPixmap(pixmap)
        
        self.show()

class timer_threadClass(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        print('timer_threadClass: started')
        time.sleep(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
