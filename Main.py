# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:45:46 2019

@author: asp5423
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import SiteScreen

class Main(QMainWindow):

    def __init__(self):

        super(Main, self).__init__()

        self.site = SiteScreen.SiteScreen()
        self.site.show()
        
        
        

    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())

    def createInputView(self):
        self.inView = Input.createInputView(self);
        self.silo_view = SiloViewCon.createSiloView(self, self.x)

app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
