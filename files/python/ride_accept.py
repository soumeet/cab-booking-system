#!C:\Python34\python.exe
import cx_Oracle
import datetime
import sys

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
sts=-1
cid=0
did=0
now=datetime.datetime.now().strftime("%d-%b-%y %H:%M")

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
cur.execute(sql)
for r in cur:
    did=r[0]

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
cur.execute(sql)
for r in cur:
    cid=r[0]

if sts==-1:
    sql="UPDATE RIDE SET UPTIME = '%s', STATUS = 'ACCEPTED' WHERE DRIVER_ID = %s AND CUSTOMER_ID = %s AND STATUS = 'REQUESTED'" % (now, did, cid)
    cur.execute(sql)
    cur.execute('COMMIT')
    sts=1

print("[\"", sts, "\"]")