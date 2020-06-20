from tkinter import*
import tkinter.messagebox as box
from math import*
from copy import*

def task_information():
    box.showinfo('Условие задачи', 'Нарисовать исходный рисунок, осуществить:'
                 '\n- его перенос'
                 '\n- масштабирование'
                 '\n- поворот')

def additional_information():
    box.showinfo('Дополнительная информация', '1. Перенос осуществляется на n '
                 'целых единиц\n'
                 '2. Чтобы произвести масштабирование рисунка задаются '
                 'соответствующие коэффициенты\n'
                 '3. Поворот задаётся углом в градусах')

def center_figure(event = 0):
    box.showinfo('Центр фигуры', 'Центр фигуры находится в точке \n'
                 'с координатами ( ' + str(round(X_CUR, 1)) + ' ; ' +
                 str(round(Y_CUR, 1)) + ' )')

def is_correct_move():
    global entry_dx, entry_dy
    global dx, dy
    
    if (dx == '' and dy == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                        'Пустые поля ввода')
        return FAILURE
    elif (dx == ''):
        entry_dx.insert(0, 0)
        dx = 0
        box.showinfo('Внимание', 'Поле переноса по оси Ох не было заполнено\n'
                        'Произошло автодополнение соответствующей ячейки')
    elif (dy == ''):
        entry_dy.insert(0, 0)
        dy = 0
        box.showinfo('Внимание', 'Поле переноса по оси Оy не было заполнено\n'
                        'Произошло автодополнение соответствующей ячейки')
        
    try:
        dx = int(dx)
        dy = int(dy)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE

    if (dx == 0) and (dy == 0):
        box.showinfo('Внимание', 'Оба значения переноса равны нулю\n'
                        'Перенос не выполняется')
        return FAILURE

def is_correct_degrees():
    global degrees
    global entry_degrees

    if (degrees == ''):
        box.showwarning('Ошибка', 'Некорректное значение градусов\n'
                        'Пустое поле ввода')
        return FAILURE

    try:
        degrees = int(degrees)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод значения градусов')
        return FAILURE

    if (degrees == 0):
        box.showinfo('Внимание', 'Значение угла поворота равно нулю\n'
                        'Поворот не выполняется')
        return FAILURE
    
    if (degrees > 360):
        box.showinfo('Внимание', 'Значение угла поворота больше 360°\n'
                        'Выполнено преобразование')
        degrees %= 360

        entry_degrees.delete(0, END)
        entry_degrees.insert(0, degrees)

def is_correct_rot():
    global X_CENTER_R, Y_CENTER_R

    if (X_CENTER_R == '' or Y_CENTER_R == ''):
        box.showwarning('Ошибка', 'Некорректный ввод центра\n'
                        'Присутствуют пустые поля')
        return FAILURE
    try:
        X_CENTER_R = float(X_CENTER_R)
        Y_CENTER_R = float(Y_CENTER_R)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод центра')
        return FAILURE

def is_correct_k():
    global kx, ky
    global entry_scale_x, entry_scale_y

    if (kx == '' or ky == ''):
        box.showwarning('Ошибка', 'Некорректный ввод\n'
                        'Присутствуют пустые поля')
        return FAILURE

    try:
        kx = float(kx)
        ky = float(ky)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод')
        return FAILURE

    if (kx == 0 and ky == 0):
        box.showinfo('Внимание', 'Фигура превратится в точку')
    elif (kx == 0 or ky == 0):
        box.showinfo('Внимание', 'Фигура превратится в отрезок')
            
        
def prev_moving(event = 0):
    if FLAG_ACTIVE == 0:
        box.showwarning('Ошибка', 'Это первое действие\n'
                        'Предыдущих не было')
        return
    
    clean_canvas()
    change_center(X_PREV, Y_PREV)
    
    global x_oval_cur, y_oval_cur
    global x_oval_prev, y_oval_prev
    
    global x_circle_cur, y_circle_cur
    global x_circle_prev, y_circle_prev
    
    global x_fin_cur, y_fin_cur
    global x_fin_prev, y_fin_prev
    
    global x_eye_cur, y_eye_cur
    global x_eye_prev, y_eye_prev
    
    global x_mouth_cur, y_mouth_cur
    global x_mouth_prev, y_mouth_prev
    
    global x_tail_cur, y_tail_cur
    global x_tail_prev, y_tail_prev

    x_temp = [0] * 2000
    x_temp = deepcopy(x_oval_cur)
    y_temp = [0] * 2000
    y_temp = deepcopy(y_oval_cur)

    x_oval_cur, y_oval_cur = change_array(x_oval_cur, y_oval_cur,
                                          x_oval_prev, y_oval_prev)
    x_oval_prev, y_oval_prev = change_array(x_oval_prev, y_oval_prev,
                                            x_temp, y_temp)
    
    x_temp = deepcopy(x_circle_cur)
    y_temp = deepcopy(y_circle_cur)

    x_circle_cur, y_circle_cur = change_array(x_circle_cur, y_circle_cur,
                                              x_circle_prev, y_circle_prev)
    x_circle_prev, y_circle_prev = change_array(x_circle_prev, y_circle_prev,
                                                x_temp, y_temp)

    x_temp = deepcopy(x_fin_cur)
    y_temp = deepcopy(y_fin_cur)
    
    x_fin_cur, y_fin_cur = change_array(x_fin_cur, y_fin_cur,
                                        x_fin_prev, y_fin_prev)
    x_fin_prev, y_fin_prev = change_array(x_fin_prev, y_fin_prev,
                                          x_temp, y_temp)

    x_temp = deepcopy(x_eye_cur)
    y_temp = deepcopy(y_eye_cur)
    
    x_eye_cur, y_eye_cur = change_array(x_eye_cur, y_eye_cur,
                                        x_eye_prev, y_eye_prev)
    x_eye_prev, y_eye_prev = change_array(x_eye_prev, y_eye_prev,
                                          x_temp, y_temp)

    x_temp = deepcopy(x_mouth_cur)
    y_temp = deepcopy(y_mouth_cur)
    
    x_mouth_cur, y_mouth_cur = change_array(x_mouth_cur, y_mouth_cur,
                                          x_mouth_prev, y_mouth_prev)
    x_mouth_prev, y_mouth_prev = change_array(x_mouth_prev, y_mouth_prev,
                                              x_temp, y_temp)

    x_temp = deepcopy(x_tail_cur)
    y_temp = deepcopy(y_tail_cur)
    
    x_tail_cur, y_tail_cur = change_array(x_tail_cur, y_tail_cur,
                                          x_tail_prev, y_tail_prev)
    x_tail_prev, y_tail_prev = change_array(x_tail_prev, y_tail_prev,
                                            x_temp, y_temp)
    draw_fish()

def change_center(x, y):
    global X_PREV, Y_PREV
    global X_CUR, Y_CUR
        
    X_PREV = X_CUR
    Y_PREV = Y_CUR
    
    X_CUR = x
    Y_CUR = y

def change_array(x_prev, y_prev, x_cur, y_cur):
    x_prev = deepcopy(x_cur)
    y_prev = deepcopy(y_cur)

    return x_prev, y_prev

def clean_canvas():
    global canv
    canv.delete("all")

    draw_axes()

def change_entry_center():
    global entry_center_x
    global entry_center_y

    entry_center_x.delete(0, END)
    entry_center_y.delete(0, END)
    
    entry_center_x.insert(0, X_CENTER_R)
    entry_center_y.insert(0, Y_CENTER_R)

def draw_axes():
    canv.create_line(transf_x(X_MIN), transf_y(0),
                 transf_x(X_MAX), transf_y(0),
                 fill = 'grey', dash = (4, 2), arrow = 'last')
    canv.create_line(transf_x(0), transf_y(Y_MIN),
                 transf_x(0), transf_y(Y_MAX),
                 fill = 'grey', dash = (4, 2), arrow = 'last')
    
    canv.create_text(transf_x(X_MIN) + 15, transf_y(0) - 10,
                     text = str(X_MIN), font = 'Times 11')
    canv.create_text(transf_x(X_MAX) - 15, transf_y(0) - 10,
                     text = str(X_MAX), font = 'Times 11')
    canv.create_text(transf_x(0) + 15, transf_y(Y_MAX) + 10,
                     text = str(Y_MAX), font = 'Times 11')
    canv.create_text(transf_x(0) + 15, transf_y(Y_MIN) - 10,
                     text = str(Y_MIN), font = 'Times 11')

def draw_fish():
    global x_oval_cur, y_oval_cur
    global x_circle_cur, y_circle_cur
    global x_eye_cur, y_eye_cur
    global x_mouth_cur, y_mouth_cur
    global x_fin_cur, y_fin_cur
    global x_tail_cur, y_tail_cur
    
    draw_figure(AMOUNT_FIN, x_fin_cur[: AMOUNT_FIN], y_fin_cur[: AMOUNT_FIN], 2)
    draw_figure(AMOUNT_FIN, x_fin_cur[AMOUNT_FIN :], y_fin_cur[AMOUNT_FIN :], 2)

    draw_figure(AMOUNT_TAIL, x_tail_cur, y_tail_cur, 2)
    
    draw_figure(AMOUNT_OVAL, x_oval_cur, y_oval_cur, 0)
    
    draw_figure(AMOUNT_CIRCLE, x_circle_cur, y_circle_cur, 0)

    draw_figure(AMOUNT_MOUTH, x_mouth_cur, y_mouth_cur, 0)

    draw_figure(AMOUNT_EYE, x_eye_cur, y_eye_cur, 1)

    
def draw_figure(number, x_arr, y_arr, flag):
    global canv

    if flag == 0:
        color = 'orangered'
        width_t = 4
    elif flag == 1:
        color = 'black'
        width_t = 3
    else:
        color = 'firebrick'
        width_t = 3
        
    for i in range(number - 1):
        canv.create_line(transf_x(x_arr[i]), transf_y(y_arr[i]),
                         transf_x(x_arr[i + 1]), transf_y(y_arr[i + 1]),
                         fill = color, width = width_t)
    if flag == 1:
        canv.create_line(transf_x(x_arr[0]), transf_y(y_arr[0]),
                         transf_x(x_arr[number - 1]),
                         transf_y(y_arr[number - 1]),
                         fill = color, width = width_t)

def move_by(x, y, dx, dy):
    return x + dx, y + dy

def rotate_by(x, y, x_center, y_center, a):
    x1 = x_center + (x - x_center)*cos(a) + (y - y_center)*sin(a)
    y1 = y_center + (y - y_center)*cos(a) + (x_center - x)*sin(a)
    return x1, y1
    
def scale_by(x, y, kx, ky, x_center, y_center):
    x1 = kx*x + (1 - kx)*x_center
    y1 = ky*y + (1 - ky)*y_center
    return x1, y1

def proccess_moving(event = 0):
    global FLAG_ACTIVE
    FLAG_ACTIVE = 1
    
    global entry_dx, entry_dy
    global dx, dy

    global x_oval_prev, y_oval_prev
    global x_oval_cur, y_oval_cur
    
    global x_circle_prev, y_circle_prev
    global x_circle_cur, y_circle_cur
    
    global x_eye_prev, y_eye_prev
    global x_eye_cur, y_eye_cur
    
    global x_mouth_prev, y_mouth_prev
    global x_mouth_cur, y_mouth_cur
    
    global x_fin_prev, y_fin_prev
    global x_fin_cur, y_fin_cur
    
    global x_tail_prev, y_tail_prev
    global x_tail_cur, y_tail_cur

    dx = entry_dx.get()
    dy = entry_dy.get()

    if (is_correct_move() == FAILURE): return

    change_center(X_CUR + dx, Y_CUR + dy)
    
    x_oval_prev, y_oval_prev = change_array(x_oval_prev, y_oval_prev,
                                            x_oval_cur, y_oval_cur)
    x_circle_prev, y_circle_prev = change_array(x_circle_prev, y_circle_prev,
                                                x_circle_cur, y_circle_cur)
    x_eye_prev, y_eye_prev = change_array(x_eye_prev, y_eye_prev,
                                          x_eye_cur, y_eye_cur)
    x_mouth_prev, y_mouth_prev = change_array(x_mouth_prev, y_mouth_prev,
                                              x_mouth_cur, y_mouth_cur)
    x_fin_prev, y_fin_prev = change_array(x_fin_prev, y_fin_prev,
                                          x_fin_cur, y_fin_cur)
    x_tail_prev, y_tail_prev = change_array(x_tail_prev, y_tail_prev,
                                            x_tail_cur, y_tail_cur)

    for i in range(AMOUNT_OVAL):
        x_oval_cur[i],y_oval_cur[i] = move_by(x_oval_cur[i], y_oval_cur[i],
                                                  dx, dy)
    for i in range(AMOUNT_CIRCLE):
        x_circle_cur[i],y_circle_cur[i] = move_by(x_circle_cur[i],y_circle_cur[i],
                                                  dx, dy)
    for i in range(AMOUNT_FIN * 2):
        x_fin_cur[i], y_fin_cur[i] = move_by(x_fin_cur[i], y_fin_cur[i],
                                             dx, dy)
    for i in range(AMOUNT_EYE):
        x_eye_cur[i], y_eye_cur[i] = move_by(x_eye_cur[i], y_eye_cur[i],
                                             dx, dy)
    for i in range(AMOUNT_MOUTH):
        x_mouth_cur[i], y_mouth_cur[i] = move_by(x_mouth_cur[i],
                                                 y_mouth_cur[i], dx, dy)
    for i in range(AMOUNT_TAIL):
        x_tail_cur[i], y_tail_cur[i] = move_by(x_tail_cur[i],
                                               y_tail_cur[i], dx, dy)

    clean_canvas()
    
    draw_fish()

def oval(t, a, b, x_c, y_c):
    x = a*cos(radians(t)) + x_c
    y = b*sin(radians(t)) + y_c
    return x, y

def first_derivative(t, a, b):
    return -a*sin(t), b*cos(t)

def second_derivative(t, a, b):
    return -a*cos(t), -b*sin(t)
    
def predraw_oval(a, b, x_arr, y_arr, x_c, y_c, flag):
    x_frst, y_frst = first_derivative(pi/4, a, b)
    x_scnd, y_scnd = second_derivative(pi/4, a, b)
    k = abs(x_frst * y_scnd - x_scnd * y_frst)/pow(x_frst**2 + y_frst**2, 3/2)
    #k += 0.2
    k += 0.1
    i = 0
    ind = 0
    while i < NUM:
        x_arr[ind], y_arr[ind] = oval(i, a, b, x_c, y_c)
        i = k * ind
        ind += 1
        
    draw_figure(ind, x_arr, y_arr, flag)
    print(ind)

    return ind

def predraw_oval_special(a, b, x_arr, y_arr, x_c, y_c, flag):
    x_frst, y_frst = first_derivative(pi/4, a, b)
    x_scnd, y_scnd = second_derivative(pi/4, a, b)
    k = abs(x_frst * y_scnd - x_scnd * y_frst)/pow(x_frst**2 + y_frst**2, 3/2)
    #k += 0.2
    k += 0.1
    i = -145
    ind = 0
    while i < 145:
        x_arr[ind], y_arr[ind] = oval(i, a, b, x_c, y_c)
        i = k * ind - 145
        ind += 1
        
    draw_figure(ind, x_arr, y_arr, flag)
    print(ind)

    return ind
    
def start_condition(event = 0):
    clean_canvas()
    change_center(X_C, Y_C)
    change_entry_center()
    if FLAG_ACTIVE == 0:
        entry_dx.insert(0, 0)
        entry_dy.insert(0, 0)
    
    draw_axes()
    
    draw_figure(AMOUNT_FIN, x_fin[: AMOUNT_FIN], y_fin[: AMOUNT_FIN], 2)
    draw_figure(AMOUNT_FIN, x_fin[AMOUNT_FIN :], y_fin[AMOUNT_FIN :], 2)

    draw_figure(AMOUNT_TAIL, x_tail, y_tail, 2)
    
    global x_oval, y_oval
    global AMOUNT_OVAL

    #AMOUNT_OVAL = predraw_oval(A, B, x_oval, y_oval, 0, 0, 0)
    AMOUNT_OVAL = predraw_oval_special(A, B, x_oval, y_oval, 0, 0, 0)

    global x_circle, y_circle
    global AMOUNT_CIRCLE

    AMOUNT_CIRCLE = predraw_oval(R_HEAD, R_HEAD, x_circle, y_circle, -4.45, 0, 0)

    global x_eye, y_eye
    global AMOUNT_EYE

    AMOUNT_EYE = predraw_oval(R_EYE, R_EYE, x_eye, y_eye, -5, 0.4, 1)

    draw_figure(AMOUNT_MOUTH, x_mouth, y_mouth, 0)


    global x_oval_cur, y_oval_cur
    global x_circle_cur, y_circle_cur
    global x_fin_cur, y_fin_cur
    global x_eye_cur, y_eye_cur
    global x_mouth_cur, y_mouth_cur
    global x_tail_cur, y_tail_cur
    
    x_oval_cur, y_oval_cur = change_array(x_oval_cur, y_oval_cur,
                                          x_oval, y_oval)
    x_circle_cur, y_circle_cur = change_array(x_circle_cur, y_circle_cur,
                                          x_circle, y_circle)
    x_fin_cur, y_fin_cur = change_array(x_fin_cur, y_fin_cur,
                                          x_fin, y_fin)
    x_eye_cur, y_eye_cur = change_array(x_eye_cur, y_eye_cur,
                                          x_eye, y_eye)
    x_mouth_cur, y_mouth_cur = change_array(x_mouth_cur, y_mouth_cur,
                                          x_mouth, y_mouth)
    x_tail_cur, y_tail_cur = change_array(x_tail_cur, y_tail_cur,
                                          x_tail, y_tail)

def proccess_rotating(event = 0):
    global FLAG_ACTIVE
    FLAG_ACTIVE = 1

    global entry_degrees
    global degrees

    degrees = entry_degrees.get()

    if (is_correct_degrees() == FAILURE): return
    
    degrees = radians(float(-degrees))

    global entry_center_x, entry_center_y
    global X_CENTER_R, Y_CENTER_R

    X_CENTER_R = entry_center_x.get()
    Y_CENTER_R = entry_center_y.get()

    if (is_correct_rot() == FAILURE): return
    
    global x_oval_prev, y_oval_prev
    global x_oval_cur, y_oval_cur
    
    global x_circle_prev, y_circle_prev
    global x_circle_cur, y_circle_cur
    
    global x_eye_prev, y_eye_prev
    global x_eye_cur, y_eye_cur
    
    global x_mouth_prev, y_mouth_prev
    global x_mouth_cur, y_mouth_cur
    
    global x_fin_prev, y_fin_prev
    global x_fin_cur, y_fin_cur
    
    global x_tail_prev, y_tail_prev
    global x_tail_cur, y_tail_cur

    x_oval_prev, y_oval_prev = change_array(x_oval_prev, y_oval_prev,
                                            x_oval_cur, y_oval_cur)
    x_circle_prev, y_circle_prev = change_array(x_circle_prev, y_circle_prev,
                                                x_circle_cur, y_circle_cur)
    x_eye_prev, y_eye_prev = change_array(x_eye_prev, y_eye_prev,
                                          x_eye_cur, y_eye_cur)
    x_mouth_prev, y_mouth_prev = change_array(x_mouth_prev, y_mouth_prev,
                                              x_mouth_cur, y_mouth_cur)
    x_fin_prev, y_fin_prev = change_array(x_fin_prev, y_fin_prev,
                                          x_fin_cur, y_fin_cur)
    x_tail_prev, y_tail_prev = change_array(x_tail_prev, y_tail_prev,
                                            x_tail_cur, y_tail_cur)

    for i in range(AMOUNT_OVAL):
        x_oval_cur[i],y_oval_cur[i] = rotate_by(x_oval_cur[i], y_oval_cur[i],
                                                X_CENTER_R, Y_CENTER_R, degrees)
    for i in range(AMOUNT_CIRCLE):
        x_circle_cur[i],y_circle_cur[i] = rotate_by(x_circle_cur[i],y_circle_cur[i],
                                                  X_CENTER_R, Y_CENTER_R, degrees)
    for i in range(AMOUNT_FIN * 2):
        x_fin_cur[i], y_fin_cur[i] = rotate_by(x_fin_cur[i], y_fin_cur[i],
                                             X_CENTER_R, Y_CENTER_R, degrees)
    for i in range(AMOUNT_EYE):
        x_eye_cur[i], y_eye_cur[i] = rotate_by(x_eye_cur[i], y_eye_cur[i],
                                             X_CENTER_R, Y_CENTER_R, degrees)
    for i in range(AMOUNT_MOUTH):
        x_mouth_cur[i], y_mouth_cur[i] = rotate_by(x_mouth_cur[i], y_mouth_cur[i],
                                                   X_CENTER_R, Y_CENTER_R, degrees)
    for i in range(AMOUNT_TAIL):
        x_tail_cur[i], y_tail_cur[i] = rotate_by(x_tail_cur[i], y_tail_cur[i],
                                                 X_CENTER_R, Y_CENTER_R, degrees)
    x, y = rotate_by(X_CUR, Y_CUR, X_CENTER_R, Y_CENTER_R, degrees)
    change_center(x, y)
    
    clean_canvas()
    
    draw_fish()

def proccess_scaling(event = 0):
    global FLAG_ACTIVE
    FLAG_ACTIVE = 1

    global entry_scale_x, entry_scale_y
    global kx, ky
    
    kx = entry_scale_x.get()
    ky = entry_scale_y.get()

    if (is_correct_k() == FAILURE): return

    global entry_center_x, entry_center_y
    global X_CENTER_R, Y_CENTER_R

    X_CENTER_R = entry_center_x.get()
    Y_CENTER_R = entry_center_y.get()

    if (is_correct_rot() == FAILURE): return

    global x_oval_prev, y_oval_prev
    global x_oval_cur, y_oval_cur
    
    global x_circle_prev, y_circle_prev
    global x_circle_cur, y_circle_cur
    
    global x_eye_prev, y_eye_prev
    global x_eye_cur, y_eye_cur
    
    global x_mouth_prev, y_mouth_prev
    global x_mouth_cur, y_mouth_cur
    
    global x_fin_prev, y_fin_prev
    global x_fin_cur, y_fin_cur
    
    global x_tail_prev, y_tail_prev
    global x_tail_cur, y_tail_cur

    x_oval_prev, y_oval_prev = change_array(x_oval_prev, y_oval_prev,
                                            x_oval_cur, y_oval_cur)
    x_circle_prev, y_circle_prev = change_array(x_circle_prev, y_circle_prev,
                                                x_circle_cur, y_circle_cur)
    x_eye_prev, y_eye_prev = change_array(x_eye_prev, y_eye_prev,
                                          x_eye_cur, y_eye_cur)
    x_mouth_prev, y_mouth_prev = change_array(x_mouth_prev, y_mouth_prev,
                                              x_mouth_cur, y_mouth_cur)
    x_fin_prev, y_fin_prev = change_array(x_fin_prev, y_fin_prev,
                                          x_fin_cur, y_fin_cur)
    x_tail_prev, y_tail_prev = change_array(x_tail_prev, y_tail_prev,
                                            x_tail_cur, y_tail_cur)
         
    for i in range(AMOUNT_OVAL):
        x_oval_cur[i],y_oval_cur[i] = scale_by(x_oval_cur[i], y_oval_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)
    for i in range(AMOUNT_CIRCLE):
        x_circle_cur[i],y_circle_cur[i] = scale_by(x_circle_cur[i],y_circle_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)
    for i in range(AMOUNT_FIN * 2):
        x_fin_cur[i], y_fin_cur[i] = scale_by(x_fin_cur[i], y_fin_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)
    for i in range(AMOUNT_EYE):
        x_eye_cur[i], y_eye_cur[i] = scale_by(x_eye_cur[i], y_eye_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)
    for i in range(AMOUNT_MOUTH):
        x_mouth_cur[i], y_mouth_cur[i] = scale_by(x_mouth_cur[i], y_mouth_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)
    for i in range(AMOUNT_TAIL):
        x_tail_cur[i], y_tail_cur[i] = scale_by(x_tail_cur[i], y_tail_cur[i],
                                             kx, ky, X_CENTER_R, Y_CENTER_R)

    x, y = scale_by(X_CUR, Y_CUR, kx, ky, X_CENTER_R, Y_CENTER_R)
    change_center(x, y)
    
    clean_canvas()
    
    draw_fish()    

# Перевод в новую систему координат
def transf_x(x):
    return (x - X_MIN)/(X_MAX - X_MIN) * canvas_x

def transf_y(y):
    return (Y_MAX - y)/(Y_MAX - Y_MIN) * canvas_y

FLAG_ACTIVE = 0

Y_MAX = 20
Y_MIN = -20
X_MAX = 30
X_MIN = -30
NUM = 360
AMOUNT_OVAL = 0
AMOUNT_CIRCLE = 0
AMOUNT_EYE = 0
AMOUNT_TAIL = 6
AMOUNT_FIN = 4
AMOUNT_MOUTH = 2

FAILURE = -1

X_C = 0
Y_C = 0
X_CUR = 0
Y_CUR = 0
X_PREV = 0
Y_PREV = 0

X_CENTER_R = 0
Y_CENTER_R = 0


dx = None
dy = None
kx = None
ky = None
degrees = None

A = 6
B = 2.5
R_HEAD = 1.5
R_EYE = 0.25

x_oval = [0] * 2000
y_oval = [0] * 2000
x_circle = [0] * 1000
y_circle = [0] * 1000
x_eye = [0] * 500
y_eye = [0] * 500
x_mouth = [ -5.2, -4 ]
y_mouth = [ -0.8, -0.8 ]
x_fin = [ -3, -1.8, 3.5, 2.4, -3.0, -1.8,  3.5,  2.4 ]
y_fin = [ 2.15, 5.0, 5.0, 2.3, -2.15, -4.0, -4.0, -2.3 ]
x_tail = [ 5.72, 7.5, 11.5,  9, 11.0, 5.52 ]
y_tail = [ 0.72, 4.0, 4.0, 0.67, -1.0, -1.0 ]

x_oval_cur = [0] * 3000
y_oval_cur = [0] * 3000
x_circle_cur = [0] * 3000
y_circle_cur = [0] * 3000
x_eye_cur = [0] * 500
y_eye_cur = [0] * 500
x_mouth_cur = [0] * 2
y_mouth_cur = [0] * 2
x_fin_cur = [0] * 8
y_fin_cur = [0] * 8
x_tail_cur = [0] * 6
y_tail_cur = [0] * 6

x_oval_prev = [0] * 3000
y_oval_prev = [0] * 3000
x_circle_prev = [0] * 3000
y_circle_prev = [0] * 3000
x_eye_prev = [0] * 500
y_eye_prev = [0] * 500
x_mouth_prev = [0] * 2
y_mouth_prev = [0] * 2
x_fin_prev = [0] * 8
y_fin_prev = [0] * 8
x_tail_prev = [0] * 6
y_tail_prev = [0] * 6

    
window = Tk()

frame_1 = Frame(window, width = 200, height = 110, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_2 = Frame(window, width = 200, height = 110, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_3 = Frame(window, width = 200, height = 80, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_4 = Frame(window, width = 200, height = 145, highlightbackground =
                'lightblue', highlightthickness = 2)
frame_5 = Frame(window, width = 200, height = 110, highlightbackground =
                'lightblue', highlightthickness = 2)

label = Label(frame_1, text = 'Центр поворота/', font = 'Times 13 bold')
label.place(x = 10, y = 5)
label = Label(frame_1, text = 'масштабирования', font = 'Times 13 bold')
label.place(x = 25, y = 25)

label = Label(frame_1, text = 'x' + ' '*18 + 'y', font = 'Times 13 bold')
label.place(x = 40, y = 45)

label = Label(frame_1, text = '[', font = 'Times 15 bold')
label.place(x = 10, y = 63)

entry_center_x = Entry(frame_1, width = 5, font = 'Times 13 bold')
entry_center_x.place(x = 25, y = 68)

label = Label(frame_1, text = ';', font = 'Times 15 bold')
label.place(x = 80, y = 63)

entry_center_y = Entry(frame_1, width = 5, font = 'Times 13 bold')
entry_center_y.place(x = 100, y = 68)

label = Label(frame_1, text = ']', font = 'Times 15 bold')
label.place(x = 153, y = 63)


label = Label(frame_2, text = 'Перенос на:', font = 'Times 13 bold')
label.place(x = 10, y = 5)

label = Label(frame_2, text = 'dx ', font = 'Times 13 bold')
label.place(x = 20, y = 35)

entry_dx = Entry(frame_2, width = 5, font = 'Times 13 bold')
entry_dx.place(x = 50, y = 35)

label = Label(frame_2, text = 'dy ', font = 'Times 13 bold')
label.place(x = 20, y = 65)

entry_dy = Entry(frame_2, width = 5, font = 'Times 13 bold')
entry_dy.place(x = 50, y = 65)

btn_ok_move = Button(frame_2, text = 'Применить', font = 'Times 10 bold',
                bg = 'lightgray')
btn_ok_move.bind('<Button-1>', proccess_moving)
btn_ok_move.bind('<Return>', proccess_moving)
btn_ok_move.place(x = 110, y = 50)


label = Label(frame_3, text = 'Поворот на:', font = 'Times 13 bold')
label.place(x = 10, y = 5)

entry_degrees = Entry(frame_3, width = 5, font = 'Times 13 bold')
entry_degrees.place(x = 30, y = 35)

label = Label(frame_3, text = '°', font = 'Times 14 bold')
label.place(x = 85, y = 25)

btn_ok_move = Button(frame_3, text = 'Применить', font = 'Times 10 bold',
                bg = 'lightgray')
btn_ok_move.bind('<Button-1>', proccess_rotating)
btn_ok_move.bind('<Return>', proccess_rotating)
btn_ok_move.place(x = 110, y = 33)


label = Label(frame_4, text = 'Масштабирование:', font = 'Times 13 bold')
label.place(x = 10, y = 5)

label = Label(frame_4, text = 'по х в', font = 'Times 13 bold')
label.place(x = 20, y = 35)

entry_scale_x = Entry(frame_4, width = 5, font = 'Times 13 bold')
entry_scale_x.place(x = 75, y = 35)

label = Label(frame_4, text = 'раз/а', font = 'Times 13 bold')
label.place(x = 120, y = 35)

label = Label(frame_4, text = 'по y в', font = 'Times 13 bold')
label.place(x = 20, y = 65)

entry_scale_y = Entry(frame_4, width = 5, font = 'Times 13 bold')
entry_scale_y.place(x = 75, y = 65)

label = Label(frame_4, text = 'раз/а', font = 'Times 13 bold')
label.place(x = 120, y = 65)

btn_ok_move = Button(frame_4, text = 'Применить', font = 'Times 10 bold',
             bg = 'lightgray')
btn_ok_move.bind('<Button-1>', proccess_scaling)
btn_ok_move.bind('<Return>', proccess_scaling)
btn_ok_move.place(x = 110, y = 100)


btn_prev_pos = Button(frame_5, text = 'Предыдущее изображение',
                     font = 'Times 10 bold', width = 25, bg = 'lightgray')
btn_prev_pos.bind('<Button-1>', prev_moving)
btn_prev_pos.bind('<Return>', prev_moving)
btn_prev_pos.place(x = 4, y = 7)

btn_basic = Button(frame_5, text = 'Исходное изображение',
                   font = 'Times 10 bold', width = 25, bg = 'lightgray')
btn_basic.bind('<Button-1>', start_condition)
btn_basic.bind('<Return>', start_condition)
btn_basic.place(x = 4, y = 40)

btn_basic = Button(frame_5, text = 'Центр фигуры', width = 25,
                   font = 'Times 10 bold', bg = 'lightgray')
btn_basic.bind('<Button-1>', center_figure)
btn_basic.bind('<Return>', center_figure)
btn_basic.place(x = 4, y = 73)


label = Label(window, text = 'Изображение', font = 'Times 13 bold')
label.place(x = 210, y = 7)

canvas_x = 780
canvas_y = 525
canv = Canvas(window, width = canvas_x, height = canvas_y,
              bg = 'paleturquoise')


# Размеры окна
window.geometry('1000x580')

# Вывод меню сверху окна
main_menu = Menu(window)

main_menu.add_cascade(label = 'Условие задачи', command = task_information)
main_menu.add_cascade(label = 'Дополнительная информация',
                      command = additional_information)
window.config(menu = main_menu)

frame_1.place(x = 2, y = 115)
frame_2.place(x = 2, y = 2)
frame_3.place(x = 2, y = 228)
frame_4.place(x = 2, y = 311)
frame_5.place(x = 2, y = 459)

canv.place(x = 210, y = 40)
    
start_condition()

window.mainloop()
