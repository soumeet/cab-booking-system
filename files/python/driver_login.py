#!C:\Python34\python.exe
import cgi
import cx_Oracle

#print('Content-type: text/html\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
email=data.getvalue('email')
password=data.getvalue('password')
sts=-1

# print('<h1>', email, password, '</h1>')

sql="SELECT * FROM DRIVER"
cur.execute(sql)
for r in cur:
	db_email=r[7]
	db_password=r[9]
#	print('<h3>',db_email, db_password, email, password, '</h3>')
	if db_email==email and db_password==password:
                sts=1
                break
	# if db_email==email and not db_password==password:
	# 	sts=-1
	# if not db_email==email and db_password==password:
	# 	sts=-2
	# if not db_email==email and not db_password==password:
	# 	sts=-2

if sts==1:
#    print("Location: ../driver_homepage.html")
	print('<h2> Driver Loged in</h2>')
	# sql="UPDATE DRIVER SET STATUS = 'ONLINE' WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
	# cur.execute(sql)
	# cur.execute('commit')

#	sql="SELECT * FROM DRIVER WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
#	cur.execute(sql)
#	for r in cur:
#                print('<h3>Name: ',r[2],'</h3>')
#                print('<h3>Gender: ',r[3],'</h3>')
#                print('<h3>Date Of Birth: ',r[4],'</h3>')
#                print('<h3>Mobile',r[6],'</h3>')
#                print('<h3>Email: ',r[7],'</h3>')
#                print('<h3>Address: ',r[8],'</h3>')
    
#if sts==-1:
#	print('<h2>Wrong Password</h2>')
# if sts==-2:
# 	print('<h3>Account not Registered</h3>')
