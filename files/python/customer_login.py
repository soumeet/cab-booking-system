#!C:\Python34\python.exe
import cgi
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
email=data.getvalue('email')
password=data.getvalue('password')
sts=-1

sql="SELECT * FROM CUSTOMER"
cur.execute(sql)
for r in cur:
	db_email=r[6]
	db_password=r[8]
	if db_email==email and db_password==password:
                sts=1
                break
if sts==1:
	sql="SELECT * FROM CUSTOMER WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
	cur.execute(sql)
	for r in cur:
		cid=r[0]
		name=r[1]
	print("location: ../customer_homepage.html\r\n\r\n")
else:
        print("location: ../customer.html\r\n\r\n")
