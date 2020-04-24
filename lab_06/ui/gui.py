# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(160, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ColorLabel = QtWidgets.QPushButton(self.centralwidget)
        self.ColorLabel.setEnabled(False)
        self.ColorLabel.setGeometry(QtCore.QRect(100, 140, 61, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.ColorLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ColorLabel.setFont(font)
        self.ColorLabel.setMouseTracking(False)
        self.ColorLabel.setText("")
        self.ColorLabel.setDefault(False)
        self.ColorLabel.setFlat(False)
        self.ColorLabel.setObjectName("ColorLabel")
        self.ChangeColor = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeColor.setGeometry(QtCore.QRect(170, 140, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ChangeColor.setFont(font)
        self.ChangeColor.setObjectName("ChangeColor")
        self.CleanScreen = QtWidgets.QPushButton(self.centralwidget)
        self.CleanScreen.setGeometry(QtCore.QRect(130, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.CleanScreen.setFont(font)
        self.CleanScreen.setObjectName("CleanScreen")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(260, 50, 531, 531))
        self.graphicsView.setObjectName("graphicsView")
        self.AnalyzeTime = QtWidgets.QPushButton(self.centralwidget)
        self.AnalyzeTime.setGeometry(QtCore.QRect(10, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.AnalyzeTime.setFont(font)
        self.AnalyzeTime.setObjectName("AnalyzeTime")
        self.LockLine = QtWidgets.QPushButton(self.centralwidget)
        self.LockLine.setGeometry(QtCore.QRect(10, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LockLine.setFont(font)
        self.LockLine.setObjectName("LockLine")
        self.FillFig = QtWidgets.QPushButton(self.centralwidget)
        self.FillFig.setGeometry(QtCore.QRect(130, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FillFig.setFont(font)
        self.FillFig.setObjectName("FillFig")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ChangeColorEdges = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeColorEdges.setGeometry(QtCore.QRect(170, 190, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ChangeColorEdges.setFont(font)
        self.ChangeColorEdges.setObjectName("ChangeColorEdges")
        self.ColorLabelEdges = QtWidgets.QPushButton(self.centralwidget)
        self.ColorLabelEdges.setEnabled(False)
        self.ColorLabelEdges.setGeometry(QtCore.QRect(100, 190, 61, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 14, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.ColorLabelEdges.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ColorLabelEdges.setFont(font)
        self.ColorLabelEdges.setMouseTracking(False)
        self.ColorLabelEdges.setText("")
        self.ColorLabelEdges.setDefault(False)
        self.ColorLabelEdges.setFlat(False)
        self.ColorLabelEdges.setObjectName("ColorLabelEdges")
        self.Delay = QtWidgets.QSlider(self.centralwidget)
        self.Delay.setGeometry(QtCore.QRect(90, 250, 160, 19))
        self.Delay.setMaximum(100)
        self.Delay.setOrientation(QtCore.Qt.Horizontal)
        self.Delay.setObjectName("Delay")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 230, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 230, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 110, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Алгоритм заполнения со списком рёбер и флагом"))
        self.label.setText(_translate("MainWindow", "Цвет"))
        self.label_2.setText(_translate("MainWindow", "заполнения:"))
        self.ChangeColor.setText(_translate("MainWindow", "Изменить"))
        self.CleanScreen.setText(_translate("MainWindow", "Очистить экран"))
        self.AnalyzeTime.setText(_translate("MainWindow", "Анализ времени"))
        self.LockLine.setText(_translate("MainWindow", "Замкнуть ломаную"))
        self.FillFig.setToolTip(_translate("MainWindow", "Укажите затравочный пиксель"))
        self.FillFig.setText(_translate("MainWindow", "Закрасить"))
        self.label_3.setText(_translate("MainWindow", "Цвет"))
        self.label_4.setText(_translate("MainWindow", "рёбер:"))
        self.ChangeColorEdges.setText(_translate("MainWindow", "Изменить"))
        self.label_5.setText(_translate("MainWindow", "Задержка"))
        self.label_6.setText(_translate("MainWindow", "минимум"))
        self.label_7.setText(_translate("MainWindow", "максимум"))
        self.label_8.setText(_translate("MainWindow", "Ввод вершины: ЛКМ"))
        self.label_9.setText(_translate("MainWindow", "Ввод вертикальных/"))
        self.label_10.setText(_translate("MainWindow", "горизонтальных линий: ПКМ"))
