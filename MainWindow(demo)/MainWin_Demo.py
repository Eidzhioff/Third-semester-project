# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sq

a=[]
aa=""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 756)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Прокручиваемое поле
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 261, 701))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 699))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        #Кнопка активарции параметра
        self.checkBox_Fridge = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Fridge.setGeometry(QtCore.QRect(0, 0, 261, 31))
        self.checkBox_Fridge.setObjectName("checkBox_Fridge")
        self.checkBox_Fridge.toggled.connect(self.is_checked)
        
        #Задаем цену от
        self.input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input.setGeometry(QtCore.QRect(10, 120, 151, 21))
        self.input.setText("")
        self.input.setObjectName("input")
        
        #Задаем цены до
        self.output = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.output.setGeometry(QtCore.QRect(10, 160, 151, 21))
        self.output.setText("")
        self.output.setObjectName("output")
        
        #Подпись input
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 100, 151, 21))
        self.label.setObjectName("label")
        
        #Подпись output
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 21))
        self.label_2.setObjectName("label_2")
        
        #Кнопка активарции параметра
        self.checkBox_Furniture = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Furniture.setGeometry(QtCore.QRect(0, 30, 261, 31))
        self.checkBox_Furniture.setObjectName("checkBox_Furniture")
        self.checkBox_Furniture.toggled.connect(self.is_checked)
        
        #Кнопка активарции параметра
        self.checkBox_Internet = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Internet.setGeometry(QtCore.QRect(0, 60, 261, 31))
        self.checkBox_Internet.setObjectName("checkBox_Internet")
        self.checkBox_Internet.toggled.connect(self.is_checked)
        
        #Кнопка вывода результатов
        self.Enter = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Enter.setGeometry(QtCore.QRect(0, 642, 261, 61))
        self.Enter.setObjectName("Enter")
        self.Enter.clicked.connect(self.export_res)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        #Вывод результатов
        self.Export = QtWidgets.QTextEdit(self.centralwidget)
        self.Export.setGeometry(QtCore.QRect(320, 40, 901, 701))
        self.Export.setObjectName("Export")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Проверка на активацию кнопки
    def is_checked(self):
        print("DA")
    
    #Функция вывода результатов
    def export_res(self):
        global a,aa
        
        inp = self.input.text() #Смотри какую цену ввел поьзователь от
        out = self.output.text() #Смотри какую цену ввел поьзователь до
        price = f"({inp} < cost_apart AND cost_apart < {out})" # Формируем строку, которую "создал" пользователь
        
        res=""
        
        #Формирование части строки sql в зависимоти от активированных параметров
        if self.checkBox_Fridge.isChecked():
            a.append("Fridge == 1")
        if self.checkBox_Furniture.isChecked():
            a.append("Furniture == 1")
        if self.checkBox_Internet.isChecked():
            a.append("Internet == 1")
   
        aa =' AND '.join(a)
        
        #Подключение к Бд
        with sq.connect("newdb.db") as con:
            cur = con.cursor()
            
            l = "SELECT new_apart, cost_apart FROM apart WHERE " + aa + " AND" + price #sql запрос
            cur.execute(f"{l}")
            
        #    cur.execute("SELECT rowid, new_apart, cost_apart FROM apart")
            for i in cur:
                res = res + "\n" + "__________________" + "\n" + ('\n'.join(map(str, i)))
                
        self.Export.setText(res) # вывод данных    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_Fridge.setText(_translate("MainWindow", "Холодильник"))
        self.checkBox_Furniture.setText(_translate("MainWindow", "Мебель"))
        self.checkBox_Internet.setText(_translate("MainWindow", "Интеренет "))
        self.Enter.setText(_translate("MainWindow", "Поиск"))
        self.label.setText(_translate("MainWindow", "Цена от:"))
        self.label_2.setText(_translate("MainWindow", "Цена до:"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
