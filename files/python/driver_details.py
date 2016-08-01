#!C:\Python34\python.exe
import cgi
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
did=data.getvalue('did')
sts=-1

sql="SELECT * FROM DRIVER WHERE DRIVER_ID = %s" % (did)
cur.execute(sql)
for r in cur:
    name=r[2]
    gender=r[3]
    dob=r[4].strftime('%d-%m-%Y')
    mobile=r[6]
    email=r[7]
    address=r[8]
    password=r[9]
    print("[\"", name, "\",\"", gender, "\",\"", dob, "\",\"", mobile, "\",\"", email, "\",\"", address, "\",\"", password, "\"]")