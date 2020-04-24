from ui.gui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QBrush, QPen, QColor
import time
import matplotlib.pyplot as plt
import numpy as np

from graphics import *

EPS = 10

class GuiMainWin(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(Qt.black)
        self.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-1, -1, 1, 1)

        self.ColorLabel.setStyleSheet("QPushButton{background:#FF0000;}")
        self.ColorLabelEdges.setStyleSheet("QPushButton{background:#FFFF00;}")
        self.ChangeColor.clicked.connect(self.change_color)
        self.ChangeColorEdges.clicked.connect(self.change_color_edges)
        self.LockLine.clicked.connect(self.lock_fig)
        self.CleanScreen.clicked.connect(self.clean_screen)
        self.FillFig.clicked.connect(self.filling)
        self.Delay.valueChanged.connect(self.value_changed)
        self.AnalyzeTime.clicked.connect(self.analyze_time)

        self.color_fill = Qt.red
        self.color_edge = Qt.yellow
        self.pen_fill = QPen(self.color_fill)
        self.pen_edge = QPen(self.color_edge)
        self.pen_bg = QPen(Qt.black)

        self.first_point = (None, None)
        self.last_point = (None, None)
        self.edges_arr = []
        self.point_temp = None

        self.delay = 0


    def change_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabel.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.color_fill = color
        self.pen_fill = QPen(self.color_fill)

    def change_color_edges(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelEdges.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.color_edge = color
        self.pen_edge = QPen(self.color_edge)

    def clean_screen(self):
        self.scene.clear()
        self.last_point = (None, None)
        self.first_point = (None, None)
        self.point_temp = None
        self.edges_arr = []

    def prepare_to_draw(self):
        self.scene.clear()

    def lock_fig(self):
        self.scene.addLine(self.last_point[0], self.last_point[1],
                           self.first_point[0], self.first_point[1], QPen(self.color_edge))   #
        add_edge(self.edges_arr, (self.last_point[0], self.last_point[1]), (self.first_point[0], self.first_point[1]))
        self.last_point = (None, None)
        self.first_point = (None, None)
        self.point_temp = None

    def filling(self):
        self.prepare_to_draw()
        fill_fig(self.edges_arr, self.draw_pixel, self.check_color, self.delay)

    def transform(self, x, y):
        x -= self.graphicsView.pos().x()
        x -= int(self.graphicsView.size().width() / 2)

        y -= self.graphicsView.pos().y()
        y -= int(self.graphicsView.size().height() / 2)

        return x, y

    def draw_ver_hor_line(self, x, y):
        if (abs(x - self.last_point[0]) < abs(y - self.last_point[1])):
            x = self.last_point[0]
        else:
            y = self.last_point[1]
        self.draw_line(x, y)

        return x, y

    def draw_line(self, x, y):
        if (self.first_point[0] == None):
            self.first_point = (x, y)
            self.last_point = (x, y)
        elif (abs(x - self.first_point[0]) < EPS and abs(y - self.first_point[1]) < EPS):
            self.scene.addLine(self.last_point[0], self.last_point[1],
                               self.first_point[0], self.first_point[1], QPen(self.color_edge)) #
            add_edge(self.edges_arr, (self.last_point[0], self.last_point[1]), (self.first_point[0], self.first_point[1]))
            self.last_point = (None, None)
            self.first_point = (None, None)
            self.point_temp = None
        else:
            self.scene.addLine(self.last_point[0], self.last_point[1], x, y, QPen(self.color_edge))   #
            self.last_point = (x, y)

    def draw_pixel(self, x, y, flag):
        if (flag == 1):
            self.scene.addLine(x, y, x, y, self.pen_bg)
        elif (flag == 2):
            self.scene.addLine(x, y, x, y, self.pen_fill)
        else:
            self.scene.addLine(x, y, x, y, self.pen_edge)

    def check_color(self, x, y):
        return self.graphicsView.itemAt(x + 264, y + 264)

    def value_changed(self, value):
        self.delay = value

    def analyze_time(self):
        self.clean_screen()
        t = []

        x, y = 1, 1

        while x <= 110:
            add_edge(self.edges_arr, (0, 0), (x, 0))
            add_edge(self.edges_arr, (0, 0), (0, y))
            add_edge(self.edges_arr, (0, y), (x, y))
            add_edge(self.edges_arr, (x, y), (x, 0))

            time_start = time.time()
            fill_fig(self.edges_arr, self.draw_pixel, self.check_color, self.delay)
            t.append(time.time() - time_start)

            self.scene.clear()

            x += 10
            y += 10
        print(t)

        s = [1]
        for i in range(10, 110, 10):
            s.append(i ** 2)
        print(s)

        plt.figure(figsize=(10, 6))
        plt.xlabel('Прямоугольная оболочка (количество пикселей)')
        plt.ylabel('Время (в миллисекундах)')
        plt.title('Зависимость времени работы от площади', size=9)

        plt.plot(s, t, linewidth=1, linestyle="-", color = "blue")

        plt.show()
