
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

import Silo
import Input
import SiloViewCon

class SiloCanvas(QScrollArea):
    def __init__(self):
        super(SiloCanvas, self).__init__()

        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.sm = Silo.SiloViewManager(self.layout)

        self.setWidget(self.widget)
        self.setWidgetResizable(True)

class SiloScreen(QMainWindow):

    def __init__(self, silo_list):

        super(SiloScreen, self).__init__()

        self.setupWindow()
        self.setGeometry(90, 90, 1200, 800)
        self.setWindowTitle('site screen')

        self.widget = SiloCanvas()
        self.layout = QGridLayout(self.widget)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        siteMenu = menubar.addMenu('Site')

        impMenu = QMenu('remove a silo', self)
        impAct = QAction('which silo you want to remove', self)
        impMenu.addAction(impAct)
        
        imp2Menu = QMenu('remove a site', self)
        imp2Act = QAction('which site you want to remove', self)
        imp2Menu.addAction(imp2Act)

        self.newAct = QAction('add a silo', self)
        self.newSite = QAction('add a site', self)

        fileMenu.addAction(self.newAct)
        fileMenu.addMenu(impMenu)
        
        
        siteMenu.addAction(self.newSite)
        siteMenu.addMenu(imp2Menu)
        

        self.inView = None

        self.newAct.triggered.connect(self.createInputView)
        
        self.silo_list = silo_list
        for silo in silo_list:
            self.widget.sm.addSilo(silo)
        self.widget.sm.silo_list = self.silo_list

        self.setCentralWidget(self.widget)

        
    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())

    def createInputView(self):
        self.inView = Input.createInputView(self);
