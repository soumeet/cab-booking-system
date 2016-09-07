#!C:\Python34\python.exe
import cgi
import cx_Oracle
import json

#print('Content-type: text/html\r\n\r\n')
print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
source=data.getvalue('source')
destination=data.getvalue('destination')
typ=data.getvalue('type')
sts=-1

if typ=="TYPE":
    sql="SELECT D.NAME, C.TYPE, C.NAME, C.COST_PER_KM FROM DRIVER D, CAB C WHERE D.CAB_ID = C.CAB_ID AND D.STATUS = 'ONLINE'"
else:
    sql="SELECT D.NAME, C.TYPE, C.NAME, C.COST_PER_KM FROM DRIVER D, CAB C WHERE D.CAB_ID = C.CAB_ID AND D.STATUS = 'ONLINE' AND C.TYPE = '%s'" % (typ)
#print(sql)
cur.execute(sql)

no_of_row=1
for r in cur:
    no_of_row=cur.rowcount

cur.execute(sql)
print("[")
i=1
for r in cur:
    driver_name=r[0]
    vehicle_type=r[1]
    vehicle_name=r[2]
    mileage=r[3]
    print("[\"", driver_name, "\",\"", vehicle_type, "\",\"", vehicle_name, "\",\"", mileage, "\"]")
    if i!=no_of_row:
        print(",")
        i=i+1
print("]")