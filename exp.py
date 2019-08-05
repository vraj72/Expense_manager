# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expense_manager.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from create_graph import create_graph
#from insert_data import insert_data
from get_data import get_data

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=7, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Ui_MainWindow(object):
    def __init__(self,id):
        self.id=id
        print('in exp.py init',id)

    def messegeBox(self,title,msg):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(msg)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def i_data(self):
        idn=self.id
        type=self.Filter_i_enter.currentText()
        amount=self.i_amount.toPlainText()
        date=self.calendarWidget_i.selectedDate().toString("yyyy-MM-dd")
        desc=self.desc_i.toPlainText()
        if(desc==""):
            desc=" "
        title="failed"
        msg=" "
        if (str(amount)=="" or not(amount.isnumeric())):
            msg="Enter amount"
        else :
            i=get_data
            i.insert_i(idn,type,amount,date,desc)
            title="Inserted"
            msg="type:- "+str(type)+"\namount:- "+str(amount)+"\ndate:- "+str(date)+"\nDescription:- "+str(desc)
            self.i_amount.setText("")
            self.desc_i.setText("")

        print(idn,type,amount,date,desc)
        print(title)
        print(msg)

        self.messegeBox(title,msg)
        a=create_graph
        print("refresh called")
        a.gi1(self.gi_total_pie,self.id)

    def e_data(self):
        idn=self.id
        type=self.Filter_type_eneter_e.currentText()
        amount=self.amount_e.toPlainText()
        date=self.calendarWidget_e.selectedDate().toString("yyyy-MM-dd")
        desc=self.desc_e.toPlainText()
        if(desc==""):
            desc=" "
        title="failed"
        msg=" "
        if (str(amount)=="" or not(amount.isnumeric())):
            msg="Enter amount"
            print(idn,type,amount,date,desc)
            print(title)
            print(msg)
            self.messegeBox(title,msg)
        else:
            print("entered condition")
            i=get_data
            c=i.insert_e(idn,type,amount,date,desc)
            title="Inserted"
            print(title)
            print(c)
            if(c==1):
                msg="type:- "+str(type)+"\namount:- "+str(amount)+"\ndate:- "+str(date)+"\nDescription:- "+str(desc)
                self.amount_e.setText("")
                self.desc_e.setText("")
                a=create_graph
                print("refresh called")
                a.ge1(self.ge_total_pie,self.id,1)
                print("refreshed")
                print(idn,type,amount,date,desc)
                print(title)
                print(msg)
                self.messegeBox(title,msg)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 730)
        MainWindow.setStyleSheet("background-color: rgb(136, 96, 208);\n"
"selection-background-color: rgb(173, 127, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 1161, 671))
        self.tabWidget.setStyleSheet("background-color: rgb(132, 206, 235);\n"
"selection-background-color: rgb(86, 128, 233);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        print('in exp.py',self.id)
        a=create_graph

        go_total_timewise = PlotCanvas(self.tab_1, width=4, height=2.6)
        go_total_timewise.move(10,10)
        a.go2(go_total_timewise)
        
        

        go_total_pie = PlotCanvas(self.tab_1, width=3.7, height=2.6)
        go_total_pie.move(430,10)
        a.go1(go_total_pie,self.id)

        gon = PlotCanvas(self.tab_1, width=3.1, height=2.6)
        gon.move(820,10)
        a.go4(gon,self.id)


        go_filter =PlotCanvas(self.tab_1, width=6, height=2.75)
        go_filter.move(10,350)
        a.go3(go_filter)

        self.Filter_o = QtWidgets.QComboBox(self.tab_1)
        self.Filter_o.setGeometry(QtCore.QRect(450, 310, 151, 31))
        self.Filter_o.setStyleSheet("background-color: rgb(136, 96, 208);")
        self.Filter_o.setObjectName("Filter_o")
        self.Filter_o.addItem("")
        self.Filter_o.addItem("")
        self.Filter_o.addItem("")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(400, 310, 41, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(710, 280, 111, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_1, "")

        self.RecentActivity_listview = QtWidgets.QListWidget(self.tab_1)
        self.RecentActivity_listview.setGeometry(QtCore.QRect(670, 320, 441, 301))
        self.RecentActivity_listview.setStyleSheet("\n"
"background-color: rgb(211, 215, 207);")
        self.RecentActivity_listview.setObjectName("RecentActivity_listview")


        
        asd=a.recent("2017135040")
        print("REcenT:-",asd)
        self.RecentActivity_listview.addItem("ItemNo     ID                 Type        Amount          Date             Description")
        for i in range(0,len(asd)):
            item = ("Item %i   " % i+str(asd[i][0])+"  "+str(asd[i][1])+"  "+str(asd[i][2])+"  "+str(asd[i][3])+"        "+str(asd[i][4]))
            self.RecentActivity_listview.addItem(item)

        self.tab_2_income = QtWidgets.QWidget()
        self.tab_2_income.setObjectName("tab_2_income")

        self.gi_total_pie = PlotCanvas(self.tab_2_income, width=4, height=2.6)
        self.gi_total_pie.move(10,50)
        a.gi1(self.gi_total_pie,self.id)
        #a=create_graph
        #a.go1(go_total_timewise)

        gi_total_timewise = PlotCanvas(self.tab_2_income, width=3.7, height=2.6)
        gi_total_timewise.move(430,50)
        a.gi2(gi_total_timewise)

        gin = PlotCanvas(self.tab_2_income, width=3.1, height=2.6)
        gin.move(820,50)

        self.label_5 = QtWidgets.QLabel(self.tab_2_income)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 181, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2_income)
        self.label_6.setGeometry(QtCore.QRect(420, 10, 191, 17))
        self.label_6.setObjectName("label_6")
        self.Filter_i = QtWidgets.QComboBox(self.tab_2_income)
        self.Filter_i.setGeometry(QtCore.QRect(600, 10, 181, 21))
        self.Filter_i.setStyleSheet("background-color: rgb(136, 96, 208);")
        self.Filter_i.setObjectName("Filter_i")
        self.Filter_i.addItem("")
        self.Filter_i.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab_2_income)
        self.label_7.setGeometry(QtCore.QRect(40, 340, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2_income)
        self.label_8.setGeometry(QtCore.QRect(20, 390, 101, 17))
        self.label_8.setObjectName("label_8")
        self.Filter_i_enter = QtWidgets.QComboBox(self.tab_2_income)
        self.Filter_i_enter.setGeometry(QtCore.QRect(129, 390, 181, 21))
        self.Filter_i_enter.setStyleSheet("background-color: rgb(136, 96, 208);")
        self.Filter_i_enter.setObjectName("Filter_i_enter")
        self.Filter_i_enter.addItem("")
        self.Filter_i_enter.addItem("")


        
        
        self.label_10 = QtWidgets.QLabel(self.tab_2_income)
        self.label_10.setGeometry(QtCore.QRect(10, 500, 111, 20))
        self.label_10.setObjectName("label_10")
        self.i_amount = QtWidgets.QTextEdit(self.tab_2_income)
        self.i_amount.setGeometry(QtCore.QRect(120, 490, 241, 51))
        self.i_amount.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.i_amount.setObjectName("i_amount")

        self.enter_i = QtWidgets.QPushButton(self.tab_2_income)
        self.enter_i.setGeometry(QtCore.QRect(960, 580, 131, 41))
        self.enter_i.setObjectName("enter_i")
        self.enter_i.clicked.connect(self.i_data)

        self.calendarWidget_i = QtWidgets.QCalendarWidget(self.tab_2_income)
        self.calendarWidget_i.setGeometry(QtCore.QRect(400, 370, 456, 171))
        self.calendarWidget_i.setStyleSheet("border-color: rgb(136, 138, 133);\n"

"background-color: rgb(233, 128, 116);")
        self.calendarWidget_i.setObjectName("calendarWidget_i")
        self.desc_i = QtWidgets.QTextEdit(self.tab_2_income)
        self.desc_i.setGeometry(QtCore.QRect(920, 400, 191, 131))
        self.desc_i.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.desc_i.setObjectName("desc_i")
        self.label_17 = QtWidgets.QLabel(self.tab_2_income)
        self.label_17.setGeometry(QtCore.QRect(920, 370, 101, 17))
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_2_income, "")
        self.tab_3_expense = QtWidgets.QWidget()
        self.tab_3_expense.setObjectName("tab_3_expense")

        self.ge_total_pie = PlotCanvas(self.tab_3_expense, width=4, height=2.6)
        self.ge_total_pie.move(10,50)
        a.ge1(self.ge_total_pie,self.id,0)
        #a=create_graph
        #a.go1(go_total_timewise)

        ge_total_timewise = PlotCanvas(self.tab_3_expense, width=3.7, height=2.6)
        ge_total_timewise.move(430,50)
        a.ge2(ge_total_timewise)
        

        gen = PlotCanvas(self.tab_3_expense, width=3.1, height=2.6)
        gen.move(820,50)

        self.label_11 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 151, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_12.setGeometry(QtCore.QRect(410, 20, 191, 17))
        self.label_12.setObjectName("label_12")
        self.Filter_e_type = QtWidgets.QComboBox(self.tab_3_expense)
        self.Filter_e_type.setGeometry(QtCore.QRect(600, 20, 181, 21))
        self.Filter_e_type.setStyleSheet("background-color: rgb(136, 96, 208);")
        self.Filter_e_type.setObjectName("Filter_e_type")
        self.Filter_e_type.addItem("")
        self.Filter_e_type.addItem("")
        self.Filter_e_type.addItem("")
        self.Filter_e_type.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_13.setGeometry(QtCore.QRect(30, 360, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_14.setGeometry(QtCore.QRect(10, 410, 101, 17))
        self.label_14.setObjectName("label_14")
        self.Filter_type_eneter_e = QtWidgets.QComboBox(self.tab_3_expense)
        self.Filter_type_eneter_e.setGeometry(QtCore.QRect(110, 410, 181, 21))
        self.Filter_type_eneter_e.setStyleSheet("background-color: rgb(136, 96, 208);")
        self.Filter_type_eneter_e.setObjectName("Filter_type_eneter_e")
        self.Filter_type_eneter_e.addItem("")
        self.Filter_type_eneter_e.addItem("")
        self.Filter_type_eneter_e.addItem("")
        self.Filter_type_eneter_e.addItem("")
        
        
        self.label_16 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_16.setGeometry(QtCore.QRect(10, 520, 111, 20))
        self.label_16.setObjectName("label_16")
        self.amount_e = QtWidgets.QTextEdit(self.tab_3_expense)
        self.amount_e.setGeometry(QtCore.QRect(120, 510, 241, 51))
        self.amount_e.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.amount_e.setObjectName("amount_e")
        self.enetr_e = QtWidgets.QPushButton(self.tab_3_expense)
        self.enetr_e.setGeometry(QtCore.QRect(940, 580, 131, 41))
        self.enetr_e.setObjectName("enetr_e")
        self.enetr_e.clicked.connect(self.e_data)

        self.calendarWidget_e = QtWidgets.QCalendarWidget(self.tab_3_expense)
        self.calendarWidget_e.setGeometry(QtCore.QRect(390, 390, 456, 171))
        self.calendarWidget_e.setStyleSheet("border-color: rgb(136, 138, 133);\n"
"background-color: rgb(233, 128, 116);")
        self.calendarWidget_e.setObjectName("calendarWidget_e")
        self.label_18 = QtWidgets.QLabel(self.tab_3_expense)
        self.label_18.setGeometry(QtCore.QRect(890, 390, 101, 17))
        self.label_18.setObjectName("label_18")
        self.desc_e = QtWidgets.QTextEdit(self.tab_3_expense)
        self.desc_e.setGeometry(QtCore.QRect(890, 420, 191, 131))
        self.desc_e.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.desc_e.setObjectName("desc_e")
        self.tabWidget.addTab(self.tab_3_expense, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(70, 10, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.Filter_o)
        MainWindow.setTabOrder(self.Filter_o, self.RecentActivity_listview)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>OverView</p></body></html>"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>OverView</p></body></html>"))
        self.Filter_o.setItemText(0, _translate("MainWindow", "Daily"))
        self.Filter_o.setItemText(1, _translate("MainWindow", "Monthly"))
        self.Filter_o.setItemText(2, _translate("MainWindow", "Yearly"))
        self.label.setText(_translate("MainWindow", "Filter:"))
        self.label_2.setText(_translate("MainWindow", "Recent Activity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "OverView"))
        self.label_5.setText(_translate("MainWindow", "timewise income graph"))
        self.label_6.setText(_translate("MainWindow", "category wise time  graph"))
        self.Filter_i.setItemText(0, _translate("MainWindow", "Business"))
        self.Filter_i.setItemText(1, _translate("MainWindow", "job"))
        self.label_7.setText(_translate("MainWindow", "Enter New Income"))
        self.label_8.setText(_translate("MainWindow", "Income Type:"))
        self.Filter_i_enter.setItemText(0, _translate("MainWindow", "Business"))
        self.Filter_i_enter.setItemText(1, _translate("MainWindow", "Job"))
        
        self.label_10.setText(_translate("MainWindow", "Enter Amount:"))
        self.enter_i.setText(_translate("MainWindow", "Enter"))
        self.label_17.setText(_translate("MainWindow", "Description:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2_income), _translate("MainWindow", "Income"))
        self.label_11.setText(_translate("MainWindow", "all expense graph"))
        self.label_12.setText(_translate("MainWindow", "category wise time  graph"))
        self.Filter_e_type.setItemText(0, _translate("MainWindow", "food"))
        self.Filter_e_type.setItemText(1, _translate("MainWindow", "Travel"))
        self.Filter_e_type.setItemText(2, _translate("MainWindow", "education"))
        self.Filter_e_type.setItemText(3, _translate("MainWindow", "Investment"))
        self.label_13.setText(_translate("MainWindow", "Enter New Expense "))
        self.label_14.setText(_translate("MainWindow", "Income Type:"))
        self.Filter_type_eneter_e.setItemText(0, _translate("MainWindow", "food"))
        self.Filter_type_eneter_e.setItemText(1, _translate("MainWindow", "Travel"))
        self.Filter_type_eneter_e.setItemText(2, _translate("MainWindow", "education"))
        self.Filter_type_eneter_e.setItemText(3, _translate("MainWindow", "Investment"))
        
        self.label_16.setText(_translate("MainWindow", "Enter Amount:"))
        self.enetr_e.setText(_translate("MainWindow", "Enter"))
        self.label_18.setText(_translate("MainWindow", "Description:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3_expense), _translate("MainWindow", "Expense"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.name_label.setText(_translate("MainWindow", "Name will be Displayed HERE"))

