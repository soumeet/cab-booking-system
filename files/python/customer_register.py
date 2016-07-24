#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content -type: text/html\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
# fname=data.getvalue('fname')
# lname=data.getvalue('lname')
name=data.getvalue('name')
gender=data.getvalue('gender')
dob=data.getvalue('dob')
mobile=data.getvalue('mobile')
email=data.getvalue('email')
address=data.getvalue('address')
password=data.getvalue('password')

# print('<h1> Customer Details: %s %s %s %s %s %s %s</h1>') % (name, gender, dob, mobile, email, address, password)
sql="INSERT INTO CUSTOMER(NAME, GENDER, DOB, STATUS, MOBILE, EMAIL, ADDRESS, PASSWORD) VALUES('%s', '%s', '%s', 'OFFLINE', '%s', '%s', '%s', '%s')" % (name, gender, dob, mobile, email, address, password)
print('<h1>', sql, '</h1>')	
# cur.execute(sql)
cur.execute('commit')
print('<h3> Customer Registered</h3>')
# print('<h1>Hello World</h1>')