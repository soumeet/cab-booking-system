#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
amount=float(data.getvalue('amount'))
sts=-2
rid=0
cid=0
bid=0
bill_status=""
bill_amount=0

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
cur.execute(sql)
for r in cur:
    cid=r[0]

sql="SELECT R.RIDE_ID FROM RIDE R, BILL B WHERE R.RIDE_ID = B.RIDE_ID AND B.STATUS = 'UNPAID' AND R.CUSTOMER_ID = %s" % (cid)
cur.execute(sql)
for r in cur:
    rid=r[0]
    
sql="SELECT BILL_ID, STATUS, AMOUNT FROM BILL WHERE RIDE_ID = %s" % (rid)
cur.execute(sql)
for r in cur:
    bid=r[0]
    bill_status=r[1]
    bill_amount=r[2]
 
if amount < bill_amount:
    due=bill_amount-amount
    sql="UPDATE BILL SET AMOUNT = %s WHERE BILL_ID = %s AND STATUS = 'UNPAID'" % (due, bid)
    cur.execute(sql)
    cur.execute('commit')
    sts=2
    
if amount == bill_amount:
    sql="UPDATE BILL SET AMOUNT = %s, STATUS = 'PAID' WHERE BILL_ID = %s AND STATUS = 'UNPAID'" % (amount, bid)
    cur.execute(sql)
    cur.execute('commit')
    sts=1

print("[\"", sts, "\"]")
