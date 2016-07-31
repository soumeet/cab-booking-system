#!C:\Python34\python.exe
import cgi
import cx_Oracle

#print('Content-type: text/html\r\n\r\n')
print('Content-type: application/json\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
sts=-1
customer_id=-1
name=data.getvalue('name')
gender=data.getvalue('gender')
dob=data.getvalue('dob')
mobile=data.getvalue('mobile')
email=data.getvalue('email')
address=data.getvalue('address')
password=data.getvalue('password')

# print('<h1> Customer Details: %s %s %s %s %s %s %s</h1>') % (name, gender, dob, mobile, email, address, password)
sql="INSERT INTO CUSTOMER(NAME, GENDER, DOB, STATUS, MOBILE, EMAIL, ADDRESS, PASSWORD) VALUES('%s', '%s', '%s', 'OFFLINE', '%s', '%s', '%s', '%s')" % (name, gender, dob, mobile, email, address, password)
#print('<h1>', sql, '</h1>')	
cur.execute(sql)
cur.execute('commit')
#print('<h3> Customer Registered</h3>')

sql="SELECT CUSTOMER_ID FROM CUSTOMER WHERE MOBILE = '%s' AND PASSWORD = '%s'" % (mobile, password)
#print(sql)
cur.execute(sql)
for r in cur:
    customer_id=r[0]
    sts=1
print("[\"", sts, "\",\"", customer_id, "\"]")