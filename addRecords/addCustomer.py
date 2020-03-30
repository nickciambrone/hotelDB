#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import pymysql
import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
db = pymysql.connect("localhost","root","password","hotel" )
cursor = db.cursor()
cID = form.getvalue('cID')
name = form.getvalue('name')
dob = form.getvalue('dob')


sql = "INSERT INTO primaryCustomer (cID, name, DOB) VALUES ("+cID+", '"+name+"', '"+dob+"');"
cursor.execute(sql)

sql_ret = """SELECT * FROM primaryCustomer"""
cursor.execute(sql_ret)
primaryCustomer = cursor.fetchall()

print(primaryCustomer)

db.close()

