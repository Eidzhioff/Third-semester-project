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
        self.pushButton.setText(_translate("MainWindow", "Расчитать ипотеку"))


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        
        
        QtWidgets.QDialog.resize(self, 333, 404) #Размер основного окна
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 331, 80))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QLineEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 9, 331, 31))
        self.label.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label.setObjectName("label")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 80, 331, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(0, 9, 331, 31))
        self.label_2.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_2.setObjectName("label_2")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 160, 331, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.textEdit_3.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(0, 9, 331, 31))
        self.label_3.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        
        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 240, 331, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.textEdit_4.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(0, 9, 331, 31))
        self.label_4.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        
        self.groupBox_5 = QtWidgets.QGroupBox(self)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 320, 331, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_5.setGeometry(QtCore.QRect(130, 40, 191, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(0, 9, 331, 31))
        self.label_5.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(0, 40, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ipot)
        
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", " Введите стоимость недвижимости:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_2.setText(_translate("MainWindow", "Срок, на который взяли кредит:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_3.setText(_translate("MainWindow", "Введите первоначальный взнос:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_4.setText(_translate("MainWindow", "Введите под каким процентом взяли кредит:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_5.setText(_translate("MainWindow", "Итог:"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        
        
    def ipot(self):
        # Стоимость недвижимости
        n = int(self.textEdit.text())
        # Срок кредитования
        m = int(self.textEdit_2.text())
        # Первоначальный взнос
        v = int(self.textEdit_3.text())
        # Ежемесяцная ставка по кредиту
        p = int(self.textEdit_4.text())
        # Общая сумма кредита
        s = n - m
        
        x = round((s*p)/(1-(1+p)*(1-m)))  
        
        self.textEdit_5.setText(str(x))
        
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