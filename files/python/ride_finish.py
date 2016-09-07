#!C:\Python34\python.exe
import cgi
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
distance=float(data.getvalue('distance'))
sts=-2
cid=0
did=0
rid=0
amount=0
mileage=0
now=datetime.datetime.now().strftime("%d-%b-%y %H:%M")

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
cur.execute(sql)
for r in cur:
    did=r[0]

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
cur.execute(sql)
for r in cur:
    cid=r[0]
    
if sts==-2:
    sql="UPDATE DRIVER SET STATUS = 'ONLINE' WHERE DRIVER_ID = %s" % (did)
    cur.execute(sql)
    cur.execute('commit')
    sql="UPDATE CUSTOMER SET STATUS = 'ONLINE' WHERE CUSTOMER_ID = %s" % (cid)
    cur.execute(sql)
    cur.execute('commit')
    sql="UPDATE RIDE SET DOWNTIME = '%s', DISTANCE = %s, STATUS = 'FINISHED' WHERE DRIVER_ID = %s AND CUSTOMER_ID = %s AND STATUS = 'ACCEPTED'" % (now, distance, did, cid)
    cur.execute(sql)
    cur.execute('COMMIT')
    sts=-1

    
sql="SELECT C.COST_PER_KM FROM CAB C, DRIVER D WHERE D.CAB_ID = C.CAB_ID AND D.DRIVER_ID = %s" % (did)
cur.execute(sql)
for r in cur:
    mileage=r[0]
sql="SELECT RIDE_ID FROM RIDE WHERE DRIVER_ID = %s AND CUSTOMER_ID = %s AND DISTANCE = %s AND STATUS = 'FINISHED'" % (did, cid, distance)
cur.execute(sql)
for r in cur:
    rid=r[0]
    
amount=distance*mileage
now=datetime.datetime.now().strftime("%d-%b-%y")

if sts==-1:
    sql="INSERT INTO BILL(RIDE_ID, BILL_DATE, STATUS, AMOUNT) VALUES(%s, '%s', 'UNPAID', %s)" % (rid, now, amount)
    cur.execute(sql)
    cur.execute('COMMIT')
    sts=1

print("[\"", sts, "\"]")