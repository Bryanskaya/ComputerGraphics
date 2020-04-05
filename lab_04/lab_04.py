from tkinter import *
from tkinter import colorchooser
import tkinter.messagebox as box
from tkinter.ttk import Combobox
from math import *
import matplotlib.pyplot as plt
import numpy as np
import time

def draw_axis():
    canv.create_line(transf_x(X_MIN), transf_y(0),
                     transf_x(X_MAX), transf_y(0),
                     fill = 'grey', dash = (4, 2), arrow = 'last')
    canv.create_line(transf_x(0) + 4, transf_y(Y_MIN),
                     transf_x(0) + 4, transf_y(Y_MAX),
                     fill = 'grey', dash = (4, 2), arrow = 'last')

    canv.create_text(transf_x(X_MAX) - 10, transf_y(0) - 15,
                     text = str(X_MAX), fill = 'grey', font = 'Times 11')
    canv.create_text(transf_x(0) + 20, transf_y(Y_MAX) + 10,
                     text = str(Y_MAX), fill = 'grey', font = 'Times 11')
    canv.create_text(transf_x(0) + 15, transf_y(Y_MIN) - 15,
                     text = str(Y_MIN), fill = 'grey', font = 'Times 11')

def draw_pixel(x, y, color):
    canv.create_rectangle(transf_x(x), transf_y(y), transf_x(x), transf_y(y),
                          width = 1, outline='', fill=color)

def clean_canvas(event = 0):
    global canv
    canv.delete("all")
    draw_axis()

def task_information():
    box.showinfo('Условие задачи', '1. Реализация и исследование алгоритмов '
                 'построения окружностей и эллипсов\nПредлагается 5 вариантов алгоритмов.\n'
                 'Пользователь должен выбрать 1 из 5 вариантов построения, цвет '
                 'линии и фона, задать параметры в соответствии с выбранной фигурой.\n'
                 '\n2. Сравнение визуальный характеристик окружностей/эллипсов, построенных '
                 'разными алгоритмами\n\n3. Исследование временных характеристик')

def additional_information():
    box.showinfo('Возможные алгоритмы', 'Алгоритмы:\n'
                 '1. через каноническое уравнение\n'
                 '2. через параметрическое уравнение\n'
                 '3. Брезенхема\n'
                 '4. средней точки\n'
                 '5. встроенная функция\n')

def change_color_back(event = 0):
    global color_back
    global BACK_COLOR
    global canv

    color = colorchooser.askcolor()
    color_back.destroy()

    BACK_COLOR = color[1]

    color_back = Label(frame_3, width = 6, bg = BACK_COLOR, relief = GROOVE)
    color_back.place(x = 125, y = 10)

    canv.config(bg = BACK_COLOR)

def change_color_same(event = 0):
    global color_line
    global CIRCLE_COLOR

    color_line.destroy()

    CIRCLE_COLOR = BACK_COLOR

    color_line = Label(frame_3, width = 6, bg = CIRCLE_COLOR, relief = GROOVE)
    color_line.place(x = 125, y = 48)

def change_color_circle(event = 0):
    global color_line
    global CIRCLE_COLOR

    color = colorchooser.askcolor()
    color_line.destroy()

    CIRCLE_COLOR = color[1]

    color_line = Label(frame_3, width = 6, bg = CIRCLE_COLOR, relief = GROOVE)
    color_line.place(x = 125, y = 48)

def commands_circle(event = 0):
    global frame_4
    global entry_center_x, entry_center_y
    global entry_rad

    for widget in frame_4.winfo_children():
        widget.destroy()

    label = Label(frame_4, text = 'Окружность', font = 'Times 13 bold').place(x = 10, y = 5)
    label = Label(frame_4, text = 'Центр:', font='Times 13 bold').place(x = 20, y = 35)
    label = Label(frame_4, text='[', font='Times 15 bold').place(x = 80, y = 30)
    entry_center_x = Entry(frame_4, width = 5, relief = SUNKEN,
                          font='Times 13 bold')
    entry_center_x.place(x = 100, y = 35)
    label = Label(frame_4, text = ';', font = 'Times 15 bold').place(x = 150, y = 30)
    entry_center_y = Entry(frame_4, width = 5, relief = SUNKEN,
                          font='Times 13 bold')
    entry_center_y.place(x = 165, y = 35)
    label = Label(frame_4, text=']', font = 'Times 15 bold').place(x = 220, y = 30)
    label = Label(frame_4, text = 'Радиус', font = 'Times 13 bold').place(x = 20, y = 70)
    entry_rad = Entry(frame_4, width = 5, relief = SUNKEN,
                        font = 'Times 13 bold')
    entry_rad.place(x = 100, y = 70)

    entry_center_x.insert(0, 0)
    entry_center_y.insert(0, 0)
    entry_rad.insert(0, 0)

    btn_draw_circle = Button(frame_4, text='Изобразить', font='Times 10 bold',
                          bg='lightgray')
    btn_draw_circle.bind('<Button-1>', draw_circle)
    btn_draw_circle.bind('<Return>', draw_circle)
    btn_draw_circle.place(x = 165, y = 68)

def commands_cascade_circles(event = 0):
    global count_param, param
    count_param = 0
    param = [0, 0, 0, 0]


    for widget in frame_4.winfo_children():
        widget.destroy()

    global entry_center_x, entry_center_y

    label = Label(frame_4, text = 'Центр:', font = 'Times 13 bold').place(x = 10, y = 3)
    label = Label(frame_4, text='[', font = 'Times 15 bold').place(x = 70, y = 1)
    entry_center_x = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_center_x.place(x = 90, y = 5)
    label = Label(frame_4, text = ';', font = 'Times 15 bold').place(x = 140, y = 1)
    entry_center_y = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_center_y.place(x = 155, y = 5)
    label = Label(frame_4, text = ']', font = 'Times 15 bold').place(x = 210, y = 1)
    btn_rad_start = Button(frame_4, text = 'Начальный\nрадиус',
                              font = 'Times 10 bold', bg = 'lightgray')
    btn_rad_start.bind('<Button-1>', input_rad_start)
    btn_rad_start.bind('<Return>', input_rad_start)
    btn_rad_start.place(x = 20, y = 35)
    btn_rad_end = Button(frame_4, text='Конечный\nрадиус',
                           font='Times 10 bold', bg='lightgray')
    btn_rad_end.bind('<Button-1>', input_rad_end)
    btn_rad_end.bind('<Return>', input_rad_end)
    btn_rad_end.place(x = 100, y = 35)
    btn_step = Button(frame_4, text = 'Шаг\n', padx = "18",
                         font = 'Times 10 bold', bg = 'lightgray')
    btn_step.bind('<Button-1>', input_step)
    btn_step.bind('<Return>', input_step)
    btn_step.place(x = 174, y = 35)
    btn_num = Button(frame_4, text='Количество\nокружностей',
                      font='Times 10 bold', bg='lightgray')
    btn_num.bind('<Button-1>', input_num)
    btn_num.bind('<Return>', input_num)
    btn_num.place(x = 249, y = 35)

    entry_center_x.insert(0, 0)
    entry_center_y.insert(0, 0)

    btn_draw = Button(frame_4, text='Изобразить', padx = "6",
                     font='Times 10 bold', bg='lightgray')
    btn_draw.bind('<Button-1>', draw_cascade_circles)
    btn_draw.bind('<Return>', draw_cascade_circles)
    btn_draw.place(x=249, y=5)

def input_rad_start(event = 0):
    global count_param

    if count_param < 3:
        if param[0] == 0:
            count_param += 1
            param[0] = 1
    elif param[0] == 0:
        label = Label(frame_4, text='Достаточно 3\nпараметра', fg = 'red',
                    font='Times 10')
        label.place(x=21, y=83)
        return

    global entry_rad_start

    entry_rad_start = Entry(frame_4, width = 8, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_rad_start.place(x = 21, y = 83)

    entry_rad_start.insert(0, 0)

def input_rad_end(event = 0):
    global count_param

    if count_param < 3:
        if param[1] == 0:
            count_param += 1
            param[1] = 1
    elif param[1] == 0:
        label = Label(frame_4, text='Достаточно 3\nпараметра', fg = 'red',
                      font='Times 10')
        label.place(x = 103, y = 83)
        return

    global entry_rad_end

    entry_rad_end = Entry(frame_4, width = 7, relief = SUNKEN,
                            font = 'Times 13 bold')
    entry_rad_end.place(x = 103, y = 83)

    entry_rad_end.insert(0, 0)

def input_step(event = 0):
    global count_param

    if count_param < 3:
        if param[2] == 0:
            count_param += 1
            param[2] = 1
    elif param[2] == 0:
        label = Label(frame_4, text='Достаточно 3\nпараметра', fg = 'red',
                      font='Times 10')
        label.place(x = 175, y =  83)
        return

    global entry_step

    entry_step = Entry(frame_4, width = 7, relief = SUNKEN,
                            font = 'Times 13 bold')
    entry_step.place(x = 175, y = 83)

    entry_step.insert(0, 0)

def input_num(event = 0):
    global count_param

    if count_param < 3:
        if param[3] == 0:
            count_param += 1
            param[3] = 1
    elif param[3] == 0:
        label = Label(frame_4, text='Достаточно 3\nпараметра', fg = 'red',
                      font='Times 10')
        label.place(x = 249, y = 83)
        return

    global entry_num

    entry_num = Entry(frame_4, width = 9, relief = SUNKEN,
                       font = 'Times 13 bold')
    entry_num.place(x = 249, y = 83)

    entry_num.insert(0, 0)

def commands_ellipse(event = 0):
    for widget in frame_4.winfo_children():
        widget.destroy()

    global entry_center_x, entry_center_y
    global entry_axle_a, entry_axle_b

    label = Label(frame_4, text = 'Эллипс', font = 'Times 13 bold').place(x = 10, y = 3)
    label = Label(frame_4, text = 'Центр:', font = 'Times 13 bold').place(x = 20, y = 28)
    label = Label(frame_4, text = '[', font = 'Times 15 bold').place(x = 100, y = 26)
    entry_center_x = (Entry(frame_4, width = 5, relief = SUNKEN,
                           font = 'Times 13 bold'))
    entry_center_x.place(x = 120, y = 30)
    label = Label(frame_4, text = ';', font = 'Times 15 bold').place(x = 170, y = 26)
    entry_center_y = Entry(frame_4, width = 5, relief = SUNKEN,
                           font = 'Times 13 bold')
    entry_center_y.place(x = 185, y = 30)
    label = Label(frame_4, text = ']', font = 'Times 15 bold').place(x = 240, y = 26)
    label = Label(frame_4, text = 'Полуось а:', font='Times 13 bold').place(x = 20, y = 60)
    entry_axle_a = Entry(frame_4, width = 5, relief = SUNKEN,
                      font = 'Times 13 bold')
    entry_axle_a.place(x = 120, y = 61)
    label = Label(frame_4, text = 'Полуось b:', font = 'Times 13 bold').place(x = 20, y = 90)
    entry_axle_b = Entry(frame_4, width=5, relief=SUNKEN,
                       font='Times 13 bold')
    entry_axle_b.place(x = 120, y = 91)

    entry_center_x.insert(0, 0)
    entry_center_y.insert(0, 0)
    entry_axle_a.insert(0, 0)
    entry_axle_b.insert(0, 0)

    btn_draw_ellipse = Button(frame_4, text='Изобразить', font='Times 10 bold',
                             bg='lightgray')
    btn_draw_ellipse.bind('<Button-1>', draw_ellipse)
    btn_draw_ellipse.bind('<Return>', draw_ellipse)
    btn_draw_ellipse.place(x = 185, y = 60)

def commands_cascade_ellipse(event = 0):
    for widget in frame_4.winfo_children():
        widget.destroy()

    global entry_center_x, entry_center_y
    global entry_axle_a, entry_axle_b
    global choose_axle, entry_chosen_axle
    global entry_num

    label = Label(frame_4, text='Центр:', font='Times 13 bold').place(x=10, y=3)
    label = Label(frame_4, text='[', font='Times 15 bold').place(x=90, y=1)
    entry_center_x = Entry(frame_4, width=5, relief=SUNKEN,
                           font='Times 13 bold')
    entry_center_x.place(x=110, y=5)
    label = Label(frame_4, text=';', font='Times 15 bold').place(x=160, y=1)
    entry_center_y = Entry(frame_4, width=5, relief=SUNKEN,
                           font='Times 13 bold')
    entry_center_y.place(x=175, y=5)
    label = Label(frame_4, text=']', font='Times 15 bold').place(x = 230, y = 1)
    label = Label(frame_4, text='Полуось а:', font='Times 13 bold').place(x=10, y=35)
    entry_axle_a = Entry(frame_4, width=5, relief=SUNKEN,
                         font='Times 13 bold')
    entry_axle_a.place(x=110, y=36)
    label = Label(frame_4, text='Полуось b:', font='Times 13 bold').place(x=170, y=36)
    entry_axle_b = Entry(frame_4, width=5, relief=SUNKEN,
                         font='Times 13 bold')
    entry_axle_b.place(x=270, y=36)
    label = Label(frame_4, text='Шаг изменения полуоси', font='Times 13 bold').place(x=10, y=66)
    choose_axle = Combobox(frame_4, values = ('a', 'b'), width = 1, font='Times 13 bold')
    choose_axle.current(0)
    choose_axle.place(x = 210, y = 66)
    label = Label(frame_4, text=':', font='Times 15 bold').place(x=245, y=66)
    entry_chosen_axle = Entry(frame_4, width=5, relief=SUNKEN,
                         font='Times 13 bold')
    entry_chosen_axle.place(x=270, y=66)
    label = Label(frame_4, text='Количество эллипсов:', font='Times 13 bold').place(x=10, y=96)
    entry_num = Entry(frame_4, width=5, relief=SUNKEN,
                      font='Times 13 bold')
    entry_num.place(x=270, y=94)

    entry_center_x.insert(0, 0)
    entry_center_y.insert(0, 0)
    entry_axle_a.insert(0, 0)
    entry_axle_b.insert(0, 0)
    entry_chosen_axle.insert(0, 0)
    entry_num.insert(0, 0)

    btn_draw_ellipse = Button(frame_4, text='Изобразить', font='Times 10 bold',
                              bg='lightgray')
    btn_draw_ellipse.bind('<Button-1>', draw_cascade_ellipse)
    btn_draw_ellipse.bind('<Return>', draw_cascade_ellipse)
    btn_draw_ellipse.place(x=270, y=1)

def transf_x(x):
    return x

def transf_y(y):
    return canvas_y - y

def get_method():
    return var2.get()

def draw_circle_by_way(method, x_center, y_center, r):
    time_start = time.time()

    if (method == CANONICAL):
        method_canonical_circle(x_center, y_center, r)
    elif (method == PARAMETRIC):
        method_parametric_circle(x_center, y_center, r)
    elif (method == BRESENHAM):
        method_bresenham_circle(x_center, y_center, r)
    elif (method == MIDDLE_POINT):
        method_middle_point_circle(x_center, y_center, r)
    elif (method == CLASSIC):
        draw_classic_circle(x_center, y_center, r)

    return time.time() - time_start

def draw_ellipse_by_way(method, x_center, y_center, axle_a, axle_b):
    time_start = time.time()

    if (method == CANONICAL):
        method_canonical_ellipse(x_center, y_center, axle_a, axle_b)
    elif (method == PARAMETRIC):
        method_parametric_ellipse(x_center, y_center, axle_a, axle_b)
    elif (method == BRESENHAM):
        method_bresenham_ellipse(x_center, y_center, axle_a, axle_b)
    elif (method == MIDDLE_POINT):
        method_middle_point_ellipse(x_center, y_center, axle_a, axle_b)
    elif (method == CLASSIC):
        draw_classic_ellipse(x_center, y_center, axle_a, axle_b)

    return time.time() - time_start

def draw_classic_circle(x_center, y_center, r):
    canv.create_oval(transf_x(x_center - r), transf_y(y_center + r),
                     transf_x(x_center + r), transf_y(y_center - r),
                     outline = CIRCLE_COLOR)

def method_canonical_circle(x_center, y_center, r):
    r2 = r ** 2
    x = 0
    x_temp = round(r/sqrt(2))

    while x <= x_temp:
        y = sqrt(r2 - x**2)

        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        draw_pixel(y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(y + x_center, -x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, -x + y_center, CIRCLE_COLOR)

        x += 1

def method_parametric_circle(x_center, y_center, r):
    t = 0
    t_temp = pi / 4
    step = 1 / r

    while t <= t_temp + EPS:
        x = round(r * cos(t))
        y = round(r * sin(t))

        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        draw_pixel(y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(y + x_center, -x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, -x + y_center, CIRCLE_COLOR)

        t += step

def method_bresenham_circle(x_center, y_center, r):
    y_temp = round(r / sqrt(2))
    x, y = 0, r
    d = 2 * (1 - r)

    while (y >= y_temp):
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        draw_pixel(y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(y + x_center, -x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, -x + y_center, CIRCLE_COLOR)

        if (d < 0):
            d1 = 2 * (d + y) - 1
            if (d1 <= 0):
                x += 1
                d += 2 * x + 1
                continue
        x += 1
        y -= 1
        d += 2 * (x - y + 1)

def method_middle_point_circle(x_center, y_center, r):
    fp = 1.25 - r
    x, y = 0, r

    dx, dy = 1, 2 * y
    while (x <= y):
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        draw_pixel(y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(y + x_center, -x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, x + y_center, CIRCLE_COLOR)
        draw_pixel(-y + x_center, -x + y_center, CIRCLE_COLOR)

        x += 1
        if (fp >= 0):
            y -= 1
            dy -= 2
            fp -= dy
        dx += 2
        fp += dx

def draw_classic_ellipse(x_center, y_center, a, b):
    canv.create_oval(transf_x(x_center - a), transf_y(y_center + b),
                     transf_x(x_center + a), transf_y(y_center - b),
                     outline=CIRCLE_COLOR)

def method_canonical_ellipse(x_center, y_center, a, b):
    a2, b2 = a ** 2, b ** 2
    x_temp = round(a2 * sqrt(1 / (b2 + a2)))
    x = 0

    while x <= x_temp:
        y = sqrt(b2 * (1 - x**2 / a2))
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR) #-----
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR) #----

        x += 1

    y_temp = round(b2 * sqrt(1 / (b2 + a2)))
    y = 0

    while y <= y_temp:
        x = sqrt(a2 * (1 - y**2 / b2))
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        y += 1

def method_parametric_ellipse(x_center, y_center, a, b):
    a2, b2 = a ** 2, b ** 2

    t = 0
    k = min(a / b2, b / a2)
    t_temp = pi / 2

    while t <= t_temp + EPS:
        x = round(a * cos(t))
        y = round(b * sin(t))

        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        t += k

def method_bresenham_ellipse(x_center, y_center, a, b):
    a2, b2 = a ** 2, b ** 2

    x, y = 0, b
    d = 1 / a2 + (-2 * b + 1) / b2

    while (y >= 0):
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        if (d < 0):
            d1 = 2 * d + (2 * y - 1) / b2
            if (d1 <= 0):
                x += 1
                d += (2 * x + 1) / a2
                continue
        elif (d > 0):
            d2 = 2 * d - (2 * x + 1) / a2
            if (d2 > 0):
                y -= 1
                d += (-2 * y + 1) / b2
                continue
        x += 1
        y -= 1
        d += (2 * x + 1) / a2 + (-2 * y + 1) / b2

def method_middle_point_ellipse(x_center, y_center, a, b):
    a2, b2 = a ** 2, b ** 2
    ad, bd = 2 * a2, 2 * b2
    fp = b2 - a2 * b + 0.25 * a2
    x, y = 0, b

    dx, dy = b2, ad * y
    max_x = round(a2 * sqrt(1 / (b2 + a2)))
    while (x <= max_x):
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        x += 1
        if (fp >= 0):
            y -= 1
            dy -= ad
            fp -= dy
        dx += bd
        fp += dx

    fp  += 0.75 * (a2 - b2) - (a2 * y + b2 * x)
    dx, dy = bd * x, a2 * (2 * y - 1)
    while (y >= 0):
        draw_pixel(x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, y + y_center, CIRCLE_COLOR)
        draw_pixel(x + x_center, -y + y_center, CIRCLE_COLOR)
        draw_pixel(-x + x_center, -y + y_center, CIRCLE_COLOR)

        y -= 1
        if (fp <= 0):
            x += 1
            dx += bd
            fp += dx
        dy -= ad
        fp -= dy

def check_point(x, y):
    if (x == '' or y == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                                  'Присутствуют пустые поля')
        return FAILURE, FAILURE

    try:
        x = float(x)
        y = float(y)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE, FAILURE

    return x, y

def check_radius(r):
    if (r == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                                  'Присутствуют пустые поля')
        return FAILURE

    try:
        r = float(r)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE

    if (r <= 0):
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE
    return r

def check_step(step):
    if (step == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                                  'Присутствуют пустые поля')
        return FAILURE

    try:
        step = float(step)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE

    return step

def check_num(num):
    if (num == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                                  'Присутствуют пустые поля')
        return FAILURE

    try:
        num = int(num)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE

    if (num <= 0):
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE
    return num

def draw_circle(event = 0):
    x_center = entry_center_x.get()
    y_center = entry_center_y.get()
    r = entry_rad.get()

    x_center, y_center = check_point(x_center, y_center)
    if (x_center == FAILURE): return

    r = check_radius(r)
    if (r == FAILURE): return

    method = get_method()
    draw_circle_by_way(method, x_center, y_center, r)

def draw_cascade_circles(event = 0):
    if (count_param < 3):
        box.showwarning('Ошибка', 'Недостаточное количество параметров\n'
                                  'Необходимо три параметра')
        return

    x_center = entry_center_x.get()
    y_center = entry_center_y.get()

    x_center, y_center = check_point(x_center, y_center)
    if (x_center == FAILURE): return

    if (param[0]):
        r_start = entry_rad_start.get()
        r_start = check_radius(r_start)
        if (r_start == FAILURE): return

    if (param[1]):
        r_end = entry_rad_end.get()
        r_end = check_radius(r_end)
        if (r_end == FAILURE): return

    if (param[2]):
        step = entry_step.get()
        step = check_step(step)
        if (step == FAILURE): return

    if (param[3]):
        num = entry_num.get()
        num = check_num(num)
        if (num == FAILURE): return

    if (param[3] == 0):
        num = int(abs(r_end - r_start) / step)
    elif (param[2] == 0):
        step = float((r_end - r_start) / (num - 1))
    elif (param[1] == 0):
        r_end = float(r_start + step * num)
    elif (param[0] == 0):
        r_start = float(r_end - step * num)

    method = get_method()

    for i in range(num):
        r = round(r_start + step * i)
        draw_circle_by_way(method, x_center, y_center, r)

def draw_ellipse(event = 0):
    x_center = entry_center_x.get()
    y_center = entry_center_y.get()
    a = entry_axle_a.get()
    b = entry_axle_b.get()

    x_center, y_center = check_point(x_center, y_center)
    if (x_center == FAILURE): return

    a = check_radius(a)
    if (a == FAILURE): return

    b = check_radius(b)
    if (b == FAILURE): return

    method = get_method()
    draw_ellipse_by_way(method, x_center, y_center, a, b)

def draw_cascade_ellipse(event = 0):
    x_center = entry_center_x.get()
    y_center = entry_center_y.get()

    x_center, y_center = check_point(x_center, y_center)
    if (x_center == FAILURE): return

    a = entry_axle_a.get()
    a = check_radius(a)
    if (a == FAILURE): return

    b = entry_axle_b.get()
    b = check_radius(b)
    if (b == FAILURE): return

    if (choose_axle.get() == 'a'): flag = 1
    elif (choose_axle.get() == 'b'): flag = 0
    else:
        box.showwarning('Ошибка', 'Некорректное название полуоси\n')
        return

    step = entry_chosen_axle.get()
    step = check_step(step)
    if (step == FAILURE): return

    num = entry_num.get()
    num = check_num(num)
    if (num == FAILURE): return

    method = get_method()

    for i in range(num):
        if (flag):
            a_temp = round(a + step * i)
            b_temp = round(b * (step * i + a) / a)
        else:
            b_temp = round(b + step * i)
            a_temp = round(a * (step * i + b) / b)
        draw_ellipse_by_way(method, x_center, y_center, a_temp, b_temp)

def analysing(event = 0):
    methods = ['Каноническое\nуравнение', 'Параметрическое\nуравнение',
               'Брезенхем', 'Средняя точка', 'Встроенная\nфункция']
    t = []
    rad = np.arange(1, 200, 30)
    print(rad, len(rad))
    color_l = ['red', 'green', 'blue', 'black', 'orange']

    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.xlabel('Радиус')
    plt.ylabel('Время (в секундах)')
    plt.title('Зависимость времени работы от радиуса окружности', size=9)

    for i in range(5):
        for j in range(len(rad)):
            t.append(draw_circle_by_way(i, X_C, Y_C, rad[j]))
        plt.plot(rad, t, linewidth = 1, linestyle = "-", color=color_l[i], label=methods[i])
        clean_canvas()
        t = []
    plt.legend(loc='upper left')

    axle_a = np.arange(1, 200, 30)
    axle_b = []
    axle_b.append(0.5)
    for i in range(1, len(axle_a)):
        axle_b.append(round(axle_b[0] * (30 * i + axle_a[0]) / axle_a[0]))

    plt.subplot(122)
    plt.xlabel('Полуось')
    plt.ylabel('Время (в секундах)')
    plt.title('Зависимость времени работы от полуоси эллипса', size=9)

    for i in range(5):
        for j in range(len(axle_a)):
            t.append(draw_ellipse_by_way(i, X_C, Y_C, axle_a[j], axle_b[j]))
        plt.plot(axle_a, t, linewidth=1, linestyle="-", color=color_l[i], label=methods[i])
        clean_canvas()
        t = []
    plt.legend(loc = 'upper left')

    plt.show()


#--------------------------------------------------------------------------
BACK_COLOR    = '#000000'
CIRCLE_COLOR  = '#f8f8f8'
#-------------------------------------------------------------------------------
CANONICAL     = 0
PARAMETRIC    = 1
BRESENHAM     = 2
MIDDLE_POINT  = 3
CLASSIC       = 4

FAILURE         = -100102562

X_MIN      = 0
X_MAX      = 616
Y_MIN      = 0
Y_MAX      = 605
EPS        = 1e-3

count_param = 0
param       = [0, 0, 0, 0]

frame_4        = None

entry_center_x    = None
entry_center_y    = None
entry_rad         = None
entry_rad_start   = None
entry_rad_end     = None
entry_step        = None
entry_num         = None
entry_axle_a      = None
entry_axle_b      = None
entry_chosen_axle = None

btn_draw_cascade  = None
btn_draw_circle   = None
btn_draw_ellipse  = None

choose_axle       = None

color_back     = None
color_line      = None

canv           = None

X_C = 0
Y_C = 0
#--------------------------------------------------------------------------

window = Tk()

frame_1 = Frame(window, width = 360, height = 140, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_2 = Frame(window, width = 360, height = 170, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_3 = Frame(window, width = 360, height = 85, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_4 = Frame(window, width = 360, height = 130, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_5 = Frame(window, width = 360, height = 72, highlightbackground =
                'lightblue', highlightthickness = 2)


label = Label(window, text = 'Реализация и исследование алгоритмов '
                 'построения окружностей и эллипсов', font = 'Times 14 bold')
label.place(x = 200, y = 5)

var1 = IntVar()
var1.set(0)

var2 = IntVar()
var2.set(0)

label = Label(frame_1, text = 'Построение:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
radio_0 = Radiobutton(frame_1, text = 'одиночной окружности', font = 'Times 13',
                      variable = var1, value = 0, command = commands_circle)
radio_1 = Radiobutton(frame_1, text = 'концентрических окружностей', font = 'Times 13',
                      variable = var1, value = 1, command = commands_cascade_circles)
radio_2 = Radiobutton(frame_1, text = 'одиночный эллипс', font = 'Times 13',
                      variable = var1, value = 2, command = commands_ellipse)
radio_3 = Radiobutton(frame_1, text = 'концентрических эллипсов', font = 'Times 13',
                      variable = var1, value = 3, command = commands_cascade_ellipse)

radio_0.place(x = 15, y = 30)
radio_1.place(x = 15, y = 55)
radio_2.place(x = 15, y = 80)
radio_3.place(x = 15, y = 105)

label = Label(frame_2, text = 'Алгоритм:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
radio_0 = Radiobutton(frame_2, text = 'Через каноническое уравнение',
                      font = 'Times 13', variable = var2, value = 0)
radio_1 = Radiobutton(frame_2, text = 'Через параметрическое уравнение',
                      font = 'Times 13', variable = var2, value = 1)
radio_2 = Radiobutton(frame_2, text = 'Брезенхема',
                      font = 'Times 13', variable = var2, value = 2)
radio_3 = Radiobutton(frame_2, text = 'Средней точки',
                      font = 'Times 13', variable = var2, value = 3)
radio_4 = Radiobutton(frame_2, text = 'Встроенная функция',
                      font = 'Times 13', variable = var2, value = 4)

radio_0.place(x = 15, y = 30)
radio_1.place(x = 15, y = 55)
radio_2.place(x = 15, y = 80)
radio_3.place(x = 15, y = 105)
radio_4.place(x = 15, y = 130)

label = Label(frame_3, text = 'Цвет фона:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
color_back = Label(frame_3, width = 6, bg = BACK_COLOR, relief = GROOVE)
color_back.place(x = 125, y = 10)
btn_back_color = Button(frame_3, text = ' Изменить', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_back_color.bind('<Button-1>', change_color_back)
btn_back_color.bind('<Return>', change_color_back)
btn_back_color.place(x = 180, y = 8)

label = Label(frame_3, text = 'Цвет линии:', font = 'Times 13 bold')
label.place(x = 10, y = 45)
color_line = Label(frame_3, width = 6, bg = CIRCLE_COLOR, relief = GROOVE)
color_line.place(x = 125, y = 48)
btn_same_color = Button(frame_3, text = 'Цвет фона', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_same_color.bind('<Button-1>', change_color_same)
btn_same_color.bind('<Return>', change_color_same)
btn_same_color.place(x = 257, y = 45)

btn_line_color = Button(frame_3, text = ' Изменить ', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_line_color.bind('<Button-1>', change_color_circle)
btn_line_color.bind('<Return>', change_color_circle)
btn_line_color.place(x = 180, y = 45)

btn_analys = Button(frame_5, text = 'Анализ', width = 12, font = 'Times 10 bold',
                        bg = 'lightgray')
btn_analys.bind('<Button-1>', analysing)
btn_analys.bind('<Return>', analysing)
btn_analys.place(x = 60, y = 10)

btn_clean = Button(frame_5, text = 'Очистить поле', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_clean.bind('<Button-1>', clean_canvas)
btn_clean.bind('<Return>', clean_canvas)
btn_clean.place(x = 175, y = 10)

canvas_x = 616
canvas_y = 605
canv = Canvas(window, width = canvas_x, height = canvas_y,
              bg = BACK_COLOR)

commands_circle()
draw_axis()

window.geometry('1000x650')

main_menu = Menu(window)

main_menu.add_cascade(label = 'Условие задачи', command = task_information)
main_menu.add_cascade(label = 'Дополнительная информация',
                      command = additional_information)
window.config(menu = main_menu)

frame_1.place(x = 2, y = 33)
frame_2.place(x = 2, y = 175)
frame_3.place(x = 2, y = 347)
frame_4.place(x = 2, y = 434)
frame_5.place(x = 2, y = 566)

canv.place(x = 370, y = 32)

window.mainloop()
