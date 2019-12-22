# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:46:19 2019

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


class Point(object):

    def __init__(self, x, y, is_fill):
        self.x = x
        self.y = y
        self.is_fill = is_fill

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def isFill(self):
        return self.is_fill
    def isDraw(self):
        return not self.is_fill

class SiloBase(object):

    def __init__(self, name, height):
        super(SiloBase, self).__init__()

        self.name = name;
        self.height = height;
        
        self.point_count = None
        self.point_pos = None
        self.repose_angle = None
        self.percent_error = None

        self.error_x = None
        self.error_y = None

        self.sensor_x = None
        self.sensor_y = None

        self.minimize_x = None
        self.minimize_y = None
        self.minimize_z = None

        self.plot_x = None
        self.plot_y = None
        self.plot_z = None

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setHeight(self, height):
        self.height = height
    def getHeight(self):
        return self.height
    
    def set_point_count(self, point_count):
        self.point_count = point_count
    
    def get_point_count(self):
        return self.point_count
    
    def set_point_pos(self, point_pos):
        self.point_pos = point_pos
    
    def get_point_pos(self):
        return self.point_pos
    
    def set_repose_angle(self, repose_angle):
        self.repose_angle = repose_angle
    
    def get_repose_angle(self):
        return self.repose_angle
    
    def set_percent_error(self, percent_error):
        self.percent_error = percent_error
        
    def get_percent_error(self):
        return self.percent_error

    def set_error_plot(self, x, y):
        self.error_x = x
        self.error_y = y

    def get_error_plot(self):
        return {"x": self.error_x,
                "y": self.error_y}

    def set_sensor_locale(self, x, y):
        self.sensor_x = x
        self.sensor_y = y

    def get_sensor_locale(self):
        return {"x": self.sensor_x,
                "y": self.sensor_y}

    def set_min_plot(self, x, y, z):
        self.minimize_x = x
        self.minimize_y = y
        self.minimize_z = z

    def get_min_plot(self):
        return {"x": self.minimize_x,
                "y": self.minimize_y,
                "z": self.minimize_z}

    def set_plot(self, x, y, z):
        self.plot_x = x
        self.plot_y = y
        self.plot_z = z

    def get_plot(self):
        return {"x": self.plot_x,
                "y": self.plot_y,
                "z": self.plot_z}



class SiloSquare(object):
    def __init__(self, name, height, side_len):
        super(SiloSquare, self).__init__()

        self.side_len = side_len;
        self.silo = SiloBase(name, height)

    def getSilo(self):
        return self.silo

    def setSideLen(self, side_len):
        self.side_len = side_len
    def getSideLen(self):
        return self.side_len


class SiloCircle(object):
    def __init__(self, name, height, radius):
        super(SiloCircle, self).__init__()

        self.radius = radius;
        self.silo = SiloBase(name, height)

    def getSilo(self):
        return self.silo

    def setRadius(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius

class SiloView(QWidget):
    WIDTH = 150
    HEIGHT = 150

    def __init__(self, silo, window):
        super(SiloView, self).__init__()

        self.silo = silo
        self.layout = QVBoxLayout(self)
        self.window = window

        if( isinstance(silo, SiloCircle) ):

            self.qt_button = QPushButton("Silo: %s\nheight: %d\nradius: %d"%(
                                            silo.getSilo().getName(),
                                            silo.getSilo().getHeight(),
                                            silo.getRadius()
                                        ), window)
        else:
            self.qt_button = QPushButton("Silo: %s\nheight: %d\nside length: %d"%(
                                            silo.getSilo().getName(),
                                            silo.getSilo().getHeight(),
                                            silo.getSideLen()
                                        ), window)

        



class SiloView(QWidget):
    WIDTH = 150
    HEIGHT = 150
    def __init__(self, silo, window):
        super(SiloView, self).__init__()

        self.silo = silo
        self.layout = QVBoxLayout(self)

        if( isinstance(silo, SiloCircle) ):

            self.qt_button = QPushButton("Silo: %s\nheight: %d\nradius: %d"%(
                                            silo.getSilo().getName(),
                                            silo.getSilo().getHeight(),
                                            silo.getRadius()
                                        ), window)
        else:
            self.qt_button = QPushButton("Silo: %s\nheight: %d\nside length: %d"%(
                                            silo.getSilo().getName(),
                                            silo.getSilo().getHeight(),
                                            silo.getSideLen()
                                        ), window)

        self.layout.addWidget(self.qt_button)
        self.qt_button.setFixedSize(QSize(SiloView.WIDTH, SiloView.HEIGHT))
        self.qt_button.show();
        self.show()

        self.sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)


        
        @pyqtSlot()
        def silo_handler():
            
            self.silo_screen = SiloViewCon.SiloView(self.window, self.silo)
            self.silo_screen.show()

        self.qt_button.clicked.connect(silo_handler)
        self.show()
    
    def updateModel(self, silo):
        self.qt_button.setText("Silo: %s\nheight: %d\nside length: %d"%(
                                  silo.getSilo().getName(),
                                  silo.getSilo().getHeight(),
                                  silo.getSideLen()
                                 ))

        self.qt_button.show()

    def updatePos(self,x,y):
        self.qt_button.move(x,y)
        self.qt_button.show()

    def setIndex(self,index):
        self.index = index
    def getIndex(self):
        return self.index

    def sizeHint(self):
        return QSize(SiloView.WIDTH, SiloView.HEIGHT)


        
class SiloViewManager(object):
    ROWS = 3
    COLS = 5
    SPACING = 30
    def __init__(self, layout):
        super(SiloViewManager, self).__init__()
        self.silo_list = []
        self.layout = layout

    def addSilo(self, silo):
        if(silo is None or not isinstance(silo, SiloView)):
            raise("Must be of SiloSquareView type")
        
        self.silo_list.append(silo);

        silo_index = len(self.silo_list)-1

        col_index = silo_index%SiloViewManager.COLS
        row_index = silo_index//SiloViewManager.COLS
        
        self.layout.addWidget(silo, row_index, col_index)
        

        silo.show()


    def removeSilo(self, index):
        for i in range(index+1, len(self.silo_list)):
            col_index1 = (i-1)%SiloViewManager.COLS
            row_index1 = (i-1)//SiloViewManager.COLS

            col_index2 = i%SiloViewManager.COLS
            row_index2 = i//SiloViewManager.COLS


            self.layout.removeWidget(self.silo_list[i])
            self.layout.addWidget(self.silo_list[i], row_index2, col_index2)

            self.silo_list[i-1] = self.silo_list[i]


        self.silo_list[len(self.silo_list)-1].deleteLater()

        self.silo_list.pop(len(self.silo_list)-1)



