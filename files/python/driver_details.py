#!C:\Python34\python.exe
import cx_Oracle
import datetime

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
did=0
sts=-1

sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
cur.execute(sql)
for r in cur:
    did=r[0]

sql="SELECT D.*, C.NAME, C.REG_NO, C.COST_PER_KM FROM DRIVER D, CAB C WHERE D.CAB_ID = C.CAB_ID AND D.DRIVER_ID = %s" % (did)
cur.execute(sql)
for r in cur:
    name=r[2]
    gender=r[3]
    dob=r[4].strftime('%d-%m-%Y')
    mobile=r[6]
    email=r[7]
    address=r[8]
    password=r[9]
    cab_name=r[10]
    cab_regno=r[11]
    cab_mileage=r[12]
    print("[\"", name, "\",\"", gender, "\",\"", dob, "\",\"", mobile, "\",\"", email, "\",\"", address, "\",\"", password, "\",\"", cab_name, "\",\"", cab_regno, "\",\"", cab_mileage, "\"]")