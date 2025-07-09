from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import latemain
import DBManager as db
class latehome:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = latemain.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.db = db.DBManager()
        self.ui.pushButton_3.clicked.connect(self.showSignup)
        self.ui.pushButton_2.clicked.connect(self.showForgetpass)
        self.ui.pushButton_6.clicked.connect(self.showLogin)
        self.ui.pushButton_5.clicked.connect(self.showLogin)
        self.ui.pushButton_4.clicked.connect(self.handleSignup)
        self.ui.pushButton.clicked.connect(self.handlelogin)
        MainWindow.show()
        sys.exit(app.exec_())

    def showSignup(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page)
    def showForgetpass(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)
    def showLogin(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_2Page1)
    def handleSignup(self):
        name = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()
        status = self.db.saveUser(name=name, email = email, password = password)
        if status == 1:
            QMessageBox.information(self.ui.stackedWidget_2Page1,"Sucess","User Created")
        elif status == 2:
            QMessageBox.information(self.ui.stackedWidget_2Page1, "Error","User already created")
        else:
            QMessageBox.information(self.ui.stackedWidget_2Page1, "Error", " error")

    def handlelogin(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        status=self.db.showUser(email=email,password=password)
        if status:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        else:
            QMessageBox.information(self.ui.stackedWidget_2Page1, "Invalid","Invalid email and pasword")
            
if __name__ == '__main__':
    latehome()
