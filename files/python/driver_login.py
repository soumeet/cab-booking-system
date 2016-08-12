#!C:\Python34\python.exe
import cgi
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
email=data.getvalue('log_email')
password=data.getvalue('log_password')
sts=-1
did=0
name=""

sql="SELECT * FROM DRIVER"
cur.execute(sql)
for r in cur:
	db_email=r[7]
	db_password=r[9]
	if db_email==email and db_password==password:
                sts=1
                break
    
if sts==1:
    sql="SELECT * FROM DRIVER WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
    cur.execute(sql)
    for r in cur:
        did=r[0]
        name=r[2]
        
    sql="INSERT INTO SESSIONS VALUES('DID', %s, '%s')" % (did, name)
    cur.execute(sql)
    cur.execute("commit")
    
    sql="UPDATE DRIVER SET STATUS = 'ONLINE' WHERE DRIVER_ID = %s" % (did)
    cur.execute(sql)
    cur.execute("commit")
        
    print("location: ../driver_homepage.html\r\n\r\n")
else:
    print("location: ../driver.html\r\n\r\n")