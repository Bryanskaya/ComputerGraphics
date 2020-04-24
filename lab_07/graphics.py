class Cut(object):
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    def __init__(self, point_1, point_2):
        self.x1, self.y1 = point_1[0], point_1[1]
        self.x2, self.y2 = point_2[0], point_2[1]

def add_cut(cuts_arr, point_1, point_2):
    new_cut = Cut(point_1, point_2)
    cuts_arr.append(new_cut)

    '''for i in range(len(cuts_arr)):
        print(cuts_arr[i].x1, cuts_arr[i].y1,
              cuts_arr[i].x2, cuts_arr[i].y2)'''
