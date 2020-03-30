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
din = form.getvalue('din')
dou = form.getvalue('dout')
cID = form.getvalue('cID')
pm = form.getvalue("pm")
rate = form.getvalue('rate')



sql = "INSERT INTO books VALUES ({},{},{},{},{},{});".format(rmNo, "'"+din+"'", "'"+dou+"'", cID,"'"+pm+"'", rate)
cursor.execute(sql)

sql_ret = """SELECT * FROM books"""
cursor.execute(sql_ret)
primaryCustomer = cursor.fetchall()

print(primaryCustomer)

db.close()

