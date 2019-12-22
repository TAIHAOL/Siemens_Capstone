#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:39:38 2019

@author: alexispritchard
"""

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


import Site


class SiteCanvas(QScrollArea):

    def __init__(self):

        super(SiteCanvas, self).__init__()

        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)
        self.sm = Site.SiteViewManager(self.layout)
        
        for i in range(0):
            x = Site.SiteName("%d"%i)
            y = Site.SiteView(x, self)
            self.sm.addSite(y)


        
        self.setWidget(self.widget)
        self.setWidgetResizable(True)

class SiteScreen(QMainWindow):

    def __init__(self):

        super(SiteScreen, self).__init__()

        self.setupWindow()
        self.setGeometry(90, 90, 1200, 800)
        self.setWindowTitle('site screen')

        self.widget = SiteCanvas()
        self.layout = QGridLayout(self.widget)

        menubar = self.menuBar()
        siteMenu = menubar.addMenu('Site')

        
        imp2Menu = QMenu('remove a site', self)
        imp2Act = QAction('which site do you want to remove', self)
        imp2Menu.addAction(imp2Act)

        self.newSite = QAction('add a site', self)
        
        siteMenu.addAction(self.newSite)
        siteMenu.addMenu(imp2Menu)

        self.inView = None

        self.newSite.triggered.connect(self.createInputViewForSite)


        self.setCentralWidget(self.widget)
        
        
    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())

    def createInputViewForSite(self):
        self.inView = Site.createInputViewForSite(self);
        

    def setupUi(self, Interface):
        self.centralWidget = QtWidgets.QWidget(Interface)
        layout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1112, 932))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        Interface.setCentralWidget(self.centralWidget)

