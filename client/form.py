#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import pymysql


import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
db = pymysql.connect("localhost","root","password","stockMarket" )
cursor = db.cursor()
sql = form.getvalue('fname')
cursor.execute(sql)
data = cursor.fetchall()
print("<table>")
for x in data:
        print("<tr>")
        print("<td>",x,"</td>")
        print("</tr>")


print("</table>")

db.close()


