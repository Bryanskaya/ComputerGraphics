from ui.gui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen

from math import *
from graphics import *


EPS = 10

class GuiMainWin(Ui_MainWindow):
    bg_color = Qt.black
    fig_color = QtGui.QColor('#FF0000')
    cut_color = QtGui.QColor('#0C69FF')
    task_color = QtGui.QColor('#00FF00')

    pen_fig = QPen(fig_color)
    pen_cut = QPen(cut_color)
    pen_task = QPen(task_color)

    is_figure = True
    count_cut = 0
    first_point, last_point = None, None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(self.bg_color)

        self.size_x = self.graphicsView.size().width()
        self.size_y = self.graphicsView.size().height()

        self.graphicsView.setSceneRect(0, 0, self.size_x - 4, self.size_y - 4)
        self.graphicsView.setScene(self.scene)

        self.ColorLabelRect.setStyleSheet("QPushButton{background:#FF0000;}")
        self.ColorLabelCut.setStyleSheet("QPushButton{background:#0C69FF;}")
        self.ColorLabelTask.setStyleSheet("QPushButton{background:#00FF00;}")

        self.ChangeColorFig.clicked.connect(self.change_color_fig)
        self.ChangeColorCut.clicked.connect(self.change_color_cut)
        self.ChangeColorTask.clicked.connect(self.change_color_task)

        self.LockLine.clicked.connect(self.lock_fig)

        self.DoTask.clicked.connect(self.clipping_cuts)
        self.Clean.clicked.connect(self.clean_screen)

        self.edges_arr = []
        self.cuts_arr = []
        self.n = []

    def change_color_fig(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ColorLabelRect.setStyleSheet("QPushButton{background:" + color.name() + ";}")
        self.set_color_fig(color)

    def set_color_fig(self, color):
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
        y = -y + self.graphicsView.size().height()

        return x, y

    def draw_line(self, x, y, flag):
        if (self.is_figure):
            if (self.first_point == None):
                self.first_point = (x, y)
                self.last_point = (x, y)
            else:
                if (abs(x - self.first_point[0]) < EPS and abs(y - self.first_point[1]) < EPS):
                    x, y = self.first_point[0], self.first_point[1]
                    self.is_figure = False

                if (flag):
                    if (abs(x - self.last_point[0]) < abs(y - self.last_point[1])):
                        x = self.last_point[0]
                    else:
                        y = self.last_point[1]

                self.scene.addLine(self.last_point[0], -self.last_point[1] + self.size_y,
                                   x, -y + self.size_y, self.pen_fig)

                add_edge(self.edges_arr, self.last_point, (x, y))

                if (self.is_figure):    self.last_point = (x, y)
                else:   self.first_point, self.last_point = None, None
        else:
            if (self.count_cut >= 10): return

            if (self.first_point == None):
                self.first_point = (x, y)
            else:
                self.count_cut += 1

                if (flag):
                    if (abs(x - self.first_point[0]) < abs(y - self.first_point[1])):
                        x = self.first_point[0]
                    else:
                        y = self.first_point[1]

                self.scene.addLine(self.first_point[0], -self.first_point[1] + self.size_y,
                                   x, -y + self.size_y, self.pen_cut)

                add_edge(self.cuts_arr, self.first_point, (x, y))
                self.first_point = None

    def draw_cut(self, t1, t2, D, P1):
        print(t1, t2)
        point1 = self.points_sum(P1, self.vect_num_mul(D, t1))
        point2 = self.points_sum(P1, self.vect_num_mul(D, t2))

        self.scene.addLine(point1[0], -point1[1] + self.size_y,
                           point2[0], -point2[1] + self.size_y, self.pen_task)

    def lock_fig(self):
        x, y = self.first_point[0], self.first_point[1]
        self.scene.addLine(self.last_point[0],
                           -self.last_point[1] + self.graphicsView.size().height(),
                           x, -y + self.graphicsView.size().height(), self.pen_fig)

        add_edge(self.edges_arr, self.last_point, (x, y))

        self.is_figure = False
        self.first_point, self.last_point = None, None

    def clean_screen(self):
        self.scene.clear()
        self.is_figure = True
        self.first_point, self.last_point = None, None
        self.count_cut = 0
        self.edges_arr = []
        self.cuts_arr = []
        self.n = []

    def clipping_cuts(self):
        flag = self.is_convex_polygon()
        if not flag: return
        self.find_normal(flag == -1)

        for cut in self.cuts_arr:
            P1 = Point(cut.x1, cut.y1)
            P2 = Point(cut.x2, cut.y2)

            self.clipping_cut(P1, P2)

    def clipping_cut(self, P1, P2):
        t_down, t_up = 0, 1
        D = self.points_sub(P2, P1)

        for i in range(len(self.edges_arr)):
            fi = Point(self.edges_arr[i].x1, self.edges_arr[i].y1)
            wi = self.points_sub(P1, fi)

            D_sc = self.scalar_mul(self.n[i], D)
            W_sc = self.scalar_mul(self.n[i], wi)
            print("D_sc, W_sc", D_sc, W_sc)

            if (not D_sc):
                if (W_sc < 0):  return
                continue

            t = - W_sc / D_sc

            if (D_sc > 0):
                if (t > 1):     return
                t_down = max(t, t_down)
            else:
                if (t < 0):     return
                t_up = min(t, t_up)

        if (t_down <= t_up): self.draw_cut(t_down, t_up, D, P1)

    def is_convex_polygon(self):
        is_neg, is_pos, is_zero = False, False, False

        for i in range(len(self.edges_arr)):
            vect_mul = self.vector_mul(self.edges_arr[(i + 1) % len(self.edges_arr)], self.edges_arr[i])
            if (vect_mul < 0):  is_neg = True
            elif (vect_mul > 0):    is_pos = True
            else:   is_zero = True

        if (((is_neg and not is_pos) or (is_pos and not is_neg)) and not is_zero): return copysign(1, vect_mul)
        else:   return False

    def find_normal(self, is_invert):
        for i in range(len(self.edges_arr)):
            n_temp = Vector(self.edges_arr[i].y2 - self.edges_arr[i].y1,
                            self.edges_arr[i].x1 - self.edges_arr[i].x2)

            if (is_invert):
                n_temp = self.vect_num_mul(n_temp, -1)
            self.n.append(n_temp)

    def vector_mul(self, vector1, vector2):
        return vector1.x * vector2.y - vector2.x * vector1.y

    def vect_num_mul(self, vector, num):
        return Point(vector.x * num, vector.y * num)

    def points_sub(self, point1, point2):
        return Vector(point1.x - point2.x, point1.y - point2.y)

    def points_sum(self, point1, point2):
        return point1.x + point2.x, point1.y + point2.y

    '''def swap_ends(self, edge):
        x1, y1 = edge.x2, edge.y2
        x2, y2 = edge.x1, edge.y1

        return Edge((x1, y1), (x2, y2))'''

    def scalar_mul(self, vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y