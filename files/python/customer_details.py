#!C:\Python34\python.exe
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
cid=0
sts=-1

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
cur.execute(sql)
for r in cur:
    cid=r[0]

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