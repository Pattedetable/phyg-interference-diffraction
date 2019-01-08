#
# Copyright 2018-2019 Manuel Barrette
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

""" Initialize windows and make the main window appear """
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import interference_main_window
import dialog_interference
import locale

# Initialize windows
app = QApplication(sys.argv)
window_Interference = QMainWindow()
dialog = QDialog()

langue_sys = locale.getdefaultlocale()[0]
langue_sys = langue_sys[0:2]
translator = QtCore.QTranslator()
if langue_sys == "fr":
    langue = "fr_CA"
else:
    langue = "en_CA"
translator.load(langue)
app.installTranslator(translator)

ui_Interference = interference_main_window.Ui_MainWindow()
ui_Dial = dialog_interference.Ui_Dialog()

ui_Dial.setupUi(dialog)
ui_Interference.setupUi(window_Interference, dialog, None)

# Make main window appear
window_Interference.show()
sys.exit(app.exec_())
