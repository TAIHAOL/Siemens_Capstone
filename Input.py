# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

class InputView(QMainWindow):

    def __init__(self, window):
        super(InputView, self).__init__()
        self.setupWindow()

        self.window = window


        self.setGeometry(90, 90, 400, 300)
        self.setWindowTitle('Input the data here')

        self.label_silo_type = QLabel("Select Silo Type", self)
        self.label_silo_type.move(20,20)
        self.label_silo_type.resize(120,40)



        self.label_name = QLabel("Enter your Name", self)
        self.label_name.move(20,60)
        self.label_name.resize(120,40)

        self.label_height = QLabel('Enter your Height', self)
        self.label_height.move(20, 100)
        self.label_height.resize(120,40)

        self.label_radius = QLabel('Enter your Radius', self)
        self.label_radius.move(20, 140)
        self.label_radius.resize(120,40)

        self.silo_type = QComboBox(self);
        self.silo_type.move(180, 20)
        self.silo_type.addItem("Circular")
        self.silo_type.addItem("Rectangular")

        self.textbox_name = QLineEdit(self)
        self.textbox_name.move(180, 60)
        self.textbox_name.resize(100, 40)

        self.textbox_height = QLineEdit(self)
        self.textbox_height.move(180, 100)
        self.textbox_height.resize(100, 40)

        self.textbox_radius = QLineEdit(self)
        self.textbox_radius.move(180, 140)
        self.textbox_radius.resize(100, 40)

        self.button_clear = QPushButton('Clear all', self)
        self.button_clear.move(300, 200)

        self.button_enterHeight = QPushButton('Enter', self)
        self.button_enterHeight.move(300, 250)

        # connect button to function on_click
        self.button_clear.clicked.connect(self.clear_click)
        self.button_enterHeight.clicked.connect(self.submit_click)
        self.silo_type.currentIndexChanged.connect(self.combo_change)

        self.show()

    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())

    @pyqtSlot()
    def clear_click(self):
        self.textbox_radius.clear()
        self.textbox_height.clear()
        self.textbox_name.clear()

    @pyqtSlot()
    def submit_click(self):
        if(self.silo_type.currentIndex() == 0):
            silo = Silo.SiloCircle(self.textbox_name.text(), 
                                   int(self.textbox_height.text()),
                                   int(self.textbox_radius.text()))
        else:
            silo = Silo.SiloSquare(self.textbox_name.text(), 
                                   int(self.textbox_height.text()),
                                   int(self.textbox_radius.text()))

        silo_view = Silo.SiloView(silo, self.window)

        self.window.widget.sm.addSilo(silo_view)

        self.close()

    @pyqtSlot(int)
    def combo_change(self, value):
        if(value == 0):
            self.label_radius.setText("Enter your Radius")
        else:
            self.label_radius.setText("Enter your Side Length")

        self.clear_click()



def createInputView(manager):
    inputView = InputView(manager)
    inputView.show()

    return inputView
