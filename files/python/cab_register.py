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
sts=-1
cab_id=-1
reg_no=data.getvalue('reg_no')
typ=data.getvalue('type')
name=data.getvalue('name')
cost_per_km=data.getvalue('cost_per_km')

#print('<h1> Cab Details: ', reg_no, typ, name, cost_per_km, '</h1>')
sql="INSERT INTO CAB(REG_NO, TYPE, NAME, COST_PER_KM) VALUES('%s', '%s', '%s', %s)" % (reg_no, typ, name, cost_per_km)
#print('<h1>', sql, '</h1>')	
cur.execute(sql)
cur.execute('commit')
#print('<h3> Cab Registered</h3>')

sql="SELECT CAB_ID FROM CAB WHERE REG_NO = '%s'" % (reg_no)
#print(sql)
cur.execute(sql)
for r in cur:
    cab_id=r[0]
    sts=1
print("[\"", sts, "\",\"", cab_id, "\"]")