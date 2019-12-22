
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:12:27 2019

@author: asp5423
"""

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

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy

import SiloScreen
import SiloViewCon

class SiteName(object):

    def __init__(self, name, site_list=None):
        super(SiteName, self).__init__()

        self.name = name;
        if site_list is None:
            self.site_list = []
        else:
            self.site_list = site_list

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def getSiteList(self):
        return self.site_list

class SiteView(QWidget):
    WIDTH = 150
    HEIGHT = 150

    def __init__(self, site, window):
        super(SiteView, self).__init__()

        self.site = site
        self.layout = QVBoxLayout(self)
        self.qt_button = QPushButton("Site: %s\n"%(site.getName()), self)
        #self.qt_button.resize(SiteView.WIDTH, SiteView.HEIGHT)
        self.layout.addWidget(self.qt_button)

        self.qt_button.setFixedSize(QSize(SiteView.WIDTH, SiteView.HEIGHT))

        self.qt_button.show();

        self.show()

        self.sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)



        @pyqtSlot()
        def silo_handler():
            
            #self.silo_view = SiloViewCon.createSiloView(self, self.site)
            self.silo_view = SiloScreen.SiloScreen(self.site.getSiteList())
            self.silo_view.show()

        self.qt_button.clicked.connect(silo_handler)
        self.show()
    
    def updateModel(self, site):
        self.qt_button.setText("Silo: %s\n"%(site.getName() ))
        self.qt_button.show()

    
    def sizeHint(self):
        return QSize(SiteView.WIDTH, SiteView.HEIGHT)

    
class SiteViewManager(object):
    SPACING = 30
    ROWS = 3
    COLS = 5
    def __init__(self, layout):
        super(SiteViewManager, self).__init__()
        self.site_list = []
        self.layout = layout

        self.curr_rows = SiteViewManager.ROWS
        self.curr_cols = SiteViewManager.COLS

    def addSite(self, site):
        if(site is None or not isinstance(site, SiteView)):
            raise("Must be of SiloSquareView type")

        
        self.site_list.append(site);

        site_index = len(self.site_list)-1

        col_index = site_index%SiteViewManager.COLS
        row_index = site_index//SiteViewManager.COLS
        
        self.layout.addWidget(site, row_index, col_index)


        site.show()


    def removeSite(self, index):
        
        for i in range(index+1, len(self.site_list)):
            col_index1 = (i-1)%SiteViewManager.COLS
            row_index1 = (i-1)//SiteViewManager.COLS

            col_index2 = i%SiteViewManager.COLS
            row_index2 = i//SiteViewManager.COLS


            self.layout.removeWidget(self.site_list[i])
            self.layout.addWidget(self.site_list[i], row_index2, col_index2)

            self.site_list[i-1] = self.site_list[i]


        self.site_list[len(self.site_list)-1].deleteLater()

        self.site_list.pop(len(self.site_list)-1)
        

class InputViewForSite(QMainWindow):

    def __init__(self, window):
        super(InputViewForSite, self).__init__()
        self.setupWindow()

        self.window = window

        self.setGeometry(90, 90, 400, 300)
        self.setWindowTitle('Input the site info here')
        
        self.site_name_label = QLabel("Enter Site Name", self)
        self.site_name_label.move(20,20)
        self.site_name_label.resize(120,40)
        
        self.textbox_name = QLineEdit(self)
        self.textbox_name.move(180, 20)
        self.textbox_name.resize(100, 40)

        self.button_enterHeight = QPushButton('Enter', self)
        self.button_enterHeight.move(300, 250)

        # connect button to function on_click
        self.button_enterHeight.clicked.connect(self.submit_click)

        
        
    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())
        
    @pyqtSlot()
    def submit_click(self):
        
        site = SiteName(self.textbox_name.text() )
        site_view = SiteView(site, self.window)

        self.window.widget.sm.addSite(site_view)

        self.close()
        
        
def createInputViewForSite(manager):
    inputViewForSite = InputViewForSite(manager)
    inputViewForSite.show()

    return inputViewForSite
