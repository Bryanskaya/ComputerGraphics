from tkinter import*
import tkinter.messagebox as box
from math import*
import numpy as np
import matplotlib.pyplot as plt

# Условие задачи
def task_information():
    box.showinfo('Условие задачи', 'На плоскости дано множество точек. '
                 'Найти такой треугольник, у которого угол между биссектрисой '
                 'и высотой, выходящими из одной вершины, максимален.'
                 '\n\n(Для каждого треугольника рассматривать все три вершины '
                 'и выбирать максимальное значение угла и номер вершины '
                 'для вывода в графическое режиме)'
                 '\n\nСделать вывод изображения в графическом режиме.')

def additional_information():
    box.showinfo('Дополнительная информация', '1. Количество точек должно быть '
                 'не меньше, чем 3 (так как рассматриваются треугольники) и '
                 'не больше, чем 10. \n2. Координаты представляют собой '
                 'вещественные числа. \n3. В процессе работы даётся возможность '
                 'редактирование числа точек, путём нажатия на соответствующую '
                 'кнопку.')

# Считывание количества точек
def count_amount():
    global amount
    amount = entry_amount.get()


# Очистка содержимого поля ввода количества точек
def clean_entry_amount():
    global entry_amount
    entry_amount.delete(0, END)

# Очистка поля ответа
def clean_frame_answer():
    global frame_3

    frame_3.place_forget()
    frame_3 = Frame(window, width = 450, height = 250)
    frame_3.place(x = 10, y = 300)

    
# Очистка всего, кроме окна ввода количества точек
def clean_frame():
    # Очистка таблицы координат
    global frame_1
    global frame_2
    global frame_3
    
    frame_1.place_forget()
    frame_1 = Frame(window, width = 450, height = 250)
    frame_1.place(x = 10, y = 35)

    frame_2.place_forget()
    frame_2 = Frame(window, width = 180, height = 250)
    frame_2.place(x = 370, y = 35)

    frame_3.place_forget()
    frame_3 = Frame(window, width = 450, height = 250)
    frame_3.place(x = 10, y = 300)

    global btn_sol
    if btn_sol:
        btn_sol.destroy()

    global canv

    canv.delete("all")
    canv = Canvas(window, width = canvas_x, height = canvas_y, bg = 'white')
    canv.place(x = 500, y = 40)


# Заполнение массивов координат
def fill_arrays():
    global points_x
    global points_y

    points_x = []
    points_y = []

    # Считывание абсцисс и ординат точек
    string = text_x.get(1.0, END)
    string = string.split('\n')
    points_x = string[:-1]

    if check_points(CHECK_X, points_x) == False:
        points_x = points_x[:amount]
        rewrite(CHECK_X, points_x)
    transform(amount, points_x)
    if flag:    
        string = text_y.get(1.0, END)
        string = string.split('\n')
        points_y = string[:-1]
    
        if check_points(CHECK_Y, points_y) == False:
            points_y = points_y[:amount]
            rewrite(CHECK_Y, points_y)
        transform(amount, points_y)
        if flag: return CORRECT
        else:
            return MISTAKE
    return MISTAKE

    
def processing_points(event = 0):
    global canv

    canv.delete("all")
    clean_frame_answer()
    
    global amount
    count_amount()

    try:
        amount = int(amount)
        if 0 < amount < MIN_AMOUNT_POINTS:
            box.showwarning('Ошибка', 'Недостаточное количество точек'
                            '\nНельзя построить треугольник')
            clean_entry_amount()
            clean_frame()
        elif amount < 1:
            box.showwarning('Ошибка', 'Некорректный ввод количества точек')
            clean_entry_amount()
            clean_frame()
        elif amount > MAX_AMOUNT_POINTS:
            box.showwarning('Ошибка', 'Количество точек больше оговорённого '
                            'максимального значения')
            clean_entry_amount()
            clean_frame()
        elif amount > 2:
            add_table_for_points()
    except:
        box.showwarning('Ошибка', 'Некорректный ввод количества точек')
        clean_entry_amount()
        clean_frame()

# Проверка коррекции ввода
def correction():
    x = []
    y = []

    # Считывание абсцисс и ординат точек
    string = text_x.get(1.0, END)
    string = string.split('\n')
    x = string[:-1]

    if check_points(CHECK_X, x) == False:
        box.showwarning('Ошибка', 'Допущена ошибка в координатах точек')
        return False
    transform(amount, x)
    
    if flag:    
        string = text_y.get(1.0, END)
        string = string.split('\n')
        y = string[:-1]
    
        if check_points(CHECK_Y, y) == False:
            box.showwarning('Ошибка', 'Допущена ошибка в координатах точек')
            return False
        transform(amount, y)
        if flag == 0:
            box.showwarning('Ошибка', 'Допущена ошибка в координатах точек')
            return False
        return True
    return False

    
# Проверка на правильность ввода координат точки
def check_points(f, s = [], *s1):
    if len(s) > amount:
        if f:
            box.showwarning('Ошибка',
                            'Число абсцисс больше введенного количества. '
                            '\nЛишние элементы были автоматически удалены.')
        else:
            box.showwarning('Ошибка',
                            'Число ординат больше введенного количества. '
                            '\nЛишние элементы были автоматически удалены.')
        return False
    return True

# Проверка на наличие совпадающих точек
def check_same():
    global points_x
    global points_y
    global amount

    temp = amount

    for i in range(amount - 1):
        for j in range(i + 1, amount):
            if abs(points_x[i] - points_x[j]) < 1e-3 and \
               abs(points_y[i] - points_y[j]) < 1e-3:
                for k in range(j, amount - 1):
                    points_x[k] = points_x[k + 1]
                    points_y[k] = points_y[k + 1]
                amount -= 1
    points_x = points_x[:amount]
    points_y = points_y[:amount]

    if temp != amount:
        box.showwarning('Внание', 'Произошло удаление повторяющихся точек')
        rewrite_all_table()
    if amount < 3:
        box.showwarning('Ошибка', 'Недостаточное количество точек'
                        '(нельзя построить треугольник)')
        return MISTAKE
    return CORRECT


# Проверка на принадлежность одной прямой
def check_one_line():
    for i in range(amount - 2):
        for j in range(i + 1, amount - 1):
            for k in range(j + 1, amount):
                if abs((points_x[k] - points_x[i])*(points_y[j] - points_y[i]) - \
                       (points_x[j] - points_x[i])*(points_y[k] - points_y[i])) > 1e-3:
                    return CORRECT
    return MISTAKE


# Проверка на принадлежность одной прямой 3х точек
def check_one_line_group(x1, y1, x2, y2, x3, y3):
    if abs((x1 - x2)*(y3 - y2) - (x3 - x2)*(y1 - y2)) > 1e-3:
        return CORRECT
    return MISTAKE


# Если введенное число координат больше, чем нужно: автоматическое удаление
# лишних
def rewrite(f, s = [], *s1):
    if f:
        global text_x
        text_x.delete(1.0, END)
        for j in range(amount):
            text_x.insert(END, str(s[j] + '\n'))
    else:
        global text_y
        text_y.delete(1.0, END)
        for j in range(amount):
            text_y.insert(END, str(s[j] + '\n'))


# Перезапись всей таблицы
def rewrite_all_table():
    clean_entry_amount()
    entry_amount.insert(END, str(amount))
    add_table_for_points()
    
    global text_x
    global text_y
    
    for j in range(amount - 1):
        text_x.insert(END, str(str(points_x[j]) + '\n'))
        text_y.insert(END, str(str(points_y[j]) + '\n'))
    text_x.insert(END, str(points_x[amount - 1]))
    text_y.insert(END, str(points_y[amount - 1]))

# Перевод координат в вещественный тип
def transform(n, s = [], *s1):
    global flag
    flag = 1
    for k in range(n):
        try:
            s[k] = float(s[k])
        except:
            box.showwarning('Ошибка', 'Некорректный ввод координат')
            flag = 0
            break


def print_answer():
    global frame_3
    
    label = Label(frame_3, text = 'Ответ: ', font = 'Times 13 bold')
    label.place(x = 0, y = 0)
    
    label = Label(frame_3, text = 'треугольник, удовлетворяющий условию задачи:',
                  font = 'Times 13')
    label.place(x = 60, y = 0)

    label = Label(frame_3, text = '- строится на вершинах с номерами ' +
                  str(numbers_points[0]) + ', ' + str(numbers_points[1])
                  + ', ' + str(numbers_points[2]) + '', font = 'Times 13')
    label.place(x = 20, y = 21)

    label = Label(frame_3, text = '- соответственно кординаты:',
                  font = 'Times 13')
    label.place(x = 20, y = 40)

    label = Label(frame_3, text = '  (' +
                  str(solution_x[0]) + ' ; '  + str(solution_y[0]) + '), ' +
                  '(' + str(solution_x[1]) + ' ; '  + str(solution_y[1]) + '), ' +
                  '(' + str(solution_x[2]) + ' ;'  + str(solution_y[2]) + ')',
                  font = 'Times 13')
    label.place(x = 20, y = 60)
    
    label = Label(frame_3, text = '- биссектриса и высота проводятся из вершины '
                  + str(numbers_points[0]), font = 'Times 13')
    label.place(x = 20, y = 80)

    label = Label(frame_3, text = '- искомый угол равен ' + str(round(solution_corner, 3)) +
                  ' градусов', font = 'Times 13')
    label.place(x = 20, y = 100)

    label = Label(frame_3, text = '- на графике отмечены: ', font = 'Times 13')
    label.place(x = 20, y = 120)

    label = Label(frame_3, text = 'высота ', fg = 'blue', font = 'Times 13')
    label.place(x = 190, y = 120)

    label = Label(frame_3, text = 'биссектриса', fg = 'red', font = 'Times 13')
    label.place(x = 250, y = 120)

    
    
# Вывод на экран полей для ввода координат точек и кнопок
def add_table_for_points():
    global frame_1
    global frame_2
    global text_x
    global text_y
    global btn_add
    global btn_del
    global btn_sol

    # Предварительная чистка только таблицы
    frame_1.place_forget()
    frame_1 = Frame(window, width = 550, height = 300)
    frame_1.place(x = 10, y = 35)
    
    # "Шапка" таблицы
    label1 = Label(frame_1, text = 'Точки: ', font = 'Times 13 bold')
    label1.grid(row = 0, column = 0)

    entry = Entry(frame_1, width = 8, justify = CENTER, font='Times 12 bold')
    entry.insert(0, '№')
    entry.grid(row = 1, column = 0)

    entry = Entry(frame_1, width = 18, justify = CENTER, font='Times 12 bold')
    entry.insert(0, 'Координата х')
    entry.grid(row = 1, column = 1)

    entry = Entry(frame_1, width = 18, justify = CENTER, font='Times 12 bold')
    entry.insert(0, 'Координата y')
    entry.grid(row = 1, column = 2)

    # Сами поля ввода: text_num - для номерации, text_x - для абсцисс,
    # text_y - для ординат
    text_num = Text(frame_1, width = 8, height = amount, font = "Times 12 bold")
    text_num.grid(row = 2, column = 0)

    for k in range(amount):
        text_num.insert(END, str(k + 1) + "\n")

    text_x = Text(frame_1, width = 18, height = amount, font = "Times 12 bold")
    text_x.grid(row = 2, column = 1)

    text_y = Text(frame_1, width = 18, height = amount, font = "Times 12 bold")
    text_y.grid(row = 2, column = 2)


    # кнопка для добавления дополнительных точек
    btn_add = Button(frame_2, text = 'Добавить точку', font = 'Times 10 bold',
                     bg = 'lightgray')
    btn_add.bind('<Button-1>', add_one_point)
    btn_add.bind('<Return>', add_one_point)
    btn_add.place(x = 10, y = 25)

    # кнопка для удаления точек
    btn_del = Button(frame_2, text = 'Удалить точку ', font = 'Times 10 bold',
                     bg = 'lightgray')
    btn_del.bind('<Button-1>', del_point)
    btn_del.bind('<Return>', del_point)
    btn_del.place(x = 10, y = 60)

    # кнопка для запуска поиска решения
    btn_sol = Button(window, text = 'Найти решение ', font = 'Times 10 bold',
                     bd = 3, relief = RIDGE, bg = 'lightgray', fg = 'red')
    btn_sol.bind('<Button-1>', find_solution)
    btn_sol.bind('<Return>', find_solution)
    btn_sol.place(x = 380, y = 10)
    

# Удаление точки по индексу (окно)
def del_point(event = 0):
    if fill_arrays() == MISTAKE:
        return
    
    if amount == 3:
        box.showwarning('Ошибка', 'Удаление строки запрещено'
                        '(не должно быть меньше трёх)')
        return
    
    if correction() == False:
        return
    
    global entry_index
    global window_1
    
    window_1 = Tk()

    # Метка
    label_amount_points = Label(window_1, text = 'Введите номер удаляемой точки: ',
                            font = 'Times 13 bold')
    label_amount_points.place(x = 10, y = 30)

    # Поле ввода количества точек
    entry_index = Entry(window_1, width = 4, font = 'Times 12')
    entry_index.place(x = 285, y = 30)

    # кнопка "Ок" для выпада полей ввода координат точек
    btn_ok_1 = Button(window_1, text = 'Ok', font = 'Times 10 bold', bg = 'lightgray')
    btn_ok_1.bind('<Button-1>', processing_del_point)
    btn_ok_1.bind('<Return>', processing_del_point)
    btn_ok_1.place(x = 325, y = 30)

    window_1.geometry('400x110')

    window_1.mainloop()

    
# Добавление одной точки
def add_one_point(event = 0):
    if fill_arrays() == MISTAKE:
        return
    
    if amount == 10:
        box.showwarning('Ошибка', 'Удаление строки запрещено'
                        '(не должно быть больше десяти)')
        return
    
    if correction() == False:
        return
    
    global entry_add_x
    global entry_add_y
    global window_1
    
    window_1 = Tk()

    # Метка
    label_add_point = Label(window_1, text = 'Введите координаты точки:  [',
                            font = 'Times 13 bold')
    label_add_point.place(x = 10, y = 30)

    # Поле координатs x точки
    entry_add_x = Entry(window_1, width = 4, font = 'Times 12')
    entry_add_x.place(x = 255, y = 30)

    label_add_point = Label(window_1, text = ';', font = 'Times 13 bold')
    label_add_point.place(x = 290, y = 30)

    # Поле координатs y точки
    entry_add_y = Entry(window_1, width = 4, font = 'Times 12')
    entry_add_y.place(x = 310, y = 30)

    label_add_point = Label(window_1, text = ']', font = 'Times 13 bold')
    label_add_point.place(x = 350, y = 30)

    # кнопка "Ок" для выпада полей ввода координат точек
    btn_ok_1 = Button(window_1, text = 'Ok', font = 'Times 10 bold', bg = 'lightgray')
    btn_ok_1.bind('<Button-1>', processing_add_point)
    btn_ok_1.bind('<Return>', processing_add_point)
    btn_ok_1.place(x = 370, y = 30)

    window_1.geometry('410x110')

    window_1.mainloop()
    

# Удаление точки по индексу
def processing_del_point(event = 0):
    global amount
    global entry_index
    index = entry_index.get()

    try:
        index = int(index)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод индекса точки')
        entry_index.delete(0, END)
        return

    if 1 > index or index > amount:
        box.showwarning('Ошибка', 'Несуществующий индекс')
        entry_index.delete(0, END)
        return

    global window_1
    window_1.destroy()
    
    global points_x
    global points_y 
        
    for i in range(index - 1, amount - 1):
        points_x[i] = points_x[i + 1]
        points_y[i] = points_y[i + 1]
    points_x.pop(amount - 1)
    points_y.pop(amount - 1)
    amount -= 1

    rewrite_all_table()


# Удаление точки по индексу
def processing_add_point(event = 0):
    global amount
    global entry_add_x
    global entry_add_y
    
    pos_x = entry_add_x.get()
    pos_y = entry_add_y.get()

    try:
        pos_x = float(pos_x)
        pos_y = float(pos_y)
    except:
        box.showwarning('Ошибка', 'Некорректный ввод координат точки')
        entry_add_x.delete(0, END)
        entry_add_y.delete(0, END)
        return

    global window_1
    window_1.destroy()

    global points_x
    global points_y 
        
    points_x.append(pos_x)
    points_y.append(pos_y)
    amount += 1

    rewrite_all_table()
        

# Заполение массивов для ответа
def fill_solution(i, j, k):
    global solution_x
    global solution_y
    global numbers_points
    
    solution_x.append(points_x[i])
    solution_y.append(points_y[i])

    solution_x.append(points_x[j])
    solution_y.append(points_y[j])
    solution_x.append(points_x[k])
    solution_y.append(points_y[k])

    numbers_points.append(i + 1)
    numbers_points.append(j + 1)
    numbers_points.append(k + 1)
    
def find_solution(event = 0):
    global canv

    canv.delete("all")
    clean_frame_answer()
    
    if fill_arrays() == MISTAKE: return
    if check_same() == MISTAKE: return
    if check_one_line() == MISTAKE:
        box.showwarning('Ошибка', 'Все точки лежат на одной прямой'
                        '\n(нельзя построить треугольник)')
        return
    
    global solution_x
    global solution_y
    global numbers_points
    global solution_corner

    solution_x = []
    solution_y = []
    numbers_points = []

    max_corner = -1

    for i in range(amount - 2):
        for j in range(i + 1, amount - 1):
            for k in range(j + 1, amount):
                if check_one_line_group(points_x[i], points_y[i],
                                     points_x[j], points_y[j],
                                     points_x[k], points_y[k]) == MISTAKE:
                    continue
                
                a = length_side(points_x[i], points_y[i], points_x[j], points_y[j])
                b = length_side(points_x[j], points_y[j], points_x[k], points_y[k])
                c = length_side(points_x[k], points_y[k], points_x[i], points_y[i])


                corner_i = corner(b, a, c)
                corner_j = corner(c, a, b)
                corner_k = corner(a, b, c)

                max_corner_temp = max(corner_i, corner_j, corner_k)

                if max_corner_temp > max_corner:
                    max_corner = max_corner_temp
                    solution_x = []
                    solution_y = []
                    numbers_points = []
                    if abs(max_corner_temp - corner_i) < 1e-5:
                        fill_solution(i, j, k)
                    if abs(max_corner_temp - corner_j) < 1e-5:
                        fill_solution(j, i, k)
                    if abs(max_corner_temp - corner_k) < 1e-5:
                        fill_solution(k, j, i)

                #print('max corner ', max_corner)
                

    solution_corner = max_corner
    print("ok")
    
    print_answer()
    
    print('******', solution_x, solution_y, numbers_points)

    draw()


#------------------------------------------------------------------------------
# Геометрия

# Длина стороны треугольника
def length_side(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Длина биссектрисы, проведенной на основание b
def length_bisector(b_foot, a, c):
    return sqrt(a*c*(a + c - b_foot)*(a + b_foot + c))/(a + c)

# Длина высоты, проведенной на основание b
def length_height(b_foot, a, c):
    return sqrt((a + b_foot + c)*(b_foot + c - a)*(a - b_foot + c)*\
                (a + b_foot - c))/(2*b_foot)

# Угол между биссектрисой и высотой
def corner(b_foot, a, c):
    height = length_height(b_foot, a, c)
    bisector = length_bisector(b_foot, a, c)
    return degrees(acos(round(height / bisector, 15)))

#------------------------------------------------------------------------------
# График

# Перевод в новую систему координат
def transf_x(x):
    return (x - x_min)/(x_max - x_min) * canvas_x

# Перевод в новую систему координат
def transf_y(y):
    return (y_max - y)/(y_max - y_min) * canvas_y

# Рисование
def draw():
    global x_max
    global y_max
    global x_min
    global y_min
    
    a = length_side(solution_x[1], solution_y[1], solution_x[2], solution_y[2])
    b = length_side(solution_x[1], solution_y[1], solution_x[0], solution_y[0])
    c = length_side(solution_x[0], solution_y[0], solution_x[2], solution_y[2])

    # Точка пересечения биссектрисы с основанием 
    x_b = (solution_x[1] + b/c * solution_x[2])/(1 + b/c)
    y_b = (solution_y[1] + b/c * solution_y[2])/(1 + b/c)
    #print('1', x_b, y_b)
    
    # Точка пересечения высоты с основанием
    if b**2 > a**2 + c**2:
        da = sqrt(b ** 2 - length_height(a, b, c) ** 2)
        x_h = (solution_x[2] + (a - da)/da * solution_x[1])/(1 + (a - da)/da)
        y_h = (solution_y[2] + (a - da)/da * solution_y[1])/(1 + (a - da)/da)
    else:
        da = sqrt(c ** 2 - length_height(a, b, c) ** 2)
        if abs(da) < 1e-5:
            x_h = solution_x[2]
            y_h = solution_y[2]
        else:
            x_h = (solution_x[1] + (a - da)/da * solution_x[2])/(1 + (a - da)/da)
            y_h = (solution_y[1] + (a - da)/da * solution_y[2])/(1 + (a - da)/da)
    #print('2', x_h, y_h, length_height(a, b, c))

    x_max = max(solution_x[0], solution_x[1], solution_x[2], x_h)
    y_max = max(solution_y[0], solution_y[1], solution_y[2], y_h)

    x_min = min(solution_x[0], solution_x[1], solution_x[2], x_h)
    y_min = min(solution_y[0], solution_y[1], solution_y[2], y_h)

    # Отступ от краеё поля графика
    x_c = (x_min + x_max)/2
    x_min = x_c - (x_c - x_min)*1.3
    x_max = x_c + (x_max - x_c)*1.3

    y_c = (y_min + y_max)/2
    y_min = y_c - (y_c - y_min)*1.3
    y_max = y_c + (y_max - y_c)*1.3

    # Коэффициенты доли в экране
    kx = (x_max - x_min)/canvas_x
    ky = (y_max - y_min)/canvas_y

    if kx < ky:
        #Координаты центра растяжения
        x_c = (x_min + x_max)/2
        x_min = x_c - (x_c - x_min)*(ky/kx)
        x_max = x_c + (x_max - x_c)*(ky/kx)
    if ky < kx:
        #Координаты центра растяжения
        y_c = (y_min + y_max)/2
        y_min = y_c - (y_c - y_min)*(kx/ky)
        y_max = y_c + (y_max - y_c)*(kx/ky)
        

    # Координатные оси
    canv.create_line(transf_x(x_min), transf_y(0),
                     transf_x(x_max), transf_y(0),
                     fill = 'grey', dash = (4, 2), arrow = 'last')
    canv.create_line(transf_x(0), transf_y(y_min),
                     transf_x(0), transf_y(y_max),
                     fill = 'grey', dash = (4, 2), arrow = 'last')

    # Треугольник
    canv.create_line(transf_x(solution_x[0]), transf_y(solution_y[0]),
                     transf_x(solution_x[1]), transf_y(solution_y[1]),
                     transf_x(solution_x[1]), transf_y(solution_y[1]),
                     transf_x(solution_x[2]), transf_y(solution_y[2]),
                     transf_x(solution_x[2]), transf_y(solution_y[2]),
                     transf_x(solution_x[0]), transf_y(solution_y[0]),
                     fill = 'black', width = 2)

    # Биссектриса
    canv.create_line(transf_x(solution_x[0]), transf_y(solution_y[0]),
                     transf_x(x_b), transf_y(y_b), fill = 'red', width = 2)

    # Высота
    canv.create_line(transf_x(solution_x[0]), transf_y(solution_y[0]),
                     transf_x(x_h), transf_y(y_h), fill = 'blue', width = 2)
    # Продолжение высоты
    if x_h >= solution_x[1] and x_h >= solution_x[2]:
        canv.create_line(transf_x(solution_x[1]), transf_y(solution_y[1]),
                transf_x(x_h), transf_y(y_h), dash = (5, 3), fill = 'grey')
    if x_h < solution_x[1] and x_h < solution_x[2]:
        canv.create_line(transf_x(solution_x[1]), transf_y(solution_y[1]),
                transf_x(x_h), transf_y(y_h), dash = (5, 3), fill = 'grey')

    # Подпись вершин
    x_max_temp = max(solution_x)
    x_min_temp = min(solution_x)
    y_max_temp = max(solution_y)
    y_min_temp = min(solution_y)
    name = ['A', 'B', 'C', 'D', 'H']

    # Высота
    flag = -1
    for i in range(3):
        if abs(x_h - solution_x[i]) < 1e-3 and abs(y_h - solution_y[i]) < 1e-3:
            flag = i
            break
    if flag == -1:
        canv.create_text(transf_x(x_h), transf_y(y_h)+10,
                         text = name[4] + '(' + str(round(x_h, 3)) + ';' +
                         str(round(y_h, 3)) + ')', font = 'Times 9',
                         fill = 'blue')             
    for i in range(3):                
        # Вершин
        if i != flag: color = 'black'
        else: color = 'blue'
        if solution_x[i] == x_max_temp:
            canv.create_text(transf_x(solution_x[i])+25, transf_y(solution_y[i]),
                             text = name[i] + '(' + str(solution_x[i]) + ';' +
                             str(solution_y[i]) + ')', font = 'Times 9',
                             fill = color)
        elif solution_x[i] == x_min_temp:
            canv.create_text(transf_x(solution_x[i])-25, transf_y(solution_y[i]),
                             text = name[i] + '(' + str(solution_x[i]) + ';' +
                             str(solution_y[i]) + ')', font = 'Times 9',
                             fill = color)
        else:
            if solution_y[i] == y_max_temp:
                canv.create_text(transf_x(solution_x[i]), transf_y(solution_y[i])-10,
                                 text = name[i] + '(' + str(solution_x[i]) + ';' +
                                 str(solution_y[i]) + ')', font = 'Times 9',
                                 fill = color)
            elif solution_y[i] == y_min_temp:
                canv.create_text(transf_x(solution_x[i]), transf_y(solution_y[i])+10,
                                 text = name[i] + '(' + str(solution_x[i]) + ';' +
                                 str(solution_y[i]) + ')', font = 'Times 9',
                                 fill = color)
            else:
                canv.create_text(transf_x(solution_x[i]), transf_y(solution_y[i])+10,
                                 text = name[i] + '(' + str(solution_x[i]) + ';' +
                                 str(solution_y[i]) + ')', font = 'Times 9',
                                 fill = color)
        # Биссектриса
        canv.create_text(transf_x(x_b)-15, transf_y(y_b) - 5,
                         text = name[3] + '(' + str(round(x_b, 3)) + ';' +
                         str(round(y_b, 3)) + ')', font = 'Times 9',
                         fill = 'red')

# Объявление глобальных переменных
amount = 0             # Число точек
flag = 1               # Флаг правильности ввода
points_x = []          # Массив абсцисс
points_y = []          # Массив ординат
solution_x = []        # Массив абсцисс нужного треугольника
solution_y = []        # Массив ординат нужного треугольника
numbers_points = []    # Номера вершин, удовлетворяющих условию задачи
solution_corner = None # Искомый угол
text_x = None          # Поле абсцисс
text_y = None          # Поле ординат
btn_add = None         # Кнопка добавления точки
btn_del = None         # Кнопка удаления точки
btn_sol = None         # Кнопка запуска поиска решения
entry_index = None     # Поле ввода индекса удаляемой точки
index = None           # Индекс удаляемой точки
window_1 = None        # Окно удаления
x_max = None           # Максимальлная абсцисса рисунка
y_max = None           # Максимальная ордината рисунка
x_min = None           # Минимальная абсцисса рисунка
y_min = None           # Минимальная ордината рисунка


# Объявление констант
MIN_AMOUNT_POINTS = 3
MAX_AMOUNT_POINTS = 10
CHECK_X = 1
CHECK_Y = 0
CORRECT = 1
MISTAKE = 0

window = Tk()
frame_1 = Frame(window, width = 450, height = 250)  # Таблица
frame_2 = Frame(window, width = 180, height = 250)  # Кнопки добаления/удаления
frame_3 = Frame(window, width = 450, height = 250)  # Поле для ответа



# Метка количества точек
label_amount_points = Label(window, text = 'Количество точек: ',
                            font = 'Times 13 bold')
label_amount_points.place(x = 10, y = 10)

# Поле ввода количества точек
entry_amount = Entry(window, width = 4, font = 'Times 12')
entry_amount.place(x = 175, y = 10)

# кнопка "Ок" для выпада полей ввода координат точек
btn_ok = Button(window, text = 'Ok', font = 'Times 10 bold', bg = 'lightgray')
btn_ok.bind('<Button-1>', processing_points)
btn_ok.bind('<Return>', processing_points)
btn_ok.place(x = 215, y = 10)


canvas_x = 480
canvas_y = 500
canv = Canvas(window, width = canvas_x, height = canvas_y, bg = 'white')

label = Label(window, text = 'Графическая интерпретация: ',
                  font = 'Times 13 bold')
label.place(x = 500, y = 10)
    
canv.place(x = 500, y = 40)


# Размеры окна
window.geometry('1000x600')

# Вывод меню сверху окна
main_menu = Menu(window)

main_menu.add_cascade(label = 'Условие задачи', command = task_information)
main_menu.add_cascade(label = 'Дополнительная информация',
                      command = additional_information)
window.config(menu = main_menu)

# Помещение таблицы с координатами
frame_1.place(x = 10, y = 35)
frame_2.place(x = 370, y = 35)
frame_3.place(x = 10, y = 300)

window.mainloop()
