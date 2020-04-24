from ui.gui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen
import time
import matplotlib.pyplot as plt

from graphics import *

EPS = 10

class GuiMainWin(Ui_MainWindow):
    scene = None
    bg_color = Qt.black
    delay = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene()
        size_x = self.graphicsView.size().width()
        size_y = self.graphicsView.size().height()
        new_part = True

        self.point = False

        self.graphicsView.setSceneRect(0, 0, size_x - 4, size_y - 4)

        self.scene.setup(self.bg_color, size_x, size_y)
        self.graphicsView.setScene(self.scene)

        self.ColorLabel.setStyleSheet("QPushButton{background:#FF0000;}")
        self.ColorLabelEdges.setStyleSheet("QPushButton{background:#FFFF00;}")
        self.ChangeColor.clicked.connect(self.change_color_fill)
        self.ChangeColorEdges.clicked.connect(self.change_color_edges)
        self.LockLine.clicked.connect(self.lock_fig)
        self.CleanScreen.clicked.connect(self.scene.clean_screen)
        self.FillFig.clicked.connect(self.point_mode)
        self.Delay.valueChanged.connect(self.value_changed)
        self.AnalyzeTime.clicked.connect(self.analyze_time)

    def change_color_fill(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabel.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.scene.set_color_fill(color)

    def change_color_edges(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelEdges.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.scene.set_color_edge(color)

    def lock_fig(self):
        self.new_part = False

        self.scene.draw_line(self.scene.last_point[0], self.scene.last_point[1],
                           self.scene.first_point[0], self.scene.first_point[1])
        self.scene.display_image()
        self.scene.last_point = (None, None)
        self.scene.first_point = (None, None)
        self.scene.point_temp = None

    def filling(self, x, y):
        self.point = False
        self.scene.fill_fig(x, y, self.delay)
        self.scene.display_image()

    def point_mode(self):
        self.point = True
        '''self.scene.clean_screen() #
        self.scene.method_canonical_circle(250, 250, 100) #
        self.scene.display_image() #'''

    def transform(self, x, y):
        x -= self.graphicsView.pos().x()
        y -= self.graphicsView.pos().y()

        return x, y

    def draw_ver_hor_line(self, x, y):
        if (abs(x - self.scene.last_point[0]) < abs(y - self.scene.last_point[1])):
            x = self.scene.last_point[0]
        else:
            y = self.scene.last_point[1]
        self.draw_line(x, y)

        return x, y

    def draw_line(self, x, y):
        self.new_part = True

        if (self.scene.first_point[0] == None):
            self.scene.first_point = (x, y)
            self.scene.last_point = (x, y)
        elif (abs(x - self.scene.first_point[0]) < EPS and abs(y - self.scene.first_point[1]) < EPS):
            self.lock_fig()
        else:
            self.scene.draw_line(self.scene.last_point[0], self.scene.last_point[1], x, y)
            self.scene.last_point = (x, y)
            self.scene.display_image()

    def value_changed(self, value):
        self.delay = value

    def analyze_time(self):
        self.scene.clean_screen()
        t = []

        x, y = 2, 2
        x0, y0 = 1, 1

        while x <= 110:
            self.scene.draw_line(0, 0, x, 0)
            self.scene.draw_line(0, 0, 0, y)
            self.scene.draw_line(0, y, x, y)
            self.scene.draw_line(x, y, x, 0)

            time_start = time.time()
            self.scene.fill_fig(x0, y0, self.delay)
            t.append(time.time() - time_start)

            self.scene.clean_screen()

            x += 10
            y += 10
        print(t)

        s = [1]
        for i in range(10, 110, 10):
            s.append(i ** 2)
        print(s)

        plt.figure(figsize=(10, 6))
        plt.xlabel('Прямоугольная оболочка (количество пикселей)')
        plt.ylabel('Время (в секундах)')
        plt.title('Зависимость времени работы от площади', size=9)

        plt.plot(s, t, linewidth=1, linestyle="-", color = "blue")

        plt.show()
