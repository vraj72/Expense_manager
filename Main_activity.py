from exp import Ui_MainWindow
from get_data import get_data


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import pyqtSlot
import sys



id=2017135040   
t=get_data(id)
name=t.get_name( )
print(name)




if(name!=-1):
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow(id)
	ui.setupUi(MainWindow)
	ui.name_label.setText(name)
	MainWindow.show()
	sys.exit(app.exec_())
	


