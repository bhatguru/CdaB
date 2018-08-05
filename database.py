#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("Users.db")
def listtable():
	a = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
	for items in a.fetchall():
		print(items)

def createTable():
	connection.execute("CREATE TABLE clientsreg(name_id integer auto_increment primary key, c_name varchar(20) NOT NULL, mobile_no int(15), pan_no int(12), GSTN varchar(16), dob text, it_paswd varchar(20), tan varchar(12), traces varchar(20), gstn_paswd varchar(20), owner text)")
	connection.commit()
	connection.close()
def createTable1():
	connection.execute("CREATE TABLE otherinfo(dsc varchar(20), data varchar(50), name_id integer, CONSTRAINT fk_clientsreg FOREIGN KEY (name_id) REFERENCES clientsreg(name_id) ON DELETE CASCADE)")
	connection.commit()
	connection.close()

def insertTable():
	connection.execute("INSERT INTO clientsreg VALUES (?,?,?,?,?,?,?,?,?,?,?)",(2,'vinay',9916788927,'CLXPB3086P','ABCD12345','27-1-1995','yash@123','TAN12345','TRACES123','GSTPASSWORD','guru'))
	connection.commit()
	connection.close()

def ViewTable():
	result = connection.execute("SELECT * FROM otherinfo")
	for data in result.fetchall():
		print (data)

def idgenerator():
	result = connection.execute("SELECT name_id FROM clientsreg")
	row = result.fetchall()
	currcount = len(row)
	newid = currcount +1
	print(newid)

def DeleteTable():
	connection.execute("DROP TABLE clientsreg")
	connection.commit()
	connection.close()

def insertuser(self):
	try:
		print('button clicked')
		usrname = self.reguser.text()
		passwrd = self.cregpaswd.text()
		if usrname != 'vinay':
			connection.execute("INSERT INTO USERS VALUES(?,?)", (usrname, passwrd))
			connection.commit()
			connection.close()
			self.msgsuccessful()
			self.reguser.clear()
			self.regpasswd.clear()
			self.cregpaswd.clear()
	except:
		self.error()

def UpdateData():
	name_id = 1
	c_name = 'vinay'
	updt = connection.execute("UPDATE clientsreg SET name_id = :name_id WHERE c_name = :c_name ",
						{'name_id': name_id, 'c_name': c_name})
	connection.commit()
# idgenerator()
# insertTable()
ViewTable()
# DeleteTable()
# listtable()
# createTable()
# UpdateData()
# createTable1()