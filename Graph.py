# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:45:46 2019

@author: asp5423
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys
import random
#fig = plt.figure()


#plt.show()

class widget_error(QtWidgets.QWidget):
    def __init__(self, parent=None, x=None, y=None):
        super(widget_error, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.ax = self.figure.add_subplot(111)
        
        if x is None and y is None:
            x = np.array([i for i in range(1, 100)])
            y = 0.3 * np.exp(x/35.0)

            for i in range(len(y)):
                y[i] *= 1 - random.random()*0.1
        elif x is None or y is None:
            raise Exception("both x and y parameters must be specified")

        self.ax.set_title("% Error With Reduced Sensors")
        self.ax.set_xlabel("Number of Points Removed")
        self.ax.set_ylabel("% Error")

        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)



    def set_mesh(self, x, y):
        self.ax.cla()
        self.ax.set_title("% Error With Reduced Sensors")
        self.ax.set_xlabel("Number of Points Removed")
        self.ax.set_ylabel("% Error")
        self.ax.plot(x,y)

    def clear_mesh(self):
        self.ax.cla()
        self.ax.set_title("% Error With Reduced Sensors")
        self.ax.set_xlabel("Number of Points Removed")
        self.ax.set_ylabel("% Error")
        

    def sizeHint(self):
        return QSize(500, 500)

class widget_top(QtWidgets.QWidget):
    def __init__(self, parent=None, x=None, y=None):
        super(widget_top, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Positions of Significant Sensors")
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")

        if x is None and y is None:
            x = np.array([0, 5, 5, 9])
            y = np.array([5, 5, 9, 0])
        elif x is None or y is None:
            raise Exception("both x and y parameters must be specified")

        #self.ax.scatter(x,y)

        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)


    def set_mesh(self, x,y):
        self.ax.cla()
        self.ax.set_title("Positions of Significant Sensors")
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")
        self.ax.scatter(x,y)
    def clear_mesh(self):
        self.ax.cla()
        self.ax.set_title("Positions of Significant Sensors")
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")

    def sizeHint(self):
        return QSize(500, 500)


class widget_semi(QtWidgets.QWidget): # 3d plot partial
    
    def __init__(self, parent=None, x=None, y=None, z=None):
        super(widget_semi, self).__init__(parent)
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        self.ax = self.figure.add_subplot(111, projection='3d')
        
        if x is None and y is None and z is None:
            x = np.array([0,  5,  5, 9])
            y = np.array([0,  5,  9, 0])
            z = 70 -(x-5)**2 - (x-5)**2

        elif x is None or y is None or z is None:
            raise Exception("x, y, and z parameters must all be specified")
        
        
        self.ax.set_title("Mesh Shape Using Minimized Sensors")
        
        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)
        
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)



    def set_mesh(self, x,y,z):
        self.ax.cla()
        self.ax.set_title("Mesh Shape Using Minimized Sensors")
        self.ax.plot_trisurf(x,y,z,color="black", edgecolor='white')
    def clear_mesh(self):
        self.ax.cla()
        self.ax.set_title("Mesh Shape Using Minimized Sensors")

    def sizeHint(self):
        return QSize(500, 500)

class widget(QtWidgets.QWidget): # 3d plot full
    
    def __init__(self, parent=None, X=None, Y=None, z=None):
        super(widget, self).__init__(parent)
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        self.ax = self.figure.add_subplot(111, projection='3d')

        
        if X is None and Y is None and z is None:
            x = np.linspace(0, 10, 11)
            y = np.linspace(0, 10, 11)
            
            X,Y = np.meshgrid(x,y)
            z = 70  -(X-5)**2 - (Y-5)**2

            for i in range(z.shape[0]):
                for j in range(z.shape[1]):
                    z[i,j] *= 1 + 2*(random.random()-0.5)*0.03
        elif X is None or Y is None or z is None:
            print(X)
            raise Exception("X, Y, and z parameters must all be specified")

        
        

        self.ax.set_title("Expected Mesh Shape")
        
        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(self.sizePolicy)
        
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)


    def set_mesh(self, x,y,z):
        self.ax.cla()
        self.ax.set_title("Expected Mesh Shape")
        self.ax.plot_surface(x,y,z, cmap='viridis')
    def clear_mesh(self):
        self.ax.cla()
        self.ax.set_title("Expected Mesh Shape")
                     
    def sizeHint(self):
        return QSize(500, 500)

def createGraph2():
    app = QtWidgets.QApplication(ss.argv)

    w = widget_semi()
    w.show()
    w.canvas.draw()

def createGraph():
    app = QtWidgets.QApplication(sys.argv)
#    app.setApplicationName("hello there")
        
    w = widget()
    w.show()
    w.canvas.draw()
        
        

