"""
simple pyQt application. Shows window
todo: make app installer program for...Arch?
"""

#!/usr/bin/python3

import sys
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtGui import QIcon
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
       btn = QPushButton('Click to destroy myself',self)
       btn.setToolTip('test button <b>QPushButton</b>')
       btn.resize(btn.sizeHint())
       btn.move(50,50)
       btn.clicked.connect(QApplication.instance().quit)       


       self.setGeometry(300,300,300,200)
       self.setWindowTitle('Tooltips test')
       self.show()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
