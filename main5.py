from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import resever5
import aboutus


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1280, 720)
        Main.setMaximumSize(QtCore.QSize(1280, 720))
        Main.setStyleSheet("background-color: rgba(47, 47, 47, 220);")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 70, 251, 241))
        self.logo.setStyleSheet("color: rgb(0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:/Users/ASUS/OneDrive/เดสก์ท็อป/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.btresever = QtWidgets.QPushButton(self.centralwidget)
        self.btresever.setGeometry(QtCore.QRect(980, 490, 235, 65))
        self.btresever.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(188, 125, 0, 220);\n"
"font: 57 18pt \"Mali Medium\";\n"
"border-radius:10;")
        self.btresever.setObjectName("btresever")
        self.tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidget.setGeometry(QtCore.QRect(270, 60, 631, 601))
        self.tablewidget.setStyleSheet("background-color: rgba(255, 255, 255, 220);")
        self.tablewidget.setObjectName("tablewidget")
        self.tablewidget.setColumnCount(4)
        self.tablewidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(3, item)
        self.listtext = QtWidgets.QLabel(self.centralwidget)
        self.listtext.setGeometry(QtCore.QRect(220, -20, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.listtext.setFont(font)
        self.listtext.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57 28pt \"Mali Medium\";")
        self.listtext.setObjectName("listtext")
        self.btaboutus = QtWidgets.QPushButton(self.centralwidget)
        self.btaboutus.setGeometry(QtCore.QRect(980, 590, 235, 65))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btaboutus.setFont(font)
        self.btaboutus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(188, 125, 0, 220);\n"
"font: 57 18pt \"Mali Medium\";\n"
"border-radius:10;\n"
"")
        self.btaboutus.setObjectName("btaboutus")
        self.btdelete_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btdelete_3.setGeometry(QtCore.QRect(50, 600, 111, 51))
        self.btdelete_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(167, 167, 167);\n"
"\n"
"font: 57 18pt \"Mali Medium\";\n"
"border-radius:10;\n"
"")
        self.btdelete_3.setObjectName("btdelete_3")
        self.idtext_2 = QtWidgets.QLabel(self.centralwidget)
        self.idtext_2.setGeometry(QtCore.QRect(970, 90, 71, 51))
        self.idtext_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Mali Medium\";")
        self.idtext_2.setObjectName("idtext_2")
        self.btdelete_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btdelete_4.setGeometry(QtCore.QRect(1120, 370, 111, 51))
        self.btdelete_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 57 18pt \"Mali Medium\";\n"
"border-radius:10;\n"
"")
        self.btdelete_4.setObjectName("btdelete_4")
        self.idinput_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.idinput_2.setGeometry(QtCore.QRect(1020, 100, 71, 41))
        self.idinput_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idinput_2.setObjectName("idinput_2")
        self.listtext_2 = QtWidgets.QLabel(self.centralwidget)
        self.listtext_2.setGeometry(QtCore.QRect(1000, 10, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.listtext_2.setFont(font)
        self.listtext_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57 28pt \"Mali Medium\";")
        self.listtext_2.setObjectName("listtext_2")
        self.idinput_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.idinput_3.setGeometry(QtCore.QRect(1030, 170, 151, 41))
        self.idinput_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idinput_3.setObjectName("idinput_3")
        self.namefix = QtWidgets.QLabel(self.centralwidget)
        self.namefix.setGeometry(QtCore.QRect(930, 160, 111, 51))
        self.namefix.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Mali Medium\";")
        self.namefix.setObjectName("namefix")
        self.namefix_2 = QtWidgets.QLabel(self.centralwidget)
        self.namefix_2.setGeometry(QtCore.QRect(930, 220, 111, 51))
        self.namefix_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Mali Medium\";")
        self.namefix_2.setObjectName("namefix_2")
        self.idinput_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.idinput_4.setGeometry(QtCore.QRect(1030, 230, 151, 41))
        self.idinput_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idinput_4.setObjectName("idinput_4")
        self.idinput_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.idinput_5.setGeometry(QtCore.QRect(1030, 290, 151, 41))
        self.idinput_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idinput_5.setObjectName("idinput_5")
        self.namefix_3 = QtWidgets.QLabel(self.centralwidget)
        self.namefix_3.setGeometry(QtCore.QRect(930, 280, 111, 51))
        self.namefix_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Mali Medium\";")
        self.namefix_3.setObjectName("namefix_3")
        self.btdelete_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btdelete_5.setGeometry(QtCore.QRect(1110, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btdelete_5.setFont(font)
        self.btdelete_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(167, 167, 167);\n"
"font: 57 14pt \"Mali Medium\";\n"
"border-radius:10;\n"
"")
        self.btdelete_5.setObjectName("btdelete_5")
        self.btdelete_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btdelete_6.setGeometry(QtCore.QRect(970, 370, 111, 51))
        self.btdelete_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 127);\n"
"font: 57 18pt \"Mali Medium\";\n"
"border-radius:10;\n"
"")
        self.btdelete_6.setObjectName("btdelete_6")
        self.namefix_3.raise_()
        self.namefix.raise_()
        self.listtext.raise_()
        self.logo.raise_()
        self.btresever.raise_()
        self.tablewidget.raise_()
        self.btaboutus.raise_()
        self.btdelete_3.raise_()
        self.idtext_2.raise_()
        self.btdelete_4.raise_()
        self.idinput_2.raise_()
        self.listtext_2.raise_()
        self.idinput_3.raise_()
        self.namefix_2.raise_()
        self.idinput_4.raise_()
        self.idinput_5.raise_()
        self.btdelete_5.raise_()
        self.btdelete_6.raise_()
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.btresever.setText(_translate("Main", "RESEVER [จองโต๊ะ]"))
        item = self.tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("Main", "ID"))
        item = self.tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("Main", "name"))
        item = self.tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("Main", "tel"))
        item = self.tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("Main", "zone"))
        self.listtext.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">List :</span></p></body></html>"))
        self.btaboutus.setText(_translate("Main", "ABOUT us"))
        self.btdelete_3.setText(_translate("Main", "Refresh"))
        self.idtext_2.setText(_translate("Main", "ID : "))
        self.btdelete_4.setText(_translate("Main", "DELETE"))
        self.listtext_2.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Edit List</span></p></body></html>"))
        self.namefix.setText(_translate("Main", "NAME : "))
        self.namefix_2.setText(_translate("Main", "TEL : "))
        self.namefix_3.setText(_translate("Main", "ZONE : "))
        self.btdelete_5.setText(_translate("Main", "checkID"))
        self.btdelete_6.setText(_translate("Main", "EDIT"))
        self.btresever.clicked.connect(self.openupload)
        self.btaboutus.clicked.connect(self.openaboutus)
        self.btdelete_3.clicked.connect(self.refresh)             #ปุ่มรีเฟส
        self.btdelete_4.clicked.connect(self.removeDatabase)      #ปุ่มลบ
        self.btdelete_4.clicked.connect(self.refresh)             #ปุ่มลบให้รีเฟส
        self.btdelete_5.clicked.connect(self.fecthID)             #ปุ่มเช็คไอดี
        self.btdelete_6.clicked.connect(self.editDatabase)        #ปุ่มเเก้ไข

    def openupload(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = resever5.Ui_resever()
        self.ui.setupUi(self.window)
        self.window.show()

    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = aboutus.Ui_about()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def refresh(self):
        print('refreshed data in the table')
        self.tablewidget.setRowCount(0)
        con = pymysql.connect(host="localhost", database="gewksix",user='root', password='')
        cursor = con.cursor()
        cursor.execute("SELECT ID,name,tel,zone FROM resever")
        data = list(cursor.fetchall())
        tablerow = 0
        for i in data:
            self.tablewidget.insertRow(tablerow)
            self.tablewidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tablewidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tablewidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tablewidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(i[3]))
            tablerow += 1

    def removeDatabase(self):                                            #ลบตาราง
        global ID
        ID = self.idinput_2.text()
        if (ID == ''):
            print("Please fill Menu ID")
        else:
            con = pymysql.connect(host="localhost", database="gewksix",
                                  user='root', password='')
            cursor = con.cursor()
            checkMenu = cursor.execute("SELECT ID FROM resever WHERE ID  = %s", ID )
            if checkMenu == 0:
                print('ไม่พบข้อมูล')
            else:
                cursor.execute("DELETE FROM resever WHERE ID  = %s", ID )
                con.commit()
                self.idinput_2.setText("")
                print("ลบข้อมูลสำเร็จ")
                con.close()

    def fecthID(self):                                            #เช็ค ID
        global ID
        ID = self.idinput_2.text()
        if ID == "":
            print("กรุณาใส่ไอดี")
        else:
            self.checkID()
    
    def checkID(self):                                                     #เช็ค ID ที่ทำงานต่อจากบรรทัดที่ 269     
        con = pymysql.connect(host="localhost", database="gewksix",
                              user='root', password='')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM resever WHERE ID = %s", ID)
        name = cursor.fetchone()
        if name == None:
            self.idinput_3.setText("ไม่พบชื่อเมนู")
            self.idinput_4.setText("ไม่พบชื่อเมนู")
            self.idinput_5.setText("ไม่พบชื่อเมนู")
            print("ไม่พบไอดีเมนู")
        else:
            self.fetchDatabase()
    
    def fetchDatabase(self):                                                  #เอาข้อมูลที่เช็คได้มาใส่ ในช่องที่เราพิมพ์
        print('fetching database')
        con = pymysql.connect(host="localhost", database="gewksix",
                              user='root', password='')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM resever WHERE ID = %s", ID)
        name = cursor.fetchone()
        cursor.execute("SELECT tel FROM resever WHERE ID = %s", ID)
        tel = cursor.fetchone()
        cursor.execute("SELECT zone FROM resever WHERE ID = %s", ID)
        zone = cursor.fetchone()
        self.idinput_3.setText(name[0])
        self.idinput_4.setText(tel[0])
        self.idinput_5.setText(zone[0])
        con.close()
    
    def editDatabase(self):                                             #ปุ่มedit
         name = self.idinput_3.text()
         tel = self.idinput_4.text()
         zone = self.idinput_5.text()
         if (   name == '' or tel == '' or zone == ''):
            print("Please fill all data")
         else:
            con = pymysql.connect(host="localhost", database="gewksix",
                                  user='root', password='')
            cursor = con.cursor()
            cursor.execute("UPDATE resever SET  name=%s, tel=%s, zone=%s WHERE ID = %s",
                           (name, tel, zone,ID))
            print("Edit data successfully")
            con.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
