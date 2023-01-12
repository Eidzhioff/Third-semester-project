from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3 as sq
import os



class Ad_Information_Window(object):
    def setupUi(self, MainWindow, rowid1):
        self.rowid=rowid1
        self.d = ["cost_apart", "cost2_apart", "metro_apart", "center_apart", "adress_apart", "date_of_publication", "Number_of_rooms", "Renovation", "Apartment_area", "Floor", "Bathroom", "Dishwasher", "Fridge", "Furniture", "Internet", "Kitchen_furniture", "TV", "Washing_machine", "Loggia", "Elevator", "Wall_material", "Concierge", "House_handover_date", "Parking", "Year_of_construction"]
        self.dictt="cost_apart, cost2_apart, metro_apart, center_apart, adress_apart, date_of_publication, Number_of_rooms, Renovation, Apartment_area, Floor, Bathroom, Dishwasher, Fridge, Furniture, Internet, Kitchen_furniture, TV, Washing_machine, Loggia, Elevator, Wall_material, Concierge, House_handover_date, Parking, Year_of_construction"
        self.a=""

        with sq.connect("newdb.db") as con:
            cur = con.cursor()
        
            cur.execute(f"SELECT new_apart FROM apart WHERE ROWID == {self.rowid}")
            for i in cur:
                self.new_apart_name=list(i)[0]
        
        

        with sq.connect("newdb.db") as con:
            cur = con.cursor()
        
            cur.execute(f"SELECT {self.dictt} FROM apart WHERE ROWID == {self.rowid}")
            for i in cur:
                for x in i:
                    self.a+= "|" + str(x)
                            
        self.b=self.a.split("|")[1::]
        for i in range (13, len(self.b)):
            self.b[i]=self.b[i].replace("1", "есть")
                
        self.dd = dict(zip(self.d,self.b))
                
        self.keyses=[]
        for key, val in self.dd.items():
            if val == "None":
                self.keyses.append(key)

        for i in self.keyses:
            if i in self.dd:
                del self.dd[i]
                
        self.new_dict=[]
        for key in self.dd.items():
            self.new_dict.append(key[0])

        self.igm=[]
        for i in range (2, 27):
            self.igm.append(f"params\{i}.png")
        #igm = ["2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png","17.png","18.png","19.png","20.png","21.png","22.png","23.png","24.png","25.png","26.png"]
        self.dict_image = dict(zip(self.d,self.igm))

        self.cut = round(len(self.new_dict)/2)
        self.cut_2 = len(self.new_dict) - round(len(self.new_dict)/2)
        self.first_cut = self.new_dict[self.cut_2:]
        self.second_cut = self.new_dict[:self.cut]

        self.dict_podpisi={
        "cost_apart":"<b> Цена квартиры (₽): </b> <br>",
        "cost2_apart":"<b> Цена квартиры (₽, m²) :</b> <br>",
        "metro_apart":"<b> Ближайшее метро: </b> <br>",
        "center_apart":"<b> Расстояние до центра: </b> <br>",
        "adress_apart":"<b> Адрес квартиры: </b> <br>",
        "date_of_publication":"<b> Дата публикации: </b> <br>",
        "Number_of_rooms":"<b> Количество комнат: </b> <br>",
        "Renovation":"<b> Отделка: </b> <br>",
        "Apartment_area":"<b> Площадь жилья: </b> <br>",
        "Floor":"<b> Этаж: </b> <br>",
        "Bathroom":"<b> Ванная: </b> <br>",
        "Dishwasher":"<b> Посудомойка: </b> <br>",
        "Fridge":"<b> Холодильник: </b> <br>",
        "Furniture":"<b> Мебель: </b> <br>",
        "Internet":"<b> Интернет: </b> <br>",
        "Kitchen_furniture":"<b> Мебель на кухне: </b> <br>",
        "TV":"<b> ТВ: </b> <br>",
        "Washing_machine":"<b> Посудомоечная машина: </b> <br>",
        "Loggia":"<b> Лоджия: </b> <br>",
        "Elevator":"<b> Лифт: </b> <br>",
        "Wall_material":"<b> Материал стен: </b> <br>",
        "Concierge":"<b> Консьерж: </b> <br>",
        "House_handover_date":"<b> Временная эпоха: </b> <br>",
        "Parking":"<b> Парковка: </b> <br>",
        "Year_of_construction":"<b> Год возведения: </b> <br>"
        }

        
        
        
        
        ######
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(870, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -4, 847, 840))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 580))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # <- кнопка
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 540))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.img_pre)
        
        #Отображение
        self.num_img = 0
        
        self.len_foder_img = len(os.listdir(path=f"images\\{self.rowid}"))
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QtCore.QSize(720, 540))
        self.pushButton_3.setMaximumSize(QtCore.QSize(720, 540))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.setIcon(QIcon(f"images\\{self.rowid}\\{self.num_img}.jpg"))
        self.pushButton_3.setIconSize(QSize(720, 540))
        
        
        
        
        # -> кнопка
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 540))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.pushButton_5.clicked.connect(self.img_next)
        
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        
        self.groupBox_2.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.names_1 = []
        self.names_layout_1 = []
        self.names_text_1 = []
        self.text_1 = []
        self.pushButtons_1 = []

        for i in self.second_cut:
            self.names_1.append(i)
            self.names_layout_1.append(i)
            self.names_text_1.append(i)
            self.text_1.append(i)
            self.pushButtons_1.append(i)
        
        for i,v in enumerate(self.names_1):         
            self.names_1[i] = QtWidgets.QGroupBox(self.groupBox_3)
            self.names_1[i].setMinimumSize(QtCore.QSize(0, 100))
            self.names_1[i].setMaximumSize(QtCore.QSize(16777215, 100))
            self.names_1[i].setFlat(True)
            self.names_layout_1[i] = QtWidgets.QHBoxLayout(self.names_1[i])
        
            self.pushButtons_1[i] = QtWidgets.QPushButton(self.names_1[i])
            self.pushButtons_1[i].setEnabled(False)
            self.pushButtons_1[i].setMinimumSize(QtCore.QSize(60, 60))
            self.pushButtons_1[i].setMaximumSize(QtCore.QSize(60, 60))
            self.pushButtons_1[i].setText("")
            self.pushButtons_1[i].setIcon(QIcon(self.dict_image[self.second_cut[i]]))
            self.pushButtons_1[i].setIconSize(QSize(60, 60))
            self.names_layout_1[i].addWidget(self.pushButtons_1[i])
        
            self.text_1[i] = QtWidgets.QTextEdit(self.names_1[i])
            self.text_1[i].setMinimumSize(QtCore.QSize(0, 60))
            self.text_1[i].setMaximumSize(QtCore.QSize(16777215, 60))
            self.text_1[i].setText(self.dict_podpisi[self.second_cut[i]]+self.dd[self.second_cut[i]])
            self.text_1[i].setFont(QtGui.QFont("Times", 9))
            self.text_1[i].setReadOnly(True)
            self.names_layout_1[i].addWidget(self.text_1[i])
            self.verticalLayout_2.addWidget(self.names_1[i])
            self.horizontalLayout_2.addWidget(self.groupBox_3)
                
                
        self.names = []
        self.names_layout = []
        self.names_text = []
        self.text = []
        self.pushButtons = []
        
        
        for i in self.first_cut:
            self.names.append(i)
            self.names_layout.append(i)
            self.names_text.append(i)
            self.text.append(i)
            self.pushButtons.append(i)
            
        
        for i,v in enumerate(self.names):         
            self.names[i] = QtWidgets.QGroupBox(self.groupBox_2)
            self.names[i].setMinimumSize(QtCore.QSize(0, 100))
            self.names[i].setMaximumSize(QtCore.QSize(16777215, 100))
            self.names[i].setFlat(True)
            self.names_layout[i] = QtWidgets.QHBoxLayout(self.names[i])
        
            self.pushButtons[i] = QtWidgets.QPushButton(self.names[i])
            self.pushButtons[i].setEnabled(False)
            self.pushButtons[i].setMinimumSize(QtCore.QSize(60, 60))
            self.pushButtons[i].setMaximumSize(QtCore.QSize(60, 60))
            self.pushButtons[i].setText("")
            self.pushButtons[i].setIcon(QIcon(self.dict_image[self.first_cut[i]]))
            self.pushButtons[i].setIconSize(QSize(60, 60))
            self.names_layout[i].addWidget(self.pushButtons[i])
        
            self.text[i] = QtWidgets.QTextEdit(self.names[i])
            self.text[i].setMinimumSize(QtCore.QSize(0, 60))
            self.text[i].setMaximumSize(QtCore.QSize(16777215, 60))
            self.text[i].setText(self.dict_podpisi[self.first_cut[i]]+self.dd[self.first_cut[i]])
            self.text[i].setFont(QtGui.QFont("Times", 9))
            self.text[i].setReadOnly(True)
            self.names_layout[i].addWidget(self.text[i])
            self.verticalLayout.addWidget(self.names[i])
            self.horizontalLayout_2.addWidget(self.groupBox_2)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def img_next(self):
        self.num_img = (self.num_img + 1) % (self.len_foder_img)
        self.pushButton_3.setIcon(QIcon(f"images\\{self.rowid}\\{self.num_img}.jpg"))
        self.pushButton_3.setIconSize(QSize(720, 540))
        
    def img_pre(self):
        self.num_img = (self.num_img - 1) % (self.len_foder_img)
        self.pushButton_3.setIcon(QIcon(f"images\\{self.rowid}\\{self.num_img}.jpg"))
        self.pushButton_3.setIconSize(QSize(720, 540))
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.new_apart_name))
        self.pushButton_2.setText(_translate("MainWindow", "<<"))
        self.pushButton_5.setText(_translate("MainWindow", ">>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ad_Information_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
