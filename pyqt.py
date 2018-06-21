#simple pyQt application. Shows window
#todo: make app installer program for...Arch?


#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   w.resize(1920,1080)
   w.move(0,10)
   w.setWindowTitle('Test! Title')
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
