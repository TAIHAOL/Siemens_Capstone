# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:07:01 2019

@author: Taihao Liu
"""


import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
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
import Graph
import Matlab

class PointSelection(QWidget):

    def __init__(self, silo=None):
        super(PointSelection, self).__init__()

        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout = QGridLayout(self)
        self.layout.setVerticalSpacing(0)

        self.x_labels = []
        self.y_labels = []
        self.x_lines = []
        self.y_lines = []
        self.fill_boxes = []

        self.layout.addItem(verticalSpacer, 5, 0, QtCore.Qt.AlignTop)

        if silo is not None and silo.getSilo().get_point_count() is not None:
            for i in range(silo.getSilo().get_point_count()):
                self.add_entry()
            for i in range(silo.getSilo().get_point_count()):
                self.x_lines[i].setText("%f"%silo.getSilo().get_point_pos()[i].getX())
                self.y_lines[i].setText("%f"%silo.getSilo().get_point_pos()[i].getY())
                self.fill_boxes[i].setChecked(silo.getSilo().get_point_pos()[i].isFill())


    def add_entry(self):
        x = QLineEdit(self)
        y = QLineEdit(self)
        fill_box = QCheckBox("Filled")
        x_label = QLabel("X Pos:", self)
        y_label = QLabel("Y Pos:", self)

        ind = len(self.x_labels)

        self.x_lines.append(x)
        self.y_lines.append(y)
        self.fill_boxes.append(fill_box)

        self.x_labels.append(x_label)
        self.y_labels.append(y_label)
        
        self.layout.addWidget(x_label, ind, 0)
        self.layout.addWidget(x, ind, 1)
        self.layout.addWidget(y_label, ind, 2)
        self.layout.addWidget(y, ind, 3)
        self.layout.addWidget(fill_box, ind, 4)


    def remove_entry(self):
        ind = len(self.x_labels)-1

        self.layout.removeWidget(self.x_lines[ind])
        self.layout.removeWidget(self.y_lines[ind])
        self.layout.removeWidget(self.fill_boxes[ind])
        self.layout.removeWidget(self.x_labels[ind])
        self.layout.removeWidget(self.y_labels[ind])

        self.x_lines[ind].deleteLater()
        self.x_labels[ind].deleteLater()
        self.y_labels[ind].deleteLater()
        self.y_lines[ind].deleteLater()
        self.fill_boxes[ind].deleteLater()

        self.x_lines = self.x_lines[:ind]
        self.y_lines = self.y_lines[:ind]
        self.x_labels = self.x_labels[:ind]
        self.y_labels = self.y_labels[:ind]
        self.fill_boxes = self.fill_boxes[:ind]

    def get_count(self):
        return len(self.x_labels)

    def update_silo(self, silo):
        positions = []
        for i in range(self.get_count()):
            if( self.x_lines[i].text() == ""):
                raise Exception("x position cannot be empty")
            if( self.y_lines[i].text() == ""):
                raise Exception("y position cannot be empty")

            x = float(self.x_lines[i].text())
            y = float(self.y_lines[i].text())
            fill = self.fill_boxes[i].isChecked()

            positions.append(Silo.Point(x,y, fill))

        silo.getSilo().set_point_pos(positions)



class InputSideBar(QWidget):
    def __init__(self, silo, graph):
        super(InputSideBar, self).__init__()

        self.layout = QGridLayout(self)

        self.graph = graph

        self.label_height = QLabel("The height of the silo is : " , self)
        self.label_height.move(20,20)
        self.label_height.resize(200,40)
        self.layout.addWidget(self.label_height, 0, 0)

        
        self.textbox_height = QLineEdit(self)
        self.textbox_height.move(250, 20)
        self.textbox_height.resize(100 , 40)
        self.textbox_height.setText("%d" %silo.getSilo().getHeight())
        self.textbox_height.setDisabled(True)
        self.layout.addWidget(self.textbox_height, 0, 1)
        
        
        self.label_width = QLabel("" , self)
        self.label_width.move(20,60)
        self.label_width.resize(200,40)
        self.layout.addWidget(self.label_width, 1, 0)
        
        self.textbox_width = QLineEdit(self)
        self.textbox_width.move(250, 60)
        self.textbox_width.resize(100, 40)
        self.textbox_width.setDisabled(True)
        self.layout.addWidget(self.textbox_width, 1, 1)
        
        if(isinstance(silo, Silo.SiloCircle)):
            self.label_width.setText("radius:")
            self.textbox_width.setText("%d"%silo.getRadius())
        else:
            self.label_width.setText("side len:")
            self.textbox_width.setText("%d"%silo.getSideLen())
            
            
        
        self.label_point_count = QLabel("Point Count", self)
        self.label_point_count.move(20, 220)
        self.label_point_count.resize(200,40)
        self.layout.addWidget(self.label_point_count, 2, 0)
        
        self.point_count = QComboBox(self);
        self.point_count.move(250, 220)
        self.point_count.addItem("None")
        self.point_count.addItem("1")
        self.point_count.addItem("2")
        self.point_count.addItem("3")
        self.point_count.addItem("4")
        self.point_count.addItem("5")
        if(silo.getSilo().get_point_count() is not None):
            self.point_count.setCurrentIndex(silo.getSilo().get_point_count())
        self.layout.addWidget(self.point_count, 2, 1)
        
        self.label_point_pos = QLabel('Enter your fill/draw point position', self)
        self.label_point_pos.move(20, 260)
        self.label_point_pos.resize(200,40)
        self.layout.addWidget(self.label_point_pos, 3, 0)
        

        self.points_widget = PointSelection(silo)
        self.points_widget.resize(100, 300)

        self.layout.addWidget(self.points_widget, 4, 0, 1, 3)
        
        self.label_repose_angle = QLabel("Enter the repose angle:", self)
        self.label_repose_angle.move(20, 100)
        self.label_repose_angle.resize(200,40)
        self.layout.addWidget(self.label_repose_angle, 5, 0)
        
        self.textbox_repose_angle = QLineEdit(self)
        self.textbox_repose_angle.move(250, 100)
        self.textbox_repose_angle.resize(100, 40)
        if(silo.getSilo().get_repose_angle() is not None):
            self.textbox_repose_angle.setText("%f"%silo.getSilo().get_repose_angle())
        self.layout.addWidget(self.textbox_repose_angle, 5, 1)
        
        
        self.label_percent_error = QLabel("Enter the percent error acceptable:", self)
        self.label_percent_error.move(20, 180)
        self.label_percent_error.resize(200,40)
        self.layout.addWidget(self.label_percent_error, 6, 0)
        
        self.textbox_percent_error = QLineEdit(self)
        self.textbox_percent_error.move(250, 180)
        self.textbox_percent_error.resize(100, 40)
        if(silo.getSilo().get_percent_error() is not None):
            self.textbox_percent_error.setText("%f"%silo.getSilo().get_percent_error())
        self.layout.addWidget(self.textbox_percent_error, 6, 1)

        self.calculate = QPushButton("Calculate",self)
        self.layout.addWidget(self.calculate, 7,1)

        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 7, 0, QtCore.Qt.AlignTop)

        self.silo = silo
        self.point_count.currentIndexChanged.connect(self.combo_change)
        self.calculate.clicked.connect(self.calculate_trigger)

    @pyqtSlot(int)
    def combo_change(self, value):
        old_count = self.points_widget.get_count()

        if(value == old_count):
            return
        while(value > old_count):
            self.points_widget.add_entry()
            old_count = self.points_widget.get_count()
        while(value < old_count):
            self.points_widget.remove_entry()
            old_count = self.points_widget.get_count()

    @pyqtSlot()
    def calculate_trigger(self):
        pt_cnt = self.point_count.currentIndex()
        if(pt_cnt == 0):
            raise Exception("Point count cannot be 0")
        self.silo.getSilo().set_point_count(pt_cnt)
        self.points_widget.update_silo(self.silo)
        repose = self.textbox_repose_angle.text()
        if(repose == ""):
            raise Exception("Must give repose angle")
        repose = float(repose)
        self.silo.getSilo().set_repose_angle(repose)
        error = self.textbox_percent_error.text()
        if(error == ""):
            raise Exception("Must give percent error")
        error = float(error)
        self.silo.getSilo().set_percent_error(error)

        # perform calculation
        fill_pts = []
        draw_pts = []
        for entry in self.silo.getSilo().get_point_pos():
            if entry.isFill():
                fill_pts.append([entry.getY(), entry.getX()])
            else:
                draw_pts.append([entry.getX(), entry.getX()])

        if isinstance(self.silo, Silo.SiloCircle):
            pile_struct = Matlab.pile(fill_pts, draw_pts, [self.silo.getRadius()*2, self.silo.getRadius()*2], repose)
        else:
            pile_struct = Matlab.pile(fill_pts, draw_pts, [self.silo.getSideLen(), self.silo.getSideLen()], repose)

        error_struct = Matlab.error(pile_struct["x"], pile_struct["y"], pile_struct["z"])

        self.silo.getSilo().set_plot(pile_struct["x"], pile_struct["y"], pile_struct["z"])

        self.graph.graph3d.set_mesh(pile_struct["x"], pile_struct["y"], pile_struct["z"])
        self.graph.graph3d.canvas.draw()

        red_x = []
        red_y = []
        red_z = []

        for row_i in range(len(error_struct["data"])):
            for col_i in range(len(error_struct["data"][row_i])):
                if(error_struct["map"][row_i, col_i] == 1):
                    red_x.append(pile_struct["x"][row_i, col_i])
                    red_y.append(pile_struct["y"][row_i, col_i])
                    red_z.append(error_struct["data"][row_i, col_i])

        self.silo.getSilo().set_min_plot(red_x, red_y, red_z)

        self.graph.graph3d_red.set_mesh(red_x, red_y, red_z)
        self.graph.graph3d_red.canvas.draw()
        
        self.silo.getSilo().set_sensor_locale(red_x, red_y)
        self.graph.graph_pos.set_mesh(red_x, red_y)
        self.graph.graph_pos.canvas.draw()

        error_index = []
        for i in range(len(error_struct["error_list"])):
            error_index.append(i+error_struct["start_count"])

        error_index.reverse()

        self.silo.getSilo().set_error_plot(error_index, error_struct["error_list"])
        self.graph.graph_error.set_mesh(error_index, error_struct["error_list"])
        self.graph.graph_error.canvas.draw()
                
        

        

        




        pass


class GraphSection(QWidget):
    def __init__(self, silo):
        super(GraphSection, self).__init__()
        self.layout = QGridLayout(self)
        
        self.graph3d = Graph.widget(self)
        self.graph3d_red = Graph.widget_semi(self)
        self.graph_pos = Graph.widget_top(self)
        self.graph_error = Graph.widget_error(self)
        
        if(silo.getSilo().get_plot()["x"] is not None):
            self.graph3d.set_mesh(silo.getSilo().get_plot()["x"], silo.getSilo().get_plot()["y"], silo.getSilo().get_plot()["z"])
            self.graph3d_red.set_mesh(silo.getSilo().get_min_plot()["x"], silo.getSilo().get_min_plot()["y"],
                                      silo.getSilo().get_min_plot()["z"])
            self.graph_pos.set_mesh(silo.getSilo().get_sensor_locale()["x"], silo.getSilo().get_sensor_locale()["y"])
            self.graph_error.set_mesh(silo.getSilo().get_error_plot()["x"], silo.getSilo().get_error_plot()["y"])
        
        
        self.layout.addWidget(self.graph3d, 0, 0)
        self.layout.addWidget(self.graph3d_red, 0, 1)
        self.layout.addWidget(self.graph_pos, 1, 0)
        self.layout.addWidget(self.graph_error, 1, 1)

        self.graph3d.show()
        self.graph3d.canvas.draw()

        self.graph3d_red.show()
        self.graph3d_red.canvas.draw()

        self.graph_pos.show()
        self.graph_pos.canvas.draw()

        self.graph_error.show()
        self.graph_error.canvas.draw()



class SiloView(QScrollArea):#(QMainWindow):

    def __init__(self, window, silo):
        self.temp = []

        super(SiloView, self).__init__()
        self.setupWindow()

        self.window = window

        self.setGeometry(90, 90, 800, 600)
        self.setWindowTitle('Silo: %s'%silo.getSilo().getName())

        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.graph_section = GraphSection(silo)
        self.graph_section.resize(1000, 1000)
        
        self.input_side_widget = InputSideBar(silo, self.graph_section)

        self.layout.addWidget(self.input_side_widget, 0, 0)


        self.layout.addWidget(self.graph_section, 0, 1)
            
        self.button_clear = QPushButton('Clear all', self)
        self.button_clear.move(700, 500)
        self.layout.addWidget(self.button_clear, 2, 2)

        self.button_enter = QPushButton('Enter', self)
        self.button_enter.move(700, 550)
        self.layout.addWidget(self.button_enter, 2, 3)

        
        self.show()

        self.setWidget(self.widget)
        self.setWidgetResizable(True)
        
        

        
    def setupWindow(self):
        frameGeo = self.frameGeometry()
        geoCenter = QDesktopWidget().availableGeometry().center()
        frameGeo.moveCenter(geoCenter)
        self.move(frameGeo.topLeft())
        





def createSiloView(window, silo):
    siloView = SiloView(window, silo)
    siloView.show()

    return siloView
