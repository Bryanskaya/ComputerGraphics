import sys
from my_gui import *

app, application = None, None

BASIC_LINE = 0
HOR_VER_LINE = 1

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = GuiMainWin()
        self.ui.setupUi(self)

    def mousePressEvent(self, event):
        x, y = self.ui.transform(event.pos().x(), event.pos().y())
        print('points ', x, y)

        if event.button() == Qt.LeftButton:
            self.ui.draw_line(x, y, BASIC_LINE)
        elif event.button() == Qt.RightButton:
            self.ui.draw_line(x, y, HOR_VER_LINE)

        '''if self.ui.is_figure:
            self.ui.draw_figure(x, y)
        elif self.ui.count_cut < 10:
            if event.button() == Qt.LeftButton:
                self.ui.draw_line(x, y)
            elif event.button() == Qt.RightButton:
                self.ui.draw_ver_hor_line(x, y)'''

def main():
    global app, application
    app = QtWidgets.QApplication([])
    application = MainWin()
    application.show()

    sys.exit(app.exec())

main()