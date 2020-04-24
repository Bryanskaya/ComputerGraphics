from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QImage, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QThread
from math import *

FILL   = 1
FIG  = 2
EDGE = 3

class Stack(object):
    points_list = list()

    def push(self, x, y):
        self.points_list.append((x, y))

    def pop(self):
        return self.points_list.pop()

    def is_empty(self):
        return len(self.points_list) == 0


class MyScene(QtWidgets.QGraphicsScene):
    color_fill = Qt.red
    color_edge = Qt.yellow

    pen_fill = QPen(color_fill)
    pen_edge = QPen(color_edge)

    first_point = (None, None)
    last_point = (None, None)
    point_temp = None

    x_min, y_min = 0, 0

    delay = 0

    image = QImage()

    def setup(self, color_bg, x_size, y_size):
        self.image_size = (x_size, y_size)
        self.x_max, self.y_max = x_size - 1, y_size - 1

        self.color_bg = color_bg
        self.setBackgroundBrush(QBrush(color_bg))

        self.image = QImage(self.image_size[0], self.image_size[1],
                            QImage.Format_RGB32)

        self.display_image()

    def set_color_fill(self, color):
        self.color_fill = color
        self.pen_fill = QPen(self.color_fill)

    def set_color_edge(self, color):
        self.color_edge = color
        self.pen_edge = QPen(self.color_edge)

    def draw_line(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        if (abs(dx) > abs(dy)):
            num = abs(dx)
        else:
            num = abs(dy)
        dx = dx / num
        dy = dy / num

        x, y = x1, y1

        for i in range(1, round(num) + 2):
            self.draw_pixel(round(x), round(y), False)
            x += dx
            y += dy

    def draw_pixel(self, x, y, flag):
        if (flag):
            self.image.setPixel(x, y, QColor(self.color_fill).rgba())
        else:
            self.image.setPixel(x, y, QColor(self.color_edge).rgba())

    def is_border(self, x, y):
        return self.image.pixel(x, y) == QColor(self.color_edge).rgba()

    def is_fill(self, x, y):
        return self.image.pixel(x, y) == QColor(self.color_fill).rgba()

    def clean_screen(self):
        self.clear()
        self.last_point = (None, None)
        self.first_point = (None, None)
        self.point_temp = None

        self.image = QImage(self.image_size[0], self.image_size[1],
                            QImage.Format_RGB32)

    def display_image(self):
        self.clear()

        pixmap = QtGui.QPixmap()
        pixmap = pixmap.fromImage(self.image)
        self.addPixmap(pixmap)

    def fill_fig(self, x, y, delay):
        stack = Stack()
        stack.push(x, y)

        while (not stack.is_empty()):
            x, y = stack.pop()
            self.draw_pixel(x, y, FILL)

            x_right = self.fill_right_line(x + 1, y)
            x_left = self.fill_left_line(x - 1, y)

            self.fill_neighbour_lines(stack, x_left, y + 1, x_right)
            self.fill_neighbour_lines(stack, x_left, y - 1, x_right)

            if (delay):
                QtWidgets.QApplication.processEvents()
                QThread.msleep(delay)

                self.display_image()

    def fill_right_line(self, x, y):
        while (not self.is_border(x, y) and x < self.x_max):
            self.draw_pixel(x, y, FILL)
            x += 1
        return x - 1

    def fill_left_line(self, x, y):
        while (not self.is_border(x, y) and x > self.x_min):
            self.draw_pixel(x, y, FILL)
            x -= 1
        return x + 1

    def fill_neighbour_lines(self, stack, x, y, x_right):
        if (not self.y_min <= y <= self.y_max): return

        while (x <= x_right):
            flag = 0
            while (not self.is_border(x, y) and not self.is_fill(x, y) \
                    and x <= x_right):
                if (not flag): flag = 1
                x += 1

            if (flag):
                if (x == x_right and not self.is_border(x, y) and \
                     not self.is_fill(x, y)):
                    stack.push(x, y)
                else:
                    stack.push(x - 1, y)

            temp_x = x
            while ((self.is_border(x, y) or self.is_fill(x, y)) and x < x_right):
                x += 1

            if (x == temp_x): x += 1

    def method_canonical_circle(self, x_center, y_center, r):
        r2 = r ** 2
        x = 0
        x_temp = round(r / sqrt(2))

        while x <= x_temp:
            y = sqrt(r2 - x ** 2)

            self.draw_pixel(x + x_center, y + y_center, 0)
            self.draw_pixel(x + x_center, -y + y_center, 0)
            self.draw_pixel(-x + x_center, y + y_center, 0)
            self.draw_pixel(-x + x_center, -y + y_center, 0)

            self.draw_pixel(y + x_center, x + y_center, 0)
            self.draw_pixel(y + x_center, -x + y_center, 0)
            self.draw_pixel(-y + x_center, x + y_center, 0)
            self.draw_pixel(-y + x_center, -x + y_center, 0)

            x += 1
