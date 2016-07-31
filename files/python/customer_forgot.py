#!C:\Python34\python.exe
import cgi
import cx_Oracle
import json

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
sts=-1
password=-1
email=data.getvalue('email')
dob=data.getvalue('dob')

sql="SELECT PASSWORD FROM CUSTOMER WHERE EMAIL = '%s' AND DOB = '%s'" % (email, dob)
cur.execute(sql)
for r in cur:
    password=r[0]
    sts=1

print("[\"", sts, "\",\"", password, "\"]")