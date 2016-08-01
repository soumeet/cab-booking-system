#!C:\Python34\python.exe
import cgi
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
cid=data.getvalue('cid')
sts=-1

sql="SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = %s" % (cid)
cur.execute(sql)
for r in cur:
    name=r[1]
    gender=r[2]
    dob=r[3].strftime('%d-%m-%Y')
    mobile=r[5]
    email=r[6]
    address=r[7]
    password=r[8]
    print("[\"", name, "\",\"", gender, "\",\"", dob, "\",\"", mobile, "\",\"", email, "\",\"", address, "\",\"", password, "\"]")