from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient

client = MongoClient("mongodb+srv://aditya:Aadi_747392@cluster0.23zaf.mongodb.net/Cluster0?retryWrites=true&w=majority")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 460)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(90, 70, 256, 311))
        self.graphicsView.setStyleSheet("background-color:rgb(241, 240, 241);border-radius:2px;")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 330, 141, 41))
        self.pushButton.setStyleSheet("border:0px solid black;background-color:rgb(67, 67, 255);\n"
"border-radius:3px;z-index:999;color:white;font-size:20px;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 180, 221, 31))
        self.lineEdit.setStyleSheet("border:1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 210, 221, 31))
        self.lineEdit_2.setStyleSheet("border:1px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 250, 111, 17))
        self.checkBox.setStyleSheet("background-color:transparent;")
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 151, 91))
        self.label.setStyleSheet("background-color:transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img.png"))
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.register)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.checkBox.setText(_translate("MainWindow", "Remeber Me"))

    def register(self):
        item1 = self.lineEdit.text()
        item2 = self.lineEdit_2.text()
        if item1 + "db" in client.list_database_names():
            pass
        else:
            db = client[item1 + "db"]
            coll = db['schema']
            print(coll)

            db2 = client[item1 + "db2"]
            coll2 = db2['schema']

            ins2 = {
                "title":"p",
                "pass":"p",
            }
            coll2.insert_one(ins2)
            coll2.delete_one({"title":"p"})
            ins = {
                "title":item1,
                "pass":item2,
            }
            coll.insert_one(ins)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
