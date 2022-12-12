import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sq

class Ui_MainWindow(object): # типо твое основное окно
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(219, 62)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кто нажал тот гей"))


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        
        
        QtWidgets.QDialog.resize(self, 1200, 800) #Размер основного окна
        
        #Окно вывода результатов
        self.Export = QtWidgets.QTextEdit(self)
        self.Export.setGeometry(QtCore.QRect(0, 50, 1200, 700))
        self.Export.setObjectName("Export")
        self.setWindowTitle("Объявление")
        
        #Надпись сверху
        self.text = QtWidgets.QLabel(self)
        self.text.setGeometry(10, 10, 200, 20)
        self.text.setObjectName("text")
        self.text.setText("Информация об объявлении:")
        self.text.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.text.adjustSize()
        
        a=""
        rowids = ['55'] #Вывод по ровиду
                
        with sq.connect("newdb.db") as con:
            cur = con.cursor()

            for i in rowids:
                
                #Новая Квартира
                cur.execute(f"SELECT new_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Новая квартира: " + '\n'.join(map(str, x)) + '\n'
                
                #О Квартира
                cur.execute(f"SELECT about_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "О квартире: " + '\n'.join(map(str, x)) + '\n'

                #Цена
                cur.execute(f"SELECT cost_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Цена: " + '\n'.join(map(str, x)) + " Рублей" + '\n'
                    
                #Цена за кв.м.
                cur.execute(f"SELECT cost2_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Цена за кв.метр: " + '\n'.join(map(str, x)) + " Рублей" + '\n'
                    
                #Метро
                cur.execute(f"SELECT metro_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Ближайщая станция метро: " + '\n'.join(map(str, x)) + '\n'
                    
                #Расстояние до цетра
                cur.execute(f"SELECT center_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "До цетра: " + '\n'.join(map(str, x)) + " км" + '\n'
                    
                #Адрес
                cur.execute(f"SELECT adress_apart FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Андрес:" + '\n'.join(map(str, x)) + '\n'
                    
                #Количество команат
                cur.execute(f"SELECT Number_of_rooms FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Количество комнат: " + ('\n'.join(map(str, x))).replace("None", "Нету информации") + '\n'
                    
                #Отдклка
                cur.execute(f"SELECT Renovation FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Ремонт: " + ('\n'.join(map(str, x))) + '\n'
                    
                #Кв.м. кваритры
                cur.execute(f"SELECT Apartment_area FROM apart WHERE ROWID == {i}")
                for x in cur:
                    a = a + "Квартира составляет: " + '\n'.join(map(str, x)) + " кв.м." + '\n'
                    
                #Жилая площадь
                cur.execute(f"SELECT Living_area FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Жилая площадь: " + ('\n'.join(map(str, x))) +" кв.м." + '\n'
                
                #Площадь кухни
                cur.execute(f"SELECT Kitchen_area FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Площадь кухни: " + ('\n'.join(map(str, x))) +" кв.м." + '\n'
                
                #Этаж
                cur.execute(f"SELECT Floor FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Этаж: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Ванная
                cur.execute(f"SELECT Bathroom FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Ванная: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Количество ванных комант
                cur.execute(f"SELECT Number_of_bathrooms FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Количество ванных комант: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Полудомойка
                cur.execute(f"SELECT Dishwasher FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Полудомойка: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                
                #Холодильник
                cur.execute(f"SELECT Fridge FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Холодильник: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Мебель
                cur.execute(f"SELECT Furniture FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Мебель: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Интернет
                cur.execute(f"SELECT Internet FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Интернет: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Стиральная машина
                cur.execute(f"SELECT Washing_machine FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Стиральная машина: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Телевиденье
                cur.execute(f"SELECT TV FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Телевиденье: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Лоджия
                cur.execute(f"SELECT Loggia FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Лоджия: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                
                #Вид из окна
                cur.execute(f"SELECT View_from_window FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Вид из окна: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Кондиционер
                cur.execute(f"SELECT Air_conditioner FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Кондиционер: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Серийный номер дома
                cur.execute(f"SELECT House_series_number FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Серийный номер дома: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Высота потолков
                cur.execute(f"SELECT Height_of_ceilings FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Высота потолков: " + ('\n'.join(map(str, x))) + " м" + '\n'
                        
                #Лифт
                cur.execute(f"SELECT Elevator FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Лифт: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Материал стен
                cur.execute(f"SELECT Wall_material FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Материал стен: " + ('\n'.join(map(str, x))) + '\n'
                
                #Обогрев
                cur.execute(f"SELECT Heating FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Обогрев: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Консьерж
                cur.execute(f"SELECT Concierge FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Консьерж: " + ('\n'.join(map(str, x))).replace("1", "Имеется") + '\n'
                        
                #Дата сдачи дома
                cur.execute(f"SELECT House_handover_date FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Дата сдачи дома: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Временной период
                cur.execute(f"SELECT Time_period FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Временной период: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Парковка
                cur.execute(f"SELECT Parking FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Парковка: " + ('\n'.join(map(str, x))) + '\n'
                        
                #Год строительства
                cur.execute(f"SELECT Year_of_construction FROM apart WHERE ROWID == {i}")
                for x in cur:
                    if str(x) == "(None,)":
                        break
                    else:
                        a = a + "Год строительства: " + ('\n'.join(map(str, x))) + '\n'
                        
        self.Export.setText(a)
        self.Export.setFont(QtGui.QFont("Times", 15))
        
    def btnClosed(self):
        self.close()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow() # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)     # Инициализация GUI

        self.ui.pushButton.clicked.connect(self.openDialog) # Открыть новую форму

    def openDialog(self):
#       pass
        dialog = ClssDialog(self)
        dialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())