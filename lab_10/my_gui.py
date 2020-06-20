from ui.gui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen

from math import *
from graphics import *


EPS = 1e-5
MAX_NUM = 1e5
MIN_NUM = -1e5

class GuiMainWin(Ui_MainWindow):
    bg_color = Qt.black
    func_color = QtGui.QColor('#00FFFF')

    pen_func = QPen(func_color)
    up_arr = []
    down_arr = []
    angles = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(self.bg_color)

        self.size_x = self.graphicsView.size().width()
        self.size_y = self.graphicsView.size().height()

        self.graphicsView.setSceneRect(0, 0, self.size_x - 4, self.size_y - 4)
        self.graphicsView.setScene(self.scene)

        self.Color.setStyleSheet("QPushButton{background:#00FFFF;}")

        self.ChangeColor.clicked.connect(self.change_color)

        self.DoTask.clicked.connect(self.do_task)
        self.Clean.clicked.connect(self.clean_screen)

        self.angle_ox.valueChanged.connect(self.do_task)
        self.angle_oy.valueChanged.connect(self.do_task)
        self.angle_oz.valueChanged.connect(self.do_task)

    def change_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.Color.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.set_color(color)

    def set_color(self, color):
        self.func_color = color
        self.pen_func = QPen(color)

    def draw_cut(self, x1, y1, x2, y2):
        self.scene.addLine(x1, y1, x2, y2, self.pen_func)

    def transform(self, x, y, z, data_x, data_y = (-10, 1000)): #think about it
        x, y, z = self.rotate_point([x, y, z])

        x = (x - data_x[0]) / (data_x[1] - data_x[0])
        x = 20 + x * (self.size_x - 40)

        y = (y - data_y[0]) / (data_y[1] - data_y[0])
        y = 20 + y * (self.size_y - 40)
        y = self.size_y - y

        return int(x), int(y)

    def find_min_max_y(self, data_x, data_z, f):
        x_min, x_max, x_step = data_x
        y_min, y_max = MAX_NUM, MIN_NUM
        x_min_scale, x_max_scale = MAX_NUM, MIN_NUM
        z_min, z_max, z_step = data_z

        for z in frange(z_min, z_max + 1, z_step):
            for x in frange(x_min, x_max, x_step):
                y = f(x, z)
                temp_x, y, temp_z = self.rotate_point([x, y, z])

                y_min = min(y, y_min)
                y_max = max(y, y_max)

                x_min_scale = min(x_min_scale, temp_x)
                x_max_scale = max(x_max_scale, temp_x)

        return (x_min_scale, x_max_scale), (y_min, y_max)

    def rotate_point(self, point):
        point = self.rotate_x(point)
        point = self.rotate_y(point)
        point = self.rotate_z(point)

        return point[0], point[1], point[2]

    def rotate_x(self, point):
        al = radians(self.angles[0])

        temp = point[1]
        point[1] = cos(al) * point[1] - sin(al) * point[2]
        point[2] = cos(al) * point[2] + sin(al) * temp
        return point

    def rotate_y(self, point):
        al = radians(self.angles[1])

        temp = point[0]
        point[0] = cos(al) * point[0] - sin(al) * point[2]
        point[2] = cos(al) * point[2] + sin(al) * temp
        return point

    def rotate_z(self, point):
        al = radians(self.angles[2])

        temp = point[0]
        point[0] = cos(al) * point[0] - sin(al) * point[1]
        point[1] = cos(al) * point[1] + sin(al) * temp
        return point

    def clean_screen(self):
        self.scene.clear()
        self.up_arr = []
        self.down_arr = []

    def do_task(self):
        self.clean_screen()

        x_min, x_max, x_step = float(self.XStart.text()), float(self.XEnd.text()), float(self.DX.text())
        z_min, z_max, z_step = float(self.ZStart.text()), float(self.ZEnd.text()), float(self.DZ.text())

        self.angles = self.get_angles()

        self.create_surface((x_min, x_max, x_step), (z_min, z_max, z_step), funcs(self.Funcs.currentIndex()))

    def get_angles(self):
        return (float(self.angle_ox.value()), float(self.angle_oy.value()),
                float(self.angle_oz.value()))

    def create_surface(self, data_x, data_z, f):
        data_x0, data_y = self.find_min_max_y(data_x, data_z, f)

        self.up_arr = [0] * self.size_x
        self.down_arr = [self.size_y] * self.size_x

        x_left = y_left = -1
        x_right = y_right = -1

        x_min, x_max, x_step = data_x
        z_min, z_max, z_step = data_z

        for z in frange(z_min, z_max, z_step):
            x_prev, y_prev = data_x[0], f(data_x[0], z)
            x_prev, y_prev = self.transform(x_prev, y_prev, z, data_x0, data_y)

            x_left, y_left = self.side_edge(x_prev, y_prev, x_left, y_left)
            prev_flag = self.is_visible(x_prev, y_prev)

            for x in frange(x_min, x_max, x_step):
                y = f(x, z)
                x, y = self.transform(x, y, z, data_x0, data_y)

                flag = self.is_visible(x, y)
                if (flag == prev_flag):
                    if (flag != 0):
                        self.draw_cut(x_prev, y_prev, x, y)
                        self.make_horizons(x_prev, y_prev, x, y)
                else:
                    if (flag == 0):
                        if (prev_flag == 1):
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.up_arr)
                        else:
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.down_arr)

                        self.draw_cut(x_prev, y_prev, x_cross, y_cross)
                        self.make_horizons(x_prev, y_prev, x_cross, y_cross)
                    elif (flag == 1):
                        if (prev_flag == 0):
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.up_arr)
                            self.draw_cut(x_cross, y_cross, x, y)
                            self.make_horizons(x_cross, y_cross, x, y)
                        else:
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.down_arr)
                            self.draw_cut(x_prev, y_prev, x_cross, y_cross)
                            self.make_horizons(x_prev, y_prev, x_cross, y_cross)

                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.up_arr)
                            self.draw_cut(x_cross, y_cross, x, y)
                            self.make_horizons(x_cross, y_cross, x, y)
                    else:
                        if (prev_flag == 0):
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.down_arr)
                            self.draw_cut(x, y, x_cross, y_cross)
                            self.make_horizons(x_cross, y_cross, x, y)
                        else:
                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.up_arr)
                            self.draw_cut(x_prev, y_prev, x_cross, y_cross)
                            self.make_horizons(x_prev, y_prev, x_cross, y_cross)

                            x_cross, y_cross = self.find_cross(x_prev, y_prev, x, y, self.down_arr)
                            self.draw_cut(x_cross, y_cross, x, y)
                            self.make_horizons(x_cross, y_cross, x, y)
                prev_flag = flag
                x_prev, y_prev = x, y

            x_right, y_right = self.side_edge(x, y, x_right, y_right)

    def side_edge(self, x, y, x_edge, y_edge):
        if (x_edge != -1):
            self.make_horizons(x_edge, y_edge, x, y)
            self.draw_cut(x_edge, y_edge, x, y)
        return x, y

    def make_horizons(self, x1, y1, x2, y2):
        x1, x2 = int(x1), int(x2)
        if (x1 == x2):
            self.up_arr[x2] = max(self.up_arr[x2], y2)
            self.down_arr[x2] = min(self.down_arr[x2], y2)
        else:
            k = (y2 - y1) / (x2 - x1)
            for x in range(x1, x2 + 1):
                y = k * (x - x1) + y1
                self.up_arr[x] = max(self.up_arr[x], y)
                self.down_arr[x] = min(self.down_arr[x], y)

    def is_visible(self, x, y):
        x = int(x)
        if (self.down_arr[x] < y and y < self.up_arr[x]): flag = 0
        elif (y >= self.up_arr[x]): flag = 1
        else:   flag = -1

        return flag

    def find_cross(self, x1, y1, x2, y2, hor_arr):
        x1, x2 = int(x1), int(x2)
        if (x1 == x2):
            xi, yi = x2, hor_arr[x2]
        else:
            k = (y2 - y1) / (x2 - x1)
            y_sign = sign(round(y1 + k - hor_arr[x1 + 1]))
            c_sign = y_sign
            xi, yi = x1 + 1, y1 + k

            while(c_sign == y_sign and xi < x2):
                yi += k
                xi += 1
                c_sign = sign(round(yi - hor_arr[xi]))

            if (fabs(yi - k - hor_arr[xi - 1]) <= fabs(yi - hor_arr[xi - 1])):
                yi -= k
                xi -= 1

        return xi, yi

def f1(x, z):
    return 5*x + 3*z - 7

def f2(x, z):
    return x**2 + z**2

def f3(x, z):
    return x**2 - 2*z**2

def f4(x, z):
    return sin(x * z)

def f5(x, z):
    return x ** 2 * z

def f6(x, z):
    return (x * z)**2

def funcs(ind):
    func_arr = [f1, f2, f3, f4, f5, f6]
    return func_arr[ind]

def frange(a, b, step = 1):
    arr = []
    while (a <= b + EPS):
        arr.append(a)
        a += step
    return arr

def sign(x):
    if (not x): return 0
    if (x > 0): return 1
    if (x < 0): return -1


