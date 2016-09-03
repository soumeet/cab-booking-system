#!C:\Python34\python.exe
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
sts=-1

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
cur.execute(sql)
for r in cur:
    did=r[0]

sql="SELECT C.NAME, B.BILL_DATE, R.SOURC, R.DESTN, R.UPTIME, R.DOWNTIME, R.DISTANCE, B.AMOUNT FROM BILL B, CUSTOMER C, DRIVER D, RIDE R WHERE R.DRIVER_ID = D.DRIVER_ID AND R.CUSTOMER_ID = C.CUSTOMER_ID AND B.RIDE_ID = R.RIDE_ID AND D.DRIVER_ID = %s" % (did)
cur.execute(sql)

no_of_row=1
for r in cur:
    no_of_row=cur.rowcount

cur.execute(sql)
print("[")
i=1
for r in cur:
    customer_name=r[0]
    bill_date=r[1].strftime('%d-%m-%Y')
    source=r[2]
    destination=r[3]
    uptime=r[4].strftime('%H:%M')
    downtime=r[5].strftime('%H:%M')
    distance=r[6]
    amount=r[7]
    print("[\"", customer_name, "\",\"", bill_date, "\",\"", source, "\",\"", destination, "\",\"", uptime, "\",\"", downtime, "\",\"", distance, "\",\"", amount, "\"]")
    if i!=no_of_row:
        print(",")
        i=i+1
print("]")