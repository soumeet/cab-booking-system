#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content-type: application/json\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
sts=-1
did=data.getvalue('did')
name=data.getvalue('name')
gender=data.getvalue('gender')
dob=data.getvalue('dob')
mobile=data.getvalue('mobile')
email=data.getvalue('email')
address=data.getvalue('address')
password=data.getvalue('password')

sql="UPDATE DRIVER SET NAME = '%s', GENDER = '%s', DOB = '%s', MOBILE = '%s', EMAIL = '%s', ADDRESS = '%s', PASSWORD = '%s' WHERE DRIVER_ID = %s" % (name, gender, dob, mobile, email, address, password, did)
cur.execute(sql)
cur.execute('commit')
sts=1

print("[\"",sts,"\"]")