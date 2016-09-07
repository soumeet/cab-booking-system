#!C:\Python34\python.exe
import cgi
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
did=-1
cid=-1
rid=-1
source=""
destination=""
uptime=""
downtime=""
distance=0
amount=0
bill_status="-1"
sts=""

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
cur.execute(sql)
for r in cur:
    did=r[0]

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
cur.execute(sql)
for r in cur:
    cid=r[0]

sql="SELECT * FROM RIDE WHERE DRIVER_ID = %s AND CUSTOMER_ID = %s" % (did, cid)
cur.execute(sql)
for r in cur:
    rid=r[0]
    source=r[3]
    destination=r[4]
    if isinstance(r[5], datetime.datetime):
        uptime=r[5].strftime('%d-%b-%y %H:%M')
    else:
        uptime="-1"
    if isinstance(r[6], datetime.datetime):
        downtime=r[6].strftime('%d-%b-%y %H:%M')
    else:
        downtime="-1"
    if r[7]!='None':
        distance=r[7]
    else:
        distance=-1
    sts=r[8]

sql="SELECT STATUS, AMOUNT FROM BILL WHERE RIDE_ID = %s " % (rid)
cur.execute(sql)
for r in cur:
    bill_status=r[0]
    amount=r[1]

print("[\"", rid, "\",\"", did, "\",\"", cid, "\",\"", source, "\",\"", destination, "\",\"", uptime, "\",\"", downtime, "\",\"", distance, "\",\"", sts, "\",\"", bill_status, "\",\"", amount, "\"]")
