#
# Copyright 2018 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pattedetable/Python/Interférence et diffraction/Interface/Interference.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog):

        self.figure = plt.figure()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setMinimum(400)
        self.horizontalSlider_3.setMaximum(700)
        self.horizontalSlider_3.setProperty("value", 500)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 7, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 13, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setMinimum(2)
        self.horizontalSlider_2.setMaximum(16)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setProperty("value", 4)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 5, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 3, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 11, 1, 1, 1)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setMinimum(10)
        self.horizontalSlider_4.setMaximum(50)
        self.horizontalSlider_4.setProperty("value", 30)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 9, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 1, 1, 1)

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 4, 1, 1, 1)

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 6, 1, 1, 1)

        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 8, 1, 1, 1)

        self.canvas = FigureCanvas(self.figure)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        #self.canvas.setScaledContents(True)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 2, 12, 1)  # Graphique

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 25))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menuAide.addAction(self.action_propos)
        self.menubar.addAction(self.menuAide.menuAction())

#       Create first graph
        self.comboBox.setCurrentIndex(1)
        self.disableMultipleSlits(1)
        self.disableEnveloppe(1)
        self.Intensite()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.lcdNumber.display(self.horizontalSlider.value())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.disableMultipleSlits(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.lcdNumber.display(self.horizontalSlider.value()))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.Intensite())
        self.lcdNumber_2.display(self.horizontalSlider_2.value()/100)
        self.horizontalSlider_2.valueChanged['int'].connect(lambda: self.lcdNumber_2.display(self.horizontalSlider_2.value()/100))
        self.horizontalSlider_2.valueChanged['int'].connect(lambda: self.Intensite())
        self.lcdNumber_3.display(self.horizontalSlider_3.value())
        self.horizontalSlider_3.valueChanged['int'].connect(lambda: self.lcdNumber_3.display(self.horizontalSlider_3.value()))
        self.horizontalSlider_3.valueChanged['int'].connect(lambda: self.Intensite())
        self.lcdNumber_4.display(self.horizontalSlider_4.value()/100)
        self.horizontalSlider_4.valueChanged['int'].connect(lambda: self.lcdNumber_4.display(self.horizontalSlider_4.value()/100))
        self.horizontalSlider_4.valueChanged['int'].connect(lambda: self.Intensite())
        self.checkBox.clicked.connect(lambda: self.Intensite())
        self.comboBox.currentIndexChanged['QString'].connect(lambda: self.disableEnveloppe(self.comboBox.currentIndex()))
        self.comboBox.currentIndexChanged['QString'].connect(lambda: self.Intensite())
        self.pushButton.clicked.connect(lambda: Dialog.close())
        self.pushButton.clicked.connect(lambda: plt.close())
        self.pushButton.clicked.connect(lambda: MainWindow.close())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interférence et diffraction"))
        self.label_2.setText(_translate("MainWindow", "Nombre de fentes"))
        self.pushButton.setText(_translate("MainWindow", "Quitter"))
        self.label_6.setText(_translate("MainWindow", "Enveloppe de diffraction d'une des fentes"))
        self.label_5.setText(_translate("MainWindow", "Distance entre deux fentes successives (en mm)"))
        self.label_4.setText(_translate("MainWindow", "Longueur d\'onde de la lumière (en nm)"))
        self.label_3.setText(_translate("MainWindow", "Largeur des fentes (en mm)"))
        self.label_1.setText(_translate("MainWindow", "Type de graphique"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Points lumineux"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Intensité"))


    def disableMultipleSlits(self, number):
        if (number == 1):
            self.horizontalSlider_4.setDisabled(True)
        else:
            self.horizontalSlider_4.setDisabled(False)

    def disableEnveloppe(self, number):
        if (number == 0):
            self.checkBox.setDisabled(True)
        else:
            self.checkBox.setDisabled(False)


    def Intensite(self):
        """
        Compute the total intensity due to both the inteference and the diffraction of light going through slits
        """

        N = self.horizontalSlider.value()
        a = self.horizontalSlider_2.value()/100
        l = self.horizontalSlider_3.value()
        d = self.horizontalSlider_4.value()/100
        enveloppe = self.checkBox.isChecked()
        points = self.comboBox.currentIndex()

        self.figure.clear()

        ax1 = self.figure.add_subplot(111)

        if points == 1:
            def Inter(t):
                """
                Intensity of light going through a series of slits due to the interference
                """
                return np.sin(N*np.pi*d*np.sin(np.arctan(t))*1000000/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(t))*1000000/l)**2)


            def Diff(t):
                """
                Intensity of light going through a series of slits due to the diffraction
                """
                return np.sin(np.pi*a*np.sin(np.arctan(t))*1000000/l)**2/((np.pi*a*np.sin(np.arctan(t))*1000000/l)**2)

            t = np.linspace(-0.03, 0.03, 5000)

            ax1.axis([-0.03, 0.03, 0, Inter(0.00000001) + 0.5])
            ax1.grid(False)

        #    plt.xlabel('$θ$ (rad)')
            ax1.set_xlabel('$y$ (m)')
            ax1.set_ylabel('$I/I_0$')

            if enveloppe == True:
                ax1.plot(t, Diff(t) * Inter(0.00000001), 'k--')

        # Define colour of the curve according to wavelength
            if (l <= 500):
                couleur = 'b'
            elif (l <= 600):
                couleur = 'g'
            elif (l <= 700):
                couleur = 'r'

            ax1.plot(t, Diff(t)*Inter(t), couleur)

        else:
            largeur = 0.1#/(N-1)

            cdictr = {'red':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0))}

            cdictb= {'red':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0))}

            cdictg= {'red':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0))}

            red1 = LinearSegmentedColormap('red1', cdictr)
            blue1 = LinearSegmentedColormap('blue1', cdictb)
            green1 = LinearSegmentedColormap('green1', cdictg)

            ax1.set_yticks([])

            grillex = np.linspace(-0.03,0.03,1000)
            grilley = np.linspace(-0.03,0.03,200)

            alpha = 3000000

            ax1.set_xlabel('$y$ (m)')

            # Define colour of the curve according to wavelength
            if (l <= 500):
                couleur = blue1
            elif (l <= 600):
                couleur = green1
            elif (l <= 700):
                couleur = red1

            X,Y = np.meshgrid(grillex,grilley)
            Z = np.sin(np.pi*a*np.sin(np.arctan(X))*1000000/l)**2/((np.pi*a*np.sin(np.arctan(X))*1000000/l)**2)*np.sin(N*np.pi*d*np.sin(np.arctan(X))*1000000/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(X))*1000000/l)**2)*np.exp(-alpha*Y**2)

            ax1.pcolormesh(X,Y,Z, cmap=couleur)

        self.canvas.draw()
#        figure.savefig(nom)
