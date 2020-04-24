from ui.gui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen

from graphics import *

class GuiMainWin(Ui_MainWindow):
    bg_color = Qt.black
    rect_color = QtGui.QColor('#FF0000')
    cut_color = QtGui.QColor('#0C69FF')
    task_color = QtGui.QColor('#00FF00')

    pen_rect = QPen(rect_color)
    pen_cut = QPen(cut_color)
    pen_task = QPen(task_color)

    x_left, x_right = None, None
    y_down, y_up = None, None

    temp_point = None

    cuts_arr = []
    I, flag = 0, 0
    R1, R2 = None, None
    P1, P2 = None, None
    Pt = None
    m = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(self.bg_color)

        size_x = self.graphicsView.size().width()
        size_y = self.graphicsView.size().height()

        self.rect = True
        self.count_cut = 0

        self.graphicsView.setSceneRect(0, 0, size_x - 4, size_y - 4)
        self.graphicsView.setScene(self.scene)

        self.ColorLabelRect.setStyleSheet("QPushButton{background:#FF0000;}")
        self.ColorLabelCut.setStyleSheet("QPushButton{background:#0C69FF;}")
        self.ColorLabelTask.setStyleSheet("QPushButton{background:#00FF00;}")

        self.ChangeColorRect.clicked.connect(self.change_color_rect)
        self.ChangeColorCut.clicked.connect(self.change_color_cut)
        self.ChangeColorTask.clicked.connect(self.change_color_task)
        self.PushRect.clicked.connect(self.entry_rect)
        self.DoTask.clicked.connect(self.simple_clipping)
        self.Clean.clicked.connect(self.clean_screen)

    def change_color_rect(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelRect.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.set_color_rect(color)

    def set_color_rect(self, color):
        self.rect_color = color
        self.pen_rect = QPen(color)

    def change_color_cut(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelCut.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.set_color_cut(color)

    def set_color_cut(self, color):
        self.cut_color = color
        self.pen_cut = QPen(color)

    def change_color_task(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelTask.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.set_color_task(color)

    def set_color_task(self, color):
        self.task_color = color
        self.pen_task = QPen(color)

    def transform(self, x, y):
        x -= self.graphicsView.pos().x()
        if not(0 <= x <= self.graphicsView.size().width()):
            return None

        y -= self.graphicsView.pos().y()
        if not(0 <= y <= self.graphicsView.size().height()):
            return None
        print('*', x, y)
        y = -y + self.graphicsView.size().height() #5656

        return x, y

    def entry_rect(self):
        if (self.rect):
            x1, y1 = int(self.EntryX1.text()), int(self.EntryY1.text())
            x2, y2 = int(self.EntryX2.text()), int(self.EntryY2.text())

            self.draw_rect(x1, y1)
            self.draw_rect(x2, y2)

    def draw_rect(self, x, y):
        if (self.rect == True):
            self.x_left, self.y_down = x, y
            self.rect = 2
        elif (self.rect == 2):
            if (self.x_left == x or self.y_down == y): return

            if (self.x_left > x): self.x_right, self.x_left = self.x_left, x
            else: self.x_right = x

            if (self.y_down > y):self.y_up, self.y_down = self.y_down, y
            else: self.y_up = y

            self.scene.addRect(self.x_left, -self.y_up + self.graphicsView.size().height(),
                               self.x_right - self.x_left,
                               abs(self.y_up - self.y_down), self.pen_rect)
            self.rect = False

    def draw_line(self, x, y):
        if (self.temp_point == None):
            self.temp_point = (x, y)
        else:
            if (self.temp_point[0] == x and self.temp_point[1] == y):
                return

            self.scene.addLine(self.temp_point[0], -self.temp_point[1] + self.graphicsView.size().height(),
                               x, -y + self.graphicsView.size().height(), self.pen_cut)
            self.count_cut += 1
            add_cut(self.cuts_arr, self.temp_point, (x, y))

            self.temp_point = None

    def draw_ver_hor_line(self, x, y):
        if (self.temp_point):
            if (abs(x - self.temp_point[0]) < abs(y - self.temp_point[1])):
                x = self.temp_point[0]
            else:
                y = self.temp_point[1]
        self.draw_line(x, y)

    def clean_screen(self):
        self.scene.clear()
        self.rect = True
        self.x_left, self.x_right = None, None
        self.y_down, self.y_up = None, None
        self.count_cut = 0
        self.temp_point = None
        self.cuts_arr = []

    def draw_result(self, point_1, point_2):
        if (not self.flag):
            self.scene.addLine(point_1[0], -point_1[1] + self.graphicsView.size().height(),
                               point_2[0], -point_2[1] + self.graphicsView.size().height(),
                               self.pen_task)

    def simple_clipping(self):
        for i in range(len(self.cuts_arr)):
            self.P1 = (self.cuts_arr[i].x1, self.cuts_arr[i].y1)
            self.P2 = (self.cuts_arr[i].x2, self.cuts_arr[i].y2)

            code_1 = self.find_code(self.P1[0], self.P1[1])
            code_2 = self.find_code(self.P2[0], self.P2[1])

            self.flag = 0
            self.R1 = self.P1
            self.R2 = self.P2
            self.m = 1e30

            s1, s2 = self.find_sum(code_1), self.find_sum(code_2)

            if (not s1 and not s2):
                self.draw_result(self.R1, self.R2)

            if (self.logic_and(code_1, code_2)):
                self.flag = -1
                continue

            if (not s1):
                self.I = 2
                self.R1 = self.P1
                self.Pt = self.P2
                self.check_left_cross()
            if (not s2):
                self.I = 2
                self.R1 = self.P2
                self.Pt = self.P1
                self.check_left_cross()

            self.I = 0
            self.next_point()

    def find_code(self, x, y):
        code = [0] * 4
        if (x < self.x_left): code[0] = 1
        if (x > self.x_right): code[1] = 1
        if (y < self.y_down): code[2] = 1
        if (y > self.y_up): code[3] = 1
        return code

    def find_sum(self, code):
        s = 0
        for i in range(len(code)):
            s += code[i]
        return s

    def logic_and(self, code_1, code_2):
        s = 0
        for i in range(len(code_1)):
            s += code_1[i] * code_2[i]
        return s

    def check_left_cross(self):
        if (self.P2[0] == self.P1[0]): self.check_up_cross()
        else:
            self.m = (self.P2[1] - self.P1[1]) / (self.P2[0] - self.P1[0])

            if (self.x_left < self.Pt[0]):  self.check_right_cross()
            else:
                y = self.m * (self.x_left - self.Pt[0]) + self.Pt[1]

                if (y > self.y_up or y < self.y_down): self.check_right_cross()
                else:
                    self.Pt = (self.x_left, y)

                    self.next_point()

    def check_right_cross(self):
        if (self.x_right > self.Pt[0]): self.check_up_cross()
        else:
            y = self.m * (self.x_right - self.Pt[0]) + self.Pt[1]

            if (y > self.y_up or y < self.y_down): self.check_up_cross()
            else:
                self.Pt = (self.x_right, y)

                self.next_point()

    def check_up_cross(self):
        if (self.m == 0):   self.next_point()
        else:
            if (self.y_up > self.Pt[1]): self.check_down_cross()
            else:
                x = self.Pt[0] + (self.y_up - self.Pt[1]) / self.m

                if (x < self.x_left or x > self.x_right): self.check_down_cross()
                else:
                    self.Pt = (x, self.y_up)

                    self.next_point()

    def check_down_cross(self):
        if (self.y_down < self.Pt[1]):  return
        x = self.Pt[0] + (self.y_down - self.Pt[1]) / self.m

        if (x < self.x_left or x > self.x_right):
            self.flag = -1
            return
        else:
            self.Pt = (x, self.y_down)

            self.next_point()

    def next_point(self):
        if (self.I):
            if (self.I == 1): self.R1 = self.Pt
            else: self.R2 = self.Pt

        self.I += 1
        if (self.I > 2):
            self.draw_result(self.R1, self.R2)
        else:
            if (self.I == 1): self.Pt = self.P1
            else: self.Pt = self.P2

            self.check_left_cross()