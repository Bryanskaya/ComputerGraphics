import sys
from my_gui import *

app, application = None, None

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = GuiMainWin()
        self.ui.setupUi(self)

    def mousePressEvent(self, event):
        x, y = self.ui.transform(event.pos().x(), event.pos().y())
        if self.ui.point:
            self.ui.filling(x, y)
            return
        if event.button() == Qt.LeftButton:
            self.ui.draw_line(x, y)
        elif event.button() == Qt.RightButton:
            x, y = self.ui.draw_ver_hor_line(x, y)

        if self.ui.new_part:
            if self.ui.scene.point_temp == None:
                self.ui.scene.point_temp = (x, y)
                #else add stack
            self.ui.scene.point_temp = (x, y)

def main():
    global app, application
    app = QtWidgets.QApplication([])
    application = MainWin()
    application.show()

    sys.exit(app.exec())

main()