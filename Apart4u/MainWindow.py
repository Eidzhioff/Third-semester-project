from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import sqlite3 as sq
from random import randint
import sys
from Ad_Info_Win import Ad_Information_Window 



class GroupBox(QtWidgets.QGroupBox):                      
    clicked = QtCore.pyqtSignal(str, object)               

    def __init__(self, title):              
        super(GroupBox, self).__init__()
        self.title = title
        self.setTitle(self.title)

    def mousePressEvent(self, event):
        self.clicked.emit(self.title, self)


       
class Ui_MainWindow(QtWidgets.QMainWindow):

    def openInfoWin(self, rowid):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ad_Information_Window()
        self.ui.setupUi(self.window, rowid)
        self.window.show()



    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_Main = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_Main.setObjectName("gridLayout_Main")
        
        self.gridLayout_Main_2 = QtWidgets.QGridLayout()
        self.gridLayout_Main_2.setObjectName("gridLayout_Main_2")

        ##Надпись Поиск квартир
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_Main_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_Main.addLayout(self.gridLayout_Main_2, 0, 0, 1, 1)

                                                    
        
        self.gridLayout_Left_Column = QtWidgets.QGridLayout()
        self.gridLayout_Left_Column.setObjectName("gridLayout_Left_Column")
        

        ##Создание ScrollArea для всех параметров
        self.scrollArea_Param = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_Param.setMinimumSize(QtCore.QSize(220, 10))
        self.scrollArea_Param.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scrollArea_Param.setWidgetResizable(True)
        self.scrollArea_Param.setObjectName("scrollArea_Param")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -155, 197, 648))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.gridLayout_Params = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_Params.setObjectName("gridLayout_Params")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents) ## label_2="Выбор паметров"
        self.label_2.setObjectName("label_2")
        self.gridLayout_Params.addWidget(self.label_2, 0, 0, 1, 1)

        ##Количество комнат
        self.groupBox_Rooms = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Rooms.setFont(font)
        self.groupBox_Rooms.setObjectName("groupBox_Rooms")
        self.gridLayout_Rooms = QtWidgets.QGridLayout(self.groupBox_Rooms)
        self.gridLayout_Rooms.setObjectName("gridLayout_Rooms")

        self.namesCheckBox_Rooms=[]
        for _ in range(4):
            self.namesCheckBox_Rooms.append(f"checkBox_Rooms_{_}")

        for i, v in enumerate(self.namesCheckBox_Rooms):
            self.namesCheckBox_Rooms[i] = QtWidgets.QCheckBox(self.groupBox_Rooms)
            self.namesCheckBox_Rooms[i].setObjectName(v)
            self.gridLayout_Rooms.addWidget(self.namesCheckBox_Rooms[i], i, 0, 1, 1)
            
        

        self.gridLayout_Params.addWidget(self.groupBox_Rooms, 1, 0, 1, 1)
        ##


        ##ПЛОЩАДЬ ОТ И ДО
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents) ##Площадь от 
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_Params.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_Area_from = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Area_from.setObjectName("lineEdit_Area_from")
        reg_ex_Area_from = QRegExp("[0-9]{1,15}")
        input_validator_Area_from = QRegExpValidator(reg_ex_Area_from, self.lineEdit_Area_from)
        self.lineEdit_Area_from.setValidator(input_validator_Area_from)
        self.gridLayout_Params.addWidget(self.lineEdit_Area_from, 3, 0, 1, 1)

        self.horizontalSlider_Area_from = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_Area_from.setMinimum(5)
        self.horizontalSlider_Area_from.setMaximum(100)
        self.horizontalSlider_Area_from.valueChanged.connect(self.changed_Area_from)
        self.horizontalSlider_Area_from.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Area_from.setObjectName("horizontalSlider_Area_from")
        self.gridLayout_Params.addWidget(self.horizontalSlider_Area_from, 4, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents) ##Плоащь до
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_Params.addWidget(self.label_7, 5, 0, 1, 1)

        
        self.lineEdit_Area_to = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Area_to.setObjectName("lineEdit_Area_to")
        reg_ex_Area_to = QRegExp("[0-9]{1,15}")
        input_validator_Area_to = QRegExpValidator(reg_ex_Area_to, self.lineEdit_Area_to)
        self.lineEdit_Area_to.setValidator(input_validator_Area_to)
        self.gridLayout_Params.addWidget(self.lineEdit_Area_to, 6, 0, 1, 1)
        
        self.horizontalSlider_Area_to = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_Area_to.setMinimum(5)
        self.horizontalSlider_Area_to.setMaximum(100)
        self.horizontalSlider_Area_to.valueChanged.connect(self.changed_Area_to)
        self.horizontalSlider_Area_to.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Area_to.setObjectName("horizontalSlider_Area_to")
        self.gridLayout_Params.addWidget(self.horizontalSlider_Area_to, 7, 0, 1, 1)
        ##

        ##Horizontal line
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_Params.addWidget(self.line, 8, 0, 1, 1)
        ##
        
        ##ЦЕНА ОТ И ДО
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents) #label_4="Цена от"
        self.label_4.setObjectName("label_4")
        self.gridLayout_Params.addWidget(self.label_4, 9, 0, 1, 1)

        self.lineEdit_Price_from = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        ##self.lineEdit_Price_from.setInputMask("")  ##???
        reg_ex_Price_from = QRegExp("[0-9]{1,15}")
        input_validator_Price_from = QRegExpValidator(reg_ex_Price_from, self.lineEdit_Price_from)
        self.lineEdit_Price_from.setValidator(input_validator_Price_from)
        self.lineEdit_Price_from.setObjectName("lineEdit_Price_from")
        self.gridLayout_Params.addWidget(self.lineEdit_Price_from, 10, 0, 1, 1)

        self.horizontalSlider_Price_from = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_Price_from.setEnabled(True)
        self.horizontalSlider_Price_from.setMinimum(1000)
        self.horizontalSlider_Price_from.setMaximum(100000000)
##        self.horizontalSlider_Price_from.setSingleStep(1000)
        self.horizontalSlider_Price_from.valueChanged.connect(self.changed_Price_from)
        self.horizontalSlider_Price_from.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Price_from.setObjectName("horizontalSlider_Price_from")
        self.gridLayout_Params.addWidget(self.horizontalSlider_Price_from, 11, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents) #label_5="Цена до"
        self.label_5.setObjectName("label_5")
        self.gridLayout_Params.addWidget(self.label_5, 12, 0, 1, 1)

        self.lineEdit_Price_to = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Price_to.setObjectName("lineEdit_Price_to")
        reg_ex_Price_to = QRegExp("[0-9]{1,15}")
        input_validator_Price_to = QRegExpValidator(reg_ex_Price_to, self.lineEdit_Price_to)
        self.lineEdit_Price_to.setValidator(input_validator_Price_to)
        self.gridLayout_Params.addWidget(self.lineEdit_Price_to, 13, 0, 1, 1)

        self.horizontalSlider_Price_to = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_Price_to.setMinimum(1000)
        self.horizontalSlider_Price_to.setMaximum(100000000)
##        self.horizontalSlider_Price_to.setSingleStep(1000)
        self.horizontalSlider_Price_to.valueChanged.connect(self.changed_Price_to)
        self.horizontalSlider_Price_to.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Price_to.setObjectName("horizontalSlider_3")
        self.gridLayout_Params.addWidget(self.horizontalSlider_Price_to, 14, 0, 1, 1)
        ##

        ##Horizontal line
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_Params.addWidget(self.line_2, 15, 0, 1, 1)
        ##


        ##label_8="Дополнительные параметры"
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setMinimumSize(QtCore.QSize(133, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: bold 9pt \"Century Gothic\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_Params.addWidget(self.label_8, 16, 0, 1, 1)


        ##СОЗДАНИЕ CHECKBOX ДЛЯ ПАРАМЕТРОВ
        self.listCheckBox = ["Dishwasher", "Fridge", "Furniture", "Internet", "Kitchen_furniture", "TV", "Washing_machine", "Loggia", "Elevator", "Concierge" ]
        self.listCheckBoxName = ["Dishwasher", "Fridge", "Furniture", "Internet", "Kitchen_furniture", "TV", "Washing_machine", "Loggia", "Elevator", "Concierge" ]
        self.listCheckBoxTitle = ["Посудомойка", "Холодильник", "Мебель", "Интернет", "Мебель на кухне", "Телевидение", "Стиралка", "Балкон", "Лифт", "Консьерж" ]

        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.listCheckBox[i].setObjectName(v)
            self.gridLayout_Params.addWidget(self.listCheckBox[i], i+17, 0, 1, 1)
        ##



        ##Кнопка Enter
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setObjectName("Enter")
        self.Enter.clicked.connect(self.export_res)
        self.gridLayout_Left_Column.addWidget(self.Enter, 1, 0, 1, 1)

        
        self.scrollArea_Param.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_Left_Column.addWidget(self.scrollArea_Param, 0, 0, 1, 1)
        


        self.gridLayout_Main_2.addLayout(self.gridLayout_Left_Column, 1, 0, 1, 1)

        ##Надпись Результаты и выбор типа сортировки
        self.gridLayout_Right_Column = QtWidgets.QGridLayout()
        self.gridLayout_Right_Column.setObjectName("gridLayout_Right_Column")
        self.groupBox_TextRes = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_TextRes.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_TextRes.setObjectName("groupBox_TextRes")
        self.gridLayout_TextRes = QtWidgets.QGridLayout(self.groupBox_TextRes)
        self.gridLayout_TextRes.setObjectName("gridLayout_TextRes")
        self.label_3 = QtWidgets.QLabel(self.groupBox_TextRes)  ##label_3="Результаты"
        self.label_3.setMinimumSize(QtCore.QSize(330, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout_TextRes.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_TextRes)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 10))
        self.comboBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        for i in range(4):
            self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.changeComboBox)
        self.paramSort = "по ↑ цены"
        self.gridLayout_TextRes.addWidget(self.comboBox, 0, 1, 1, 1)
        self.gridLayout_Right_Column.addWidget(self.groupBox_TextRes, 0, 0, 1, 1)
        ##


        ##Панель вывода
        self.scrollArea_Results = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_Results.setMinimumSize(QtCore.QSize(530, 400))
        self.scrollArea_Results.setWidgetResizable(True)
        self.scrollArea_Results.setObjectName("scrollArea_Results")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 543, 475))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        
        self.gridLayout_Results = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_Results.setObjectName("gridLayout_Results")

        


        
        self.scrollArea_Results.setWidget(self.scrollAreaWidgetContents_2)

        
        self.gridLayout_Right_Column.addWidget(self.scrollArea_Results, 1, 0, 1, 1)

        
        self.gridLayout_Main_2.addLayout(self.gridLayout_Right_Column, 1, 1, 1, 1)

        

        MainWindow.setCentralWidget(self.centralwidget)

        self.namesBoxes=[]
        self.namesTexts=[]
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changed_Area_from(self):
        _translate = QtCore.QCoreApplication.translate
        new_value=str(self.horizontalSlider_Area_from.value())
        self.lineEdit_Area_from.setText(_translate("lineEdit_Area_from", new_value))

    def changed_Area_to(self):
        _translate = QtCore.QCoreApplication.translate
        new_value=str(self.horizontalSlider_Area_to.value())
        self.lineEdit_Area_to.setText(_translate("lineEdit_Area_to", new_value))

    def changed_Price_from(self):
        _translate = QtCore.QCoreApplication.translate
        new_value=str(self.horizontalSlider_Price_from.value())
        self.lineEdit_Price_from.setText(_translate("lineEdit_Price_from", new_value))

    def changed_Price_to(self):
        _translate = QtCore.QCoreApplication.translate
        new_value=str(self.horizontalSlider_Price_to.value())
        self.lineEdit_Price_to.setText(_translate("lineEdit_Price_to", new_value))

        
    def onFooGroupClick(self, title):                                  
        #print(f"Group: {title}; objectName=`{obj.objectName()}`")
        rowid=title.split("_")[1]
        print (rowid)
        self.openInfoWin(rowid)

        
        
    def changeComboBox(self, index):
        self.paramSort = self.comboBox.itemText(index)
        print (self.paramSort)
        self.export_res()

    def clear(self):
        objectList = self.scrollArea_Results.findChildren(GroupBox)
        for i in objectList:
            i.setParent(None)

    def export_res(self):
        _translate = QtCore.QCoreApplication.translate

        self.clear()
        
        objectList = self.scrollArea_Results.findChildren(GroupBox)

        eror=""
        price=""
        area=""
        
        price_from_text=self.lineEdit_Price_from.text()
        price_to_text=self.lineEdit_Price_to.text()
        if price_from_text != "" and price_to_text != "":
            if int(price_from_text) < int(price_to_text):
                price = f"({price_from_text} < cost_apart AND cost_apart < {price_to_text})"
            else:
                eror="Введите корректный диапазон цены"
        else:
            if (price_from_text != ""):
                price = f"({price_from_text} < cost_apart AND cost_apart < 100000000000)"
            elif (price_to_text != ""):
                price = f"(1 < cost_apart AND cost_apart < {price_to_text})"
            else:
                price = "(1 < cost_apart AND cost_apart < 100000000000)"

        area_from_text=self.lineEdit_Area_from.text()
        area_to_text=self.lineEdit_Area_to.text()
        if area_from_text != "" and area_to_text != "":
            if float(area_from_text) < float(area_to_text):
                area = f"({area_from_text} < Apartment_area AND Apartment_area < {area_to_text})"
            else:
                if eror != "":
                    eror="Введите корректный диапазон цены и площади квартиры"
                else:
                    eror="Введите корректный диапазон площади квартиры"
        else:
            if (area_from_text != ""):
                area = f"({area_from_text} < Apartment_area AND Apartment_area < 10000)"
            elif (area_to_text != ""):
                area=f"(1 < Apartment_area AND Apartment_area < {area_to_text})"
            else:
                area = "(1 < Apartment_area AND Apartment_area < 10000)"

        result=[]
        resultParam = []
        for i, v in enumerate(self.listCheckBox):
            if self.listCheckBox[i].isChecked():
                resultParam.append(self.listCheckBoxName[i] + " == 1")

                
        resultRooms = []       
        for i, v in enumerate(self.namesCheckBox_Rooms):
            if self.namesCheckBox_Rooms[i].isChecked():
                resultRooms.append("Number_of_rooms == " + str(i+1))


        resultParam=str((' AND '.join(resultParam)))  
        resultRooms=str(f"({(' OR '.join(resultRooms))})")

        result.append(resultParam)
        result.append(resultRooms)
        result.append(price)
        result.append(area)
        result=[value for value in result if (value != "" and value != "()")]
        result = str(' AND '.join(result))


        if eror!="":
            self.eror_Box=GroupBox("eror_Box")
            self.eror_Box.setMinimumSize(QtCore.QSize(200, 200))
            self.eror_Box.setObjectName("eror_Box")

            self.eror_Grid=QtWidgets.QGridLayout(self.eror_Box)
            self.eror_Grid.setObjectName("eror_Grid")

            self.eror_Text = QtWidgets.QTextEdit(self.eror_Box)
            self.eror_Text.setMinimumSize(QtCore.QSize(0, 100))
            self.eror_Text.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.eror_Text.setFrameShadow(QtWidgets.QFrame.Plain)
            self.eror_Text.setTabChangesFocus(False)
            self.eror_Text.setReadOnly(True)
            self.eror_Text.setObjectName("eror_Text")

            self.eror_Grid.addWidget(self.eror_Text, 0, 0, 1, 1)
            self.gridLayout_Results.addWidget(self.eror_Box, 0, 0, 1, 1)


            self.eror_Box.setTitle(_translate("MainWindow", "Ошибка"))
            self.eror_Box.setStyleSheet("font: bold 10pt \"Century Gothic\";")

            self.eror_Text.setHtml(_translate("MainWindow", eror))
            self.eror_Text.setStyleSheet("font: 75 9pt \"Century Gothic\";")

        else:
            self.res={}
            eror2=""

            #["по ↑ цены","по ↓ цены", "по ↑ времени добавления", "по ↓ времени добавления"]
            if "↑" in self.paramSort:
                if "цены" in self.paramSort:
                    orderStr= " ORDER BY cost_apart"
                else:
                    orderStr= " ORDER BY date"
            else:
                if "цены" in self.paramSort:
                    orderStr= " ORDER BY cost_apart DESC"
                else:
                    orderStr= " ORDER BY date DESC"

            try:
                with sq.connect("newdb.db") as con:
                    cur = con.cursor()
                
                    l = "SELECT rowid, new_apart, cost_apart, about_apart, date FROM apart WHERE " + result + orderStr
                    print (l)
                    cur.execute(f"{l}")

                    for i in cur:
                        price=str('{0:,}'.format(int(i[2])).replace(",", "."))+" ₽"
                        outputStr=[str(i[1]),f" <b>{price} </b>", str(i[3]), f"Дата добавления объявления: {str(i[-1])}"]
                        self.res[i[0]]=('\n'.join(outputStr))
                    if self.res=={}:
                        eror2="Нет объявлений, удовлетволяющих заданным параметрам"
            except:
                eror2="Не удается подключиться к базе данных"

            if eror2!="":
                self.eror_Box=GroupBox("eror_Box")
                self.eror_Box.setMinimumSize(QtCore.QSize(200, 200))
                self.eror_Box.setObjectName("eror_Box")

                self.eror_Grid=QtWidgets.QGridLayout(self.eror_Box)
                self.eror_Grid.setObjectName("eror_Grid")

                self.eror_Text = QtWidgets.QTextEdit(self.eror_Box)
                self.eror_Text.setMinimumSize(QtCore.QSize(0, 100))
                self.eror_Text.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.eror_Text.setFrameShadow(QtWidgets.QFrame.Plain)
                self.eror_Text.setTabChangesFocus(False)
                self.eror_Text.setReadOnly(True)
                self.eror_Text.setObjectName("eror_Text")

                self.eror_Grid.addWidget(self.eror_Text, 0, 0, 1, 1)
                self.gridLayout_Results.addWidget(self.eror_Box, 0, 0, 1, 1)


                self.eror_Box.setTitle(_translate("MainWindow", "Ошибка"))
                self.eror_Box.setStyleSheet("font: bold 10pt \"Century Gothic\";")

                self.eror_Text.setHtml(_translate("MainWindow", eror2))
                self.eror_Text.setStyleSheet("font: 75 9pt \"Century Gothic\";")

                self.namesBoxes=[]
                self.namesGrids=[]
                self.namesTexts=[]
            else:
                #Поиск по заданным параметрам возвращает список rowid
                #По данным rowid мы создаем список из названий GroupBox_{rowid} и записываем в namesBoxes
                #В дальнейшем будем переиминовывать GroupBox_{rowid} в короткое название объявления
                #Аналогичные действия мы делаем с namesTexts, то есть создаем список из TextEdit_{rowid}
                self.namesBoxes=[]
                self.namesGrids=[]
                self.namesTexts=[]

                for _ in self.res.keys():
                    self.namesBoxes.append(f'GroupBox_{_}')
                    self.namesGrids.append(f'GridLayout_{_}')
                    self.namesTexts.append(f'TextEdit_{_}')

                
                for i, v in enumerate(self.namesBoxes):
                    
                    self.namesBoxes[i]=GroupBox(self.namesBoxes[i])
                    self.namesBoxes[i].setEnabled(True)
                    self.namesBoxes[i].setMinimumSize(QtCore.QSize(200, 200))
                    self.namesBoxes[i].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    self.namesBoxes[i].setFlat(True)
                    self.namesBoxes[i].setCheckable(False)
                    self.namesBoxes[i].setChecked(False)
                    self.namesBoxes[i].setObjectName(v)
                    self.namesBoxes[i].clicked.connect(self.onFooGroupClick)

                    self.nameGrid=self.namesGrids[i]
                    self.namesGrids[i]=QtWidgets.QGridLayout(self.namesBoxes[i])
                    self.namesGrids[i].setObjectName(self.nameGrid)

                    self.nameText=self.namesTexts[i]
                    self.namesTexts[i] = QtWidgets.QTextEdit(self.namesBoxes[i])
                    self.namesTexts[i].setMinimumSize(QtCore.QSize(0, 100))
                    self.namesTexts[i].setEnabled(True)
                    self.namesTexts[i].setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.namesTexts[i].setFrameShadow(QtWidgets.QFrame.Plain)
                    self.namesTexts[i].setTabChangesFocus(False)
                    self.namesTexts[i].setReadOnly(True)
                    self.namesTexts[i].setObjectName(self.nameText)

                    self.namesGrids[i].addWidget(self.namesTexts[i], 0, 0, 1, 1)
                    self.gridLayout_Results.addWidget(self.namesBoxes[i], i, 0, 1, 1)
                    
            self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        ##label Поиск квартиры
        self.label.setText(_translate("MainWindow", "Поиск квартиры"))
        self.label.setStyleSheet("font: bold 18pt \"Century Gothic\";")
        ##Button поиск
        self.Enter.setText(_translate("MainWindow", "Поиск"))
        self.Enter.setStyleSheet("font: 75 10pt \"Century Gothic\";")
        ##label Результаты
        self.groupBox_TextRes.setTitle(_translate("MainWindow", "")) 
        self.label_3.setText(_translate("MainWindow", "Результаты:"))
        self.label_3.setStyleSheet("font: bold 10pt \"Century Gothic\";")
        ##label Цена от и Цена до и площадь от и до
        self.label_4.setText(_translate("MainWindow", "Цена от:"))
        self.label_5.setText(_translate("MainWindow", "Цена до:"))
        self.label_4.setStyleSheet("font: bold 10pt \"Century Gothic\";")
        self.label_5.setStyleSheet("font: bold 10pt \"Century Gothic\";")
        self.label_7.setText(_translate("MainWindow", "Площадь до:"))
        self.label_6.setText(_translate("MainWindow", "Площадь от:"))
        self.label_7.setStyleSheet("font: bold 10pt \"Century Gothic\";")
        self.label_6.setStyleSheet("font: bold 10pt \"Century Gothic\";")

        ##label Выбор параметров и доп параметры
        self.label_2.setText(_translate("MainWindow", "Выбор параметров:"))
        self.label_2.setStyleSheet("font: bold 10pt \"Century Gothic\";")

        self.label_8.setText(_translate("MainWindow", "Дополнительные \n"
" параметры:"))
        self.label_8.setStyleSheet("font: bold 10pt \"Century Gothic\";")
        

        #Названия параметров поиска (Мебель, TV и тд)
        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i].setText(_translate("MainWindow", self.listCheckBoxTitle[i]))
            v.setStyleSheet("font: 75 9pt \"Century Gothic\";")



        ##Название GroupBox - название объявлений 
        for i, v in enumerate(self.namesBoxes):
            name = ((self.res[list(self.res.keys())[i]]).split("\n"))[0]
            v.setStyleSheet("font: bold 9pt \"Century Gothic\";")
            v.setTitle(_translate("MainWindow", name))

            
        ##Текст объявлений 
        for i, v in enumerate(self.namesTexts):
            name = '<br>'.join(((self.res[list(self.res.keys())[i]]).split("\n"))[1:])

            v.setStyleSheet("font: 75 8pt \"Century Gothic\";")
            v.setHtml(_translate("MainWindow",name))

        ##Параметры сортировки
        self.namesComboBox = ["по ↑ цены","по ↓ цены", "по ↑ времени добавления", "по ↓ времени добавления"]
        for i, v in enumerate(self.namesComboBox):
            self.comboBox.setItemText(i,_translate("MainWindow", v))
        self.comboBox.setStyleSheet("font: 75 9pt \"Century Gothic\";")

        ##Количество комнат
        self.groupBox_Rooms.setTitle(_translate("MainWindow", "Количество комнат"))

        for i, v in enumerate(self.namesCheckBox_Rooms):
            v.setText(_translate("MainWindow", str(i+1) ))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
