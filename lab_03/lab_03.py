from tkinter import*
import tkinter.messagebox as box
from math import*
import matplotlib.pyplot as plt
import numpy as np
import time

def task_information():
    box.showinfo('Условие задачи', '1. Реализация и исследование алгоритмов '
                 'построения отрезков\nПредлагается 6 вариантов алгоритмов.\n'
                 'Пользователь должен выбрать 1 из 6 вариантов построения, цвет '
                 'отрезка и фона, задать координаты концов.\n'
                 '\n2. Сравнение визуальный характеристик отрезков, построенных '
                 'разными алгоритмами\n\n3. Исследование временных характеристик')

def additional_information():
    box.showinfo('Возможные алгоритмы', 'Алгоритмы:\n'
                 '1. Цифрового дифференциального анализатора\n'
                 '2. Брезенхема (для действительных чисел)\n'
                 '3. Брезенхема (для целых чисел)\n'
                 '4. Брезенхема (устранение ступенчатости)\n'
                 '5. Ву\n'
                 '6. Встроенная функция\n')

def commands_cut(event = 0):
    global frame_4
    global entry_start_x
    global entry_start_y 
    global entry_end_x
    global entry_end_y
    global btn_draw_cut

    for widget in frame_4.winfo_children():
       widget.destroy()
    
    label = Label(frame_4, text = 'Координаты отрезка:', font = 'Times 13 bold')
    label.place(x = 10, y = 5)
    label = Label(frame_4, text = 'x', font = 'Times 13 bold')
    label.place(x = 140, y = 27)
    label = Label(frame_4, text = 'y', font = 'Times 13 bold')
    label.place(x = 205, y = 27)
    label = Label(frame_4, text = 'начало', font = 'Times 13 bold')
    label.place(x = 30, y = 45)
    label = Label(frame_4, text = '[', font = 'Times 15 bold')
    label.place(x = 100, y = 45)
    entry_start_x = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_start_x.place(x = 120, y = 49)
    label = Label(frame_4, text = ';', font = 'Times 15 bold')
    label.place(x = 175, y = 45)
    entry_start_y = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_start_y.place(x = 190, y = 49)
    label = Label(frame_4, text = ']', font = 'Times 15 bold')
    label.place(x = 245, y = 45)
    label = Label(frame_4, text = 'конец', font = 'Times 13 bold')
    label.place(x = 30, y = 80)
    label = Label(frame_4, text = '[', font = 'Times 15 bold')
    label.place(x = 100, y = 80)
    entry_end_x = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_end_x.place(x = 120, y = 84)
    label = Label(frame_4, text = ';', font = 'Times 15 bold')
    label.place(x = 175, y = 80)
    entry_end_y = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_end_y.place(x = 190, y = 84)
    label = Label(frame_4, text = ']', font = 'Times 15 bold')
    label.place(x = 245, y = 80)
    
    entry_start_x.insert(0, 0)
    entry_start_y.insert(0, 0)
    entry_end_x.insert(0, 0)
    entry_end_y.insert(0, 0)
    
    btn_draw_cut = Button(frame_4, text = 'Изобразить', font = 'Times 10 bold',
                        bg = 'lightgray')
    btn_draw_cut.bind('<Button-1>', draw_cut)
    btn_draw_cut.bind('<Return>', draw_cut)
    btn_draw_cut.place(x = 260, y = 65)
    
def commands_beam(event = 0):
    global frame_4

    for widget in frame_4.winfo_children():
       widget.destroy()

    global entry_start_x
    global entry_start_y 
    global entry_num_cuts
    global entry_len_cuts
    global btn_draw_beam

    label = Label(frame_4, text = 'Центр пучка:', font = 'Times 13 bold')
    label.place(x = 10, y = 23)
    label = Label(frame_4, text = 'x', font = 'Times 13 bold')
    label.place(x = 160, y = 1)
    label = Label(frame_4, text = 'y', font = 'Times 13 bold')
    label.place(x = 225, y = 1)
    label = Label(frame_4, text = '[', font = 'Times 15 bold')
    label.place(x = 120, y = 21)
    entry_start_x = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_start_x.place(x = 140, y = 26)
    label = Label(frame_4, text = ';', font = 'Times 15 bold')
    label.place(x = 195, y = 21)
    entry_start_y = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_start_y.place(x = 210, y = 26)
    label = Label(frame_4, text = ']', font = 'Times 15 bold')
    label.place(x = 265, y = 21)
    label = Label(frame_4, text = 'Шаг:', font = 'Times 13 bold')
    label.place(x = 10, y = 61)
    entry_num_cuts = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_num_cuts.place(x = 140, y = 61)
    label = Label(frame_4, text = '°', font = 'Times 15 bold')
    label.place(x = 190, y = 55)
    label = Label(frame_4, text = 'Длина лучей:', font = 'Times 13 bold')
    label.place(x = 10, y = 91)
    entry_len_cuts = Entry(frame_4, width = 5, relief = SUNKEN,
                          font = 'Times 13 bold')
    entry_len_cuts.place(x = 140, y = 91)

    entry_start_x.insert(0, 0)
    entry_start_y.insert(0, 0)
    entry_num_cuts.insert(0, 0)
    entry_len_cuts.insert(0, 0)
    
    
    btn_draw_beam = Button(frame_4, text = 'Изобразить', font = 'Times 10 bold',
                        bg = 'lightgray')
    btn_draw_beam.bind('<Button-1>', draw_beam)
    btn_draw_beam.bind('<Return>', draw_beam)
    btn_draw_beam.place(x = 260, y = 65)
    

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

def change_color_cuts(event = 0):
    global color_cut
    global CUT_COLOR

    color = colorchooser.askcolor()
    color_cut.destroy()

    CUT_COLOR = color[1]

    color_cut = Label(frame_3, width = 6, bg = CUT_COLOR, relief = GROOVE)
    color_cut.place(x = 125, y = 48)
    
def change_color_same(event = 0):
    global color_cut
    global CUT_COLOR

    color_cut.destroy()
    
    CUT_COLOR = BACK_COLOR

    color_cut = Label(frame_3, width = 6, bg = CUT_COLOR, relief = GROOVE)
    color_cut.place(x = 125, y = 48)

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

def clean_canvas(event = 0):
    global canv
    canv.delete("all")
    draw_axis()

def transf_x(x):
    return x

def transf_y(y):
    return canvas_y - y

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

def draw_cut(event = 0):  
    x_start = entry_start_x.get()
    y_start = entry_start_y.get()
    x_end = entry_end_x.get()
    y_end = entry_end_y.get()

    x_start, y_start = check_point(x_start, y_start)
    if (x_start == FAILURE): return

    x_end, y_end = check_point(x_end, y_end)
    if (x_end == FAILURE): return

    if abs(x_start - x_end) < EPS and abs(y_start - y_end) < EPS:
        box.showinfo('Внимание', 'Отрезок вырожден в точку')
        draw_pixel(x_start, y_start, CUT_COLOR)
        return

    command = get_method()
    command_execution(command, x_start, y_start, x_end, y_end)

def command_execution(command, x_start, y_start, x_end, y_end):
    if command == METHOD_ANALYS:
        method_analys(x_start, y_start, x_end, y_end)
    if command == BRESENHAM_FLOAT:
        method_bresenham_float(x_start, y_start, x_end, y_end)
    if command == BRESENHAM_INT:
        method_bresenham_int(x_start, y_start, x_end, y_end)
    if command == BRESENHAM_STEP:
        method_bresenham_step(x_start, y_start, x_end, y_end)
    if command == BY:
        method_by(x_start, y_start, x_end, y_end)
    if command == CLASSIC:
        draw_classic_cut(x_start, y_start, x_end, y_end)

def draw_pixel(x, y, color):
    canv.create_rectangle(transf_x(x), transf_y(y), transf_x(x), transf_y(y),
                          width = 1, outline = '', fill = color)
    
def draw_pixel_end(x_end, y_end):
    canv.create_rectangle(transf_x(x_end), transf_y(y_end),
                     transf_x(x_end), transf_y(y_end), outline = '', fill = 'red')

    canv.create_oval(transf_x(x_end - 5), transf_y(y_end + 5),
                     transf_x(x_end + 5), transf_y(y_end - 5),
                     outline = '#f5001d')

def get_method():
    return var2.get()

def get_global_color_red():
    return int(BACK_COLOR[ 1 : 3 ], 16)

def get_global_color_green():
    return int(BACK_COLOR[ 3 : 5 ], 16)

def get_global_color_blue():
    return int(BACK_COLOR[ 5 : ], 16)
    
def count_color(color, general, error):
    return hex(int(color + (general - color)*error))

def correct_length_color(color):
    if (len(color) < 2):
        color = '0'*(2 - len(color)) + color
    return color
    
def change_color(error):
    red = int(CUT_COLOR[ 1 : 3 ], 16)
    green = int(CUT_COLOR[ 3 : 5 ], 16)
    blue = int(CUT_COLOR[ 5 : ], 16)

    if (error > 1): error -= 1
    elif (error < 0): error += 1

    red = count_color(red, get_global_color_red(), error)
    green = count_color(green, get_global_color_green(), error)
    blue = count_color(blue, get_global_color_blue(), error)

    red = str(red[2:])
    green = str(green[2:])
    blue = str(blue[2:])

    red = correct_length_color(red)
    green = correct_length_color(green)
    blue = correct_length_color(blue)
    
    return '#' + str(red) + str(green) + str(blue)

def check_end(x, y, x_end, y_end):
    #if abs(x_end - x) < EPS and abs(y_end - y) < EPS: return
    if int(x) == int(x_end) and int(y_end) == int(y): return
    draw_pixel_end(x_end, y_end)

def draw_classic_cut(x_s, y_s, x_e, y_e):
    time_start = time.time()
    
    canv.create_line(transf_x(x_s), transf_y(y_s),
                     transf_x(x_e), transf_y(y_e), fill = CUT_COLOR)
    canv.create_line(transf_x(x_e), transf_y(y_e),
                     transf_x(x_e + sign(x_e - x_s)),
                     transf_y(y_e + sign(y_e - y_s)), fill = CUT_COLOR)

    time_end = time.time()
    return time_end - time_start

def method_analys(x_s, y_s, x_e, y_e):
    time_start = time.time()
    dx = x_e - x_s
    dy = y_e - y_s
    
    if (abs(dx) > abs(dy)):
        num = abs(dx)
    else:
        num = abs(dy)
    dx = dx / num
    dy = dy / num

    x, y = x_s, y_s

    for i in range(1, round(num) + 2):
        draw_pixel(round(x), round(y), CUT_COLOR)
        x += dx
        y += dy

        
    check_end(x - dx, y - dy, x_e, y_e)

    time_end = time.time()

    return time_end - time_start

def sign(a):
    if (a < 0): return -1
    elif (a > 0): return 1
    else: return 0
    
def method_bresenham_float(x_s, y_s, x_e, y_e):
    time_start = time.time()
    
    x, y = x_s, y_s
    
    dx = x_e - x_s
    dy = y_e - y_s
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx > dy):
        exchange = 0
    else:
        exchange = 1
        dx, dy = dy, dx

    m = dy / dx
    error = m - 0.5
    for i in range(1, round(dx) + 2):
        prev_x, prev_y = x, y
        draw_pixel(x, y, CUT_COLOR)
        if (error >= 0):
            if (exchange == 0):
                y += sy
            else:
                x += sx
            error -= 1
        if (exchange == 0):
            x += sx
        else:
            y += sy
        error += m
    check_end(prev_x, prev_y, x_e, y_e)

    time_end = time.time()
    return time_end - time_start

def method_bresenham_int(x_s, y_s, x_e, y_e):
    time_start = time.time()
    
    x = round(x_s)
    y = round(y_s)
    
    dx = round(x_e - x_s)
    dy = round(y_e - y_s)
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx > dy):
        exchange = 0
    else:
        exchange = 1
        dx, dy = dy, dx

    m = dy / dx
    error = 2 * dy - dx
    for i in range(1, dx + 2):
        prev_x, prev_y = x, y
        draw_pixel(x, y, CUT_COLOR)
        if (error >= 0):
            if (exchange == 0):
                y += sy
            else:
                x += sx
            error -= 2 * dx
        if (exchange == 0):
            x += sx
        else:
            y += sy
        error += 2 * dy
    check_end(prev_x, prev_y, x_e, y_e)

    time_end = time.time()
    return time_end - time_start

def method_bresenham_step(x_s, y_s, x_e, y_e):
    time_start = time.time()
    
    x, y = x_s, y_s
    I = 1

    dx = x_e - x_s
    dy = y_e - y_s
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx > dy):
        exchange = 0
    else:
        exchange = 1
        dx, dy = dy, dx
        
    m = dy / dx
    error = I / 2
    m *= I
    w = I - m
    draw_pixel(x, y, change_color(error))
    for i in range(1, round(dx) + 2):
        prev_x, prev_y = x, y
        if (error < w):
            if (exchange == 0):
                x += sx
            else:
                y += sy
            error += m
        else:
            x += sx
            y += sy
            error -= w
        color = change_color(error)
        draw_pixel(x, y, color)
    check_end(prev_x, prev_y, x_e, y_e)

    time_end = time.time()
    return time_end - time_start

def method_by(x_s, y_s, x_e, y_e):
    time_start = time.time()
    
    x1, y1 = x_s, y_s
    x2, y2 = x_e, y_e

    dx = x2 - x1
    dy = y2 - y1
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx < dy):
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    m = dy / dx

    draw_pixel(x1, y1, CUT_COLOR)
    draw_pixel(x2, y2, CUT_COLOR)

    if (exchange):
        y1 += sy
        x1 += sx * m
    else:
        x1 += sx
        y1 += sy * m
    
    for i in range(1, round(dx)):
        if (exchange):
            draw_pixel(int(x1), y1, change_color((x1 - int(x1))))
            draw_pixel(int(x1) + 1, y1, change_color(1 - (x1 - int(x1))))
            y1 += sy
            x1 += sx * m
        else:
            draw_pixel(x1, int(y1), change_color((y1 - int(y1))))
            draw_pixel(x1, int(y1) + 1, change_color(1 - (y1 - int(y1))))
            x1 += sx
            y1 += sy * m

    time_end = time.time()
    return time_end - time_start

def check_num(num):
    if (num == ''):
        box.showwarning('Ошибка', 'Некорректный ввод шага лучей')
        return FAILURE
    
    try:
        num = float(num)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод шага лучей')
        return FAILURE

    if (num == 0 or num > 360):
        box.showwarning('Ошибка', 'Некорректный ввод шага лучей')
        return FAILURE

    return num

def check_length(length):
    if (length == ''):
        box.showwarning('Ошибка', 'Некорректный ввод длины лучей')
        return FAILURE
    
    try:
        length = float(length)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод длины лучей')
        return FAILURE

    if (length <= 0):
        box.showwarning('Ошибка', 'Некорректный ввод длины лучей')
        return FAILURE

    return length
    
def draw_beam(event = 0):
    x_start = entry_start_x.get()
    y_start = entry_start_y.get()
    num = entry_num_cuts.get()
    length = entry_len_cuts.get()

    x_start, y_start = check_point(x_start, y_start)
    if (x_start == FAILURE): return

    num = check_num(num)
    if (num == FAILURE): return

    length = check_length(length)
    if (length == FAILURE): return

    command = get_method()
    drawing_beam(command, x_start, y_start, num, length)
        
def get_xy_beam(x0, y0, r, a):
    return x0 + r * cos(radians(a)), y0 + r * sin(radians(a))
    
def drawing_beam(command, x_s, y_s, alpha, length):
    time_start = time.time()
    
    x, y = x_s, y_s
    x0, y0 = x, y
    a = alpha
    
    for i in range(int(WHOLE_CIRCLE / alpha)):
        x, y = get_xy_beam(x0, y0, length, a)
        command_execution(command, x0, y0, x, y)
        a += alpha

    time_end = time.time()
    return time_end - time_start

def method_analys_max_test(x_s, y_s, x_e, y_e):
    dx = x_e - x_s
    dy = y_e - y_s
    
    if (abs(dx) > abs(dy)):
        num = abs(dx)
    else:
        num = abs(dy)
    dx = dx / num
    dy = dy / num

    x, y = x_s, y_s

    count = 1
    max_count = 0
    
    for i in range(1, round(num) + 2):
        if (int(x) != int(x + dx) and int(y) != int(y + dy)):
            if (count > max_count):
                max_count = count
            count = 1
        else:
            count += 1
        x += dx
        y += dy

    if (count > max_count):
        max_count = count
                
    return max_count

def method_analys_test(x_s, y_s, x_e, y_e):
    dx = x_e - x_s
    dy = y_e - y_s
    
    if (abs(dx) > abs(dy)):
        num = abs(dx)
    else:
        num = abs(dy)
    dx = dx / num
    dy = dy / num

    x, y = x_s, y_s

    len_step = 0
    
    for i in range(1, round(num) + 2):
        if (int(x) != int(x + dx) and int(y) != int(y + dy)):
            len_step += 1
        x += dx
        y += dy             
    return len_step

def method_bresenham_int_max_test(x_s, y_s, x_e, y_e):
    x = round(x_s)
    y = round(y_s)
    
    dx = round(x_e - x_s)
    dy = round(y_e - y_s)
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx > dy):
        exchange = 0
    else:
        exchange = 1
        dx, dy = dy, dx

    m = dy / dx
    error = 2 * dy - dx
    count = 1
    max_count = 0
    for i in range(1, dx + 2):
        if (error >= 0):
            if (exchange == 0):
                y += sy
            else:
                x += sx
            error -= 2 * dx
            
            if (count > max_count):
                max_count = count
            count = 1
        else:
            count += 1
        if (exchange == 0):
            x += sx
        else:
            y += sy
        error += 2 * dy

    if (count > max_count):
        max_count = count
                
    return max_count

def method_bresenham_int_test(x_s, y_s, x_e, y_e):
    x = round(x_s)
    y = round(y_s)
    
    dx = round(x_e - x_s)
    dy = round(y_e - y_s)
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if (dx > dy):
        exchange = 0
    else:
        exchange = 1
        dx, dy = dy, dx

    m = dy / dx
    error = 2 * dy - dx
    len_step = 0
    for i in range(1, dx + 2):
        if (error >= 0):
            if (exchange == 0):
                y += sy
            else:
                x += sx
            error -= 2 * dx
            len_step += 1
        if (exchange == 0):
            x += sx
        else:
            y += sy
        error += 2 * dy
    return len_step
         
def analysing(event = 0):
    methods = ['', 'ЦДА', 'Брезенхем\nна R\nчислах',
               'Брезенхем\nна Z\nчислах',
               'Брезенхем\nустранение\nступенчатости', 'Ву',
               'Встроенная\nфункция']
    x_marks = range(len(methods))

    t = []
    '''t.append(method_analys(0, 0, 1000, 2000))
    t.append(method_bresenham_float(0, 0, 1000, 2000))
    t.append(method_bresenham_int(0, 0, 1000, 2000))
    t.append(method_bresenham_step(0, 0, 1000, 2000))
    t.append(method_by(0, 0, 1000, 2000))
    t.append(draw_classic_cut(0, 0, 1000, 2000))'''

    t.append(drawing_beam(0, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    t.append(drawing_beam(1, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    t.append(drawing_beam(2, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    t.append(drawing_beam(3, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    t.append(drawing_beam(4, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    t.append(drawing_beam(5, TEST_CENTER_X, TEST_CENTER_Y, TEST_CORNER, TEST_LEN))
    
    plt.figure(figsize = (13, 6))
    t[2] -= 0.05

    plt.subplot2grid((2,2), (0,0), rowspan = 2)
    plt.bar([x * 4 for x in [1, 2, 3, 4, 5, 6]], t, width = 2)
    plt.xticks([x * 4 for x in x_marks], methods, rotation = 0, size = 7)
    plt.ylabel('Секунды')
    plt.grid(axis = 'y')
    plt.title('Время работы (построение пучка, длина = {:.1f}, '
              'шаг = {:.1f}°)'.format(TEST_LEN, TEST_CORNER), size = 9)

    grad = np.arange(0, 93, 3)
    len_cda = []
    len_br =  []
    
    plt.subplot2grid((2,2), (0,1), colspan = 1)
    plt.xticks([x * 4 for x in range(len(grad))], grad, rotation = 0, size = 7)

    for i in range(len(grad)):
        x, y = get_xy_beam(0, 0, 500, grad[i])
        len_cda.append(method_analys_test(0, 0, x, y))
        len_br.append(method_bresenham_int_test(0, 0, x, y))
    
    plt.bar([x * 4 for x in range(len(grad))], len_cda, width = 3.5, label = 'ЦДА')
    plt.bar([x * 4 for x in range(len(grad))], len_br, width = 1.5, color = '#00FA9A',
            label = 'Брезенхем')
    plt.legend(loc='upper left')
    plt.ylabel('Количество ступенек')
    plt.grid(axis = 'y')
    plt.title('Исследование ступенчатости от угла на отрезке в 500 пикселей', size = 9)

    grad = np.arange(0, 91, 1)
    max_cda = []
    max_br = []

    for i in range(len(grad)):
        x, y = get_xy_beam(0, 0, 500, grad[i])
        max_cda.append(method_analys_max_test(0, 0, x, y))
        max_br.append(method_bresenham_int_max_test(0, 0, x, y))
    
    plt.subplot2grid((2,2), (1,1), colspan = 1)
    plt.plot(grad, max_br, color = '#00FA9A',label = 'Брезенхем')
    plt.plot(grad, max_cda, '--', label = 'ЦДА')
    plt.legend(loc='upper left')
    plt.ylabel('Количество пикселей')
    plt.grid(axis = 'y')
    plt.title('Максимальная длина ступеньки отрезка в 500 пикселей', size = 9)    
    
    plt.show()
    
#-------------------------------------------------------------------------------
METHOD_ANALYS   = 0
BRESENHAM_FLOAT = 1
BRESENHAM_INT   = 2
BRESENHAM_STEP  = 3
BY              = 4
CLASSIC         = 5
#-------------------------------------------------------------------------------

FAILURE = -100102562
WHOLE_CIRCLE = 360
TEST_CENTER_X = 0
TEST_CENTER_Y = -100
TEST_CORNER = 10
TEST_LEN = 500


BACK_COLOR = '#000000'
CUT_COLOR  = '#f8f8f8'
X_MIN      = 0
X_MAX      = 616
Y_MIN      = 0
Y_MAX      = 548
EPS        = 1e-5

frame_4        = None

entry_start_x  = None
entry_start_y  = None
entry_end_x    = None
entry_end_y    = None
entry_num_cuts = None
entry_len_cuts = None

btn_draw_beam  = None
btn_draw_cut   = None

color_back     = None
color_cut      = None

canv           = None

x_start        = None
y_start        = None
x_end          = None
y_end          = None

window = Tk()

frame_1 = Frame(window, width = 360, height = 90, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_2 = Frame(window, width = 360, height = 190, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_3 = Frame(window, width = 360, height = 85, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_4 = Frame(window, width = 360, height = 125, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_5 = Frame(window, width = 360, height = 50, highlightbackground =
                'lightblue', highlightthickness = 2)


label = Label(window, text = 'Реализация и исследование алгоритмов '
                 'построения отрезков', font = 'Times 14 bold')
label.place(x = 200, y = 5)

var1 = IntVar()
var1.set(0)

var2 = IntVar()
var2.set(0)

label = Label(frame_1, text = 'Построение:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
radio_0 = Radiobutton(frame_1, text = 'одиночного отрезка', font = 'Times 13',
                      variable = var1, value = 0, command = commands_cut)
radio_1 = Radiobutton(frame_1, text = 'пучка', font = 'Times 13',
                      variable = var1, value = 1, command = commands_beam)
radio_0.place(x = 15, y = 30)
radio_1.place(x = 15, y = 55)

label = Label(frame_2, text = 'Алгоритм:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
radio_0 = Radiobutton(frame_2, text = 'Цифровой дифференциального анализатора',
                      font = 'Times 13', variable = var2, value = 0)
radio_1 = Radiobutton(frame_2, text = 'Брезенхема (на действительных чисел)',
                      font = 'Times 13', variable = var2, value = 1)
radio_2 = Radiobutton(frame_2, text = 'Брезенхема (на целых чисел)',
                      font = 'Times 13', variable = var2, value = 2)
radio_3 = Radiobutton(frame_2, text = 'Брезенхема (устранение ступенчатости)',
                      font = 'Times 13', variable = var2, value = 3)
radio_4 = Radiobutton(frame_2, text = 'Ву',
                      font = 'Times 13', variable = var2, value = 4)
radio_5 = Radiobutton(frame_2, text = 'Встроенная функция',
                      font = 'Times 13', variable = var2, value = 5)

radio_0.place(x = 15, y = 30)
radio_1.place(x = 15, y = 55)
radio_2.place(x = 15, y = 80)
radio_3.place(x = 15, y = 105)
radio_4.place(x = 15, y = 130)
radio_5.place(x = 15, y = 155)

label = Label(frame_3, text = 'Цвет фона:', font = 'Times 13 bold')
label.place(x = 10, y = 5)
color_back = Label(frame_3, width = 6, bg = BACK_COLOR, relief = GROOVE)
color_back.place(x = 125, y = 10)
btn_back_color = Button(frame_3, text = ' Изменить', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_back_color.bind('<Button-1>', change_color_back)
btn_back_color.bind('<Return>', change_color_back)
btn_back_color.place(x = 180, y = 8)

label = Label(frame_3, text = 'Цвет отрезка:', font = 'Times 13 bold')
label.place(x = 10, y = 45)
color_cut = Label(frame_3, width = 6, bg = CUT_COLOR, relief = GROOVE)
color_cut.place(x = 125, y = 48)
btn_same_color = Button(frame_3, text = 'Цвет фона', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_same_color.bind('<Button-1>', change_color_same)
btn_same_color.bind('<Return>', change_color_same)
btn_same_color.place(x = 257, y = 45)

btn_cut_color = Button(frame_3, text = ' Изменить ', font = 'Times 10 bold',
                        bg = 'lightgray')
btn_cut_color.bind('<Button-1>', change_color_cuts)
btn_cut_color.bind('<Return>', change_color_cuts)
btn_cut_color.place(x = 180, y = 45)

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
canvas_y = 548
canv = Canvas(window, width = canvas_x, height = canvas_y,
              bg = BACK_COLOR)

commands_cut()
draw_axis()

window.geometry('1000x600')

main_menu = Menu(window)

main_menu.add_cascade(label = 'Условие задачи', command = task_information)
main_menu.add_cascade(label = 'Дополнительная информация',
                      command = additional_information)
window.config(menu = main_menu)

frame_1.place(x = 2, y = 33)
frame_2.place(x = 2, y = 125)
frame_3.place(x = 2, y = 317)
frame_4.place(x = 2, y = 405)
frame_5.place(x = 2, y = 532)

canv.place(x = 370, y = 32)

window.mainloop()
