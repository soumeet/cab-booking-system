#!C:\Python34\python.exe
import cgi
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
did=data.getvalue('did')
sts=-1

if sts==-1:
	sql="UPDATE DRIVER SET STATUS = 'OFFLINE' WHERE DRIVER_ID = %s" % (did)
	cur.execute(sql)
	cur.execute("commit")
	print("location: ../driver.html\r\n\r\n")
else:
        print("location: ../driver_homepage.html\r\n\r\n")
