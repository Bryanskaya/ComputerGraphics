from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt,  QThread
from PyQt5.QtGui import QBrush, QPen, QColor

BG   = 1
FIG  = 2
EDGE = 3
EPS  = 1e-3

class Edge(object):
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    def __init__(self, point_1, point_2):
        self.x1, self.y1 = point_1[0], point_1[1]
        self.x2, self.y2 = point_2[0], point_2[1]

def add_edge(edges_arr, point_1, point_2):
    if (point_1[1] > point_2[1]):
        point_1, point_2 = point_2, point_1
    new_edge = Edge(point_1, point_2)
    edges_arr.append(new_edge)

def fill_fig(edges_arr, draw_pixel, check_color, delay):
    min_x, max_x = edges_arr[0].x1, edges_arr[0].x1
    min_y, max_y = edges_arr[0].y1, edges_arr[0].y1

    for i in range(len(edges_arr)):
        if (edges_arr[i].x1 > max_x):
            max_x = edges_arr[i].x1
        if (edges_arr[i].x1 < min_x):
            min_x = edges_arr[i].x1
        if (edges_arr[i].y1 > max_y):
            max_y = edges_arr[i].y1
        if (edges_arr[i].y1 < min_y):
            min_y = edges_arr[i].y1

        if (edges_arr[i].x2 > max_x):
            max_x = edges_arr[i].x2
        if (edges_arr[i].x2 < min_x):
            min_x = edges_arr[i].x2
        if (edges_arr[i].y2 > max_y):
            max_y = edges_arr[i].y2
        if (edges_arr[i].y2 < min_y):
            min_y = edges_arr[i].y2

    for i in range(len(edges_arr)):
        y = edges_arr[i].y1
        x = edges_arr[i].x1

        if (edges_arr[i].y1 == edges_arr[i].y2):
            continue

        dx = (edges_arr[i].x2 - edges_arr[i].x1) / (edges_arr[i].y2 - edges_arr[i].y1)
        while y <= edges_arr[i].y2:
            if (control_pixels(edges_arr, y) == True):
                draw_pixel(round(x) + 1, y, EDGE)
            draw_pixel(round(x), y, EDGE)

            x += dx
            y += 1

    y = min_y
    while (y <= max_y):
        flag = False
        x = min_x
        while x <= max_x:
            if (check_color(x, y) != None):
                flag = not flag
            if (flag == True):
                draw_pixel(x, y, FIG)
            else:
                draw_pixel(x, y, BG)
            x += 1
        if (delay != 0):
            QtWidgets.QApplication.processEvents()
            QThread.msleep(delay)
        y += 1

def control_pixels(edges_arr, y):
    arr = []
    for i in range(len(edges_arr)):
        if (edges_arr[i].y2 - edges_arr[i].y1) < EPS:
            continue

        if (edges_arr[i].y1 <= y <= edges_arr[i].y2):
            x = edges_arr[i].x1 + (edges_arr[i].x2 - edges_arr[i].x1) * \
                (y - edges_arr[i].y1) / (edges_arr[i].y2 - edges_arr[i].y1)
            if round(x) not in arr: arr.append(round(x))
    print(len(arr))
    if len(arr) == 1: return True
    else: return False
