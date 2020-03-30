#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import pymysql
import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
db = pymysql.connect("localhost","root","password","hotel" )
cursor = db.cursor()
rmNo = form.getvalue('rmNo')





sql_ret = "SELECT DISTINCT * FROM books WHERE roomNumber = {}{}".format(rmNo,";")
cursor.execute(sql_ret)
primaryCustomer = cursor.fetchall()

print(primaryCustomer)

db.close()

