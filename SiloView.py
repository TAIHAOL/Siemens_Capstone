# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:07:01 2019

@author: Taihao Liu
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
from PyQt5.QtWidgets import QComboBox

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


import Silo

class SiloView(QMainWindow):

    def __init__(self, window, silo):
        self.temp = []
        super(SiloView, self).__init__()
        self.setupWindow()

        self.window = window

        self.setGeometry(90, 90, 800, 600)
        self.setWindowTitle('Silo: %s'%silo.getSilo().getName())

        self.label_height = QLabel("The height of the silo is : " , self)
        self.label_height.move(20,20)
        self.label_height.resize(200,40)
        
        self.textbox_height = QLineEdit(self)
        self.textbox_height.move(250, 20)
        self.textbox_height.resize(100 , 40)
        self.textbox_height.setText("%d" %silo.getSilo().getHeight())
        
        
        self.label_width = QLabel("" , self)
        self.label_width.move(20,60)
        self.label_width.resize(200,40)
        
        self.textbox_width = QLineEdit(self)
        self.textbox_width.move(250, 60)
        self.textbox_width.resize(100, 40)
        
        if(isinstance(silo, Silo.SiloCircle)):
            self.label_width.setText("radius:")
            self.textbox_width.setText("%d"%silo.getHeight())
        else:
            self.label_width.setText("side len:")
            self.textbox_width.setText("%d"%silo.getSideLen())
            
            
        self.label_draw_fill = QLabel('Fill or Draw', self)
        self.label_draw_fill.move(20, 140)
        self.label_draw_fill.resize(200,40)
        
        self.fill_draw = QComboBox(self);
        self.fill_draw.move(250, 140)
        self.fill_draw.addItem("Fill")
        self.fill_draw.addItem("Draw")
               
        
        
        self.label_point_count = QLabel("Point Count", self)
        self.label_point_count.move(20, 220)
        self.label_point_count.resize(200,40)
        
        self.point_count = QComboBox(self);
        self.point_count.move(250, 220)
        self.point_count.addItem("None")
        self.point_count.addItem("1")
        self.point_count.addItem("2")
        self.point_count.addItem("3")
        self.point_count.addItem("4")
        self.point_count.addItem("5")
        
        
        
        
#        if(silo.getSilo().get_point_count() is None):
#            self.textbox_point_count.setText("")
#        else:
#            self.textbox_point_count.setText("%d"%silo.getSilo().get_point_count())
            
        self.label_point_pos = QLabel('Enter your fill/draw point position', self)
        self.label_point_pos.move(20, 260)
        self.label_point_pos.resize(200,40)
        
        self.textbox_point_pos = []
        
        
        
        """
        if(silo.getSilo().get_point_pos() is None):
            self.textbox_point_pos.setText("")
        else:
            self.textbox_point_pos.setText("%d"%silo.getSilo().get_point_pos())
        """
        
        self.label_repose_angle = QLabel("Enter the repose angle:", self)
        self.label_repose_angle.move(20, 100)
        self.label_repose_angle.resize(200,40)
        
        self.textbox_repose_angle = QLineEdit(self)
        self.textbox_repose_angle.move(250, 100)
        self.textbox_repose_angle.resize(100, 40)
        
        
        self.label_percent_error = QLabel("Enter the percent error acceptable:", self)
        self.label_percent_error.move(20, 180)
        self.label_percent_error.resize(200,40)
        
        self.textbox_percent_error = QLineEdit(self)
        self.textbox_percent_error.move(250, 180)
        self.textbox_percent_error.resize(100, 40)
    
            
        self.button_clear = QPushButton('Clear all', self)
        self.button_clear.move(700, 500)

        self.button_enter = QPushButton('Enter', self)
        self.button_enter.move(700, 550)
        
        self.point_count.currentIndexChanged.connect(self.combo_change)

        self.show()

    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())
        
    @pyqtSlot(int)
    def combo_change(self, value):
        for i in self.temp:
            self.textbox_point_pos[i].close()
        self.temp =[]
        if(value == 0):
            self.textbox_point_pos = []
            self.textbox_point_pos.clear()
        else:
            del self.textbox_point_pos[:len(self.textbox_point_pos)]
            
            for i in range(value):
                self.textbox_point_pos.append(QLineEdit(self))
                self.textbox_point_pos[2*i].move(250, 260 + 40*i)
                self.textbox_point_pos[2*i].resize(100, 40)
                
                self.textbox_point_pos.append(QLineEdit(self))
                self.textbox_point_pos[2*i+1].move( 400 , 260 + 40*i)
                self.textbox_point_pos[2*i+1].resize(100, 40)
                
                
                self.textbox_point_pos[2*i].show()
                self.textbox_point_pos[2*i+1].show()
                print("in function", 2*i)
                print("in function", 2*i+1)
                self.temp.append(2*i)
                self.temp.append(2*i+1)
      
        print(len(self.textbox_point_pos))
        print(self.textbox_point_pos)





def createInputView(window, silo):
    siloView = SiloView(window, silo)
    siloView.show()

    return siloView
