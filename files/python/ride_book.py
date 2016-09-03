#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
driver_name=data.getvalue('driver_name')
customer_name=data.getvalue('customer_name')
source=data.getvalue('source')
destination=data.getvalue('destination')
sts=-1
cid=0
did=0

sql="SELECT CUSTOMER_ID FROM CUSTOMER WHERE NAME = '%s'" % (customer_name)
cur.execute(sql)
for r in cur:
        cid=r[0]
sql="SELECT DRIVER_ID FROM DRIVER WHERE NAME = '%s'" % (driver_name)
cur.execute(sql)
for r in cur:
        did=r[0]
if sts==-1:
    sql="UPDATE DRIVER SET STATUS = 'REQUESTED' WHERE DRIVER_ID = %s" % (did)
    cur.execute(sql)
    cur.execute('commit')
    sql="UPDATE CUSTOMER SET STATUS = 'REQUESTED' WHERE CUSTOMER_ID = %s" % (cid)
    cur.execute(sql)
    cur.execute('commit')
    sql="INSERT INTO RIDE(DRIVER_ID, CUSTOMER_ID, SOURC, DESTN, STATUS) VALUES(%s, %s, '%s', '%s', 'REQUESTED')" % (did, cid, source, destination)
    cur.execute(sql)
    cur.execute('commit')
    sts=1

print("[\"", sts, "\"]")
