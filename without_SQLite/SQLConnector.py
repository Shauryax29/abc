import mysql.connector 

class  database:
    def __init__(self):
        self.mydb = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="1234" 
        ) 

        self.cursor = self.mydb.cursor()
        self.cursor.execute("""CREATE DATABASE if not exists Student""")
        self.cursor.execute("use student") 
        print("connected") if self.mydb.is_connected() else print("Not connected")
        self.createInfoTable()
        self.mydb.commit()

    def createInfoTable(self):
        self.cursor.execute('''CREATE TABLE if not exists information (
                            rollno integer primary key,
                            Name varchar(20),
                            course varchar(10),
                            mobileno varchar(10))''')
        print('Table created')

    def addInfo(self):
        rollno = input('enter roll no')
        name = input('enter name ')
        course = input('enter course')
        mobileno = input('enter mob no')
        add_info ='insert into information(rollno,name,course,mobileno)values(%s,%s,%s,%s)'
        info_data = (rollno,name,course,mobileno)
        self.cursor.execute(add_info,info_data)
        print('Data Saved')

    def showAllData(self):
        self.cursor.execute(""" select * from information""")
        data = self.cursor.fetchall()
        print(data)

    def showOneData(self):
        rollno = input('enter rollno.')
        query = ("select * from information where rollno = %s")
        self.cursor.execute(query,(rollno,))
        data = self.cursor.fetchone()
        print(data)

    def updateTable(self):
        rollno = input('enter roll no')
        name = input('enter name ')
        course = input('enter course')
        mobileno = input('enter mob no')
        update_info ='update information set name = %s, course =%s , mobno=%s where rollno = %s'
        self.cursor.execute(update_info,(name,course,mobileno))
        print('update succesfully')

    def deletedata(self):
        rollno = input('enter roll no.')
        update_query = 'delete from information where rollno = %s'
        self.cursor.execute(update_query,(rollno,))
        print('Deleted Sucessfully')

    def createAnotherTable(self):
        self.cursor.execute(''' CREATE TABLE if not exist Fee(
                                receiptno integer primary key,
                                rollno integer(20),
                                course varchar(10),
                                fee float )''')
        print('Table created')

    def joininginfo(self):
        query = 'select information.name,fee.receiptno, information.course, fee.fee from information inner join fee on information.rollno = fee.rollno'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)

    def errorHandling(self):
        reciptno = input('enter receiptno')
        rollno = input('enter rollno')
        course = input('enter course')
        fee = input('enter fee')
        try:
            addFee ='insert into Fee(recieptno,rollno,course,fee) values(%s,%s,%s,%s)'
            feeData = (reciptno,rollno,course,fee)
            self.cursor.execute(addFee,feeData)
            print('data saved')
        except mysql.connector.errors.IntegrityError:
            print('duplicate reciept no')
        





db = database() 
db.addInfo()    
db.showAllData()
db.showOneData()
db.updateTable()  
db.deletedata()  
db.createAnotherTable()
db.joininginfo()
db.errorHandling()
