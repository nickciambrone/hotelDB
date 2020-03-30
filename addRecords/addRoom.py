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
occ = form.getvalue('occ')
floor = form.getvalue('floor')
edisc = form.getvalue('edisc')
spRate = form.getvalue('spRate')
suRate = form.getvalue('suRate')
faRate = form.getvalue('faRate')
wiRate = form.getvalue('wiRate')
jac = form.getvalue('jac')
smo = form.getvalue('smo')

sql = "INSERT INTO room VALUES ("+rmNo+", "+occ+", "+floor+", "+edisc+", "+spRate+", "+suRate+", "+faRate+", "+wiRate+", "+jac+", "+smo+",'..'"+");"
cursor.execute(sql)

sql_ret = """SELECT * FROM room"""
cursor.execute(sql_ret)
primaryCustomer = cursor.fetchall()

print(primaryCustomer)

db.close()

