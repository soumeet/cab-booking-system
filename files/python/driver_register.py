#!C:\Python34\python.exe
import cgi
import cx_Oracle
import json

#print('Content-type: text/html\r\n\r\n')
print('Content-type: application/json\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
#print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
sts=-1
driver_id=-1
cab_id=data.getvalue('cab_id')
name=data.getvalue('name')
gender=data.getvalue('gender')
dob=data.getvalue('dob')
mobile=data.getvalue('mobile')
email=data.getvalue('email')
address=data.getvalue('address')
password=data.getvalue('password')

#print('<h2>Customer Details: ', cab_id, name, gender, dob, mobile, email, address, password'</h2>')
sql="INSERT INTO DRIVER(CAB_ID, NAME, GENDER, DOB, STATUS, MOBILE, EMAIL, ADDRESS, PASSWORD) VALUES(%s, '%s', '%s', '%s', 'OFFLINE', '%s', '%s', '%s', '%s')" % (cab_id, name, gender, dob, mobile, email, address, password)
#print('<h3>', sql, '</h3>')	
cur.execute(sql)
cur.execute('commit')
#print('<h3> Customer Registered</h3>')

sql="SELECT DRIVER_ID FROM DRIVER WHERE CAB_ID = %s" % (cab_id)
#print(sql)
cur.execute(sql)
for r in cur:
    driver_id=r[0]
    sts=1
print("[\"", sts, "\",\"", driver_id, "\"]")