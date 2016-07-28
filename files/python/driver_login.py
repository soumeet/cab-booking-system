#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content -type: text/html\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
email=data.getvalue('email')
password=data.getvalue('password')
sts=-1

# print('<h1>', email, password, '</h1>')

sql="SELECT * FROM CUSTOMER"
cur.execute(sql)
for r in cur:
	db_email=r[6]
	db_password=r[8]
	# print('<h3>',db_email, db_password, email, password, '</h3>')
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
	print('<h2> Customer Loged in</h2>')
	# sql="UPDATE CUSTOMER SET STATUS = 'ONLINE' WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
	# cur.execute(sql)
	# cur.execute('commit')
    '''
    sql="SELECT * FROM CUSTOMER WHERE EMAIL = '%s' AND PASSWORD = '%s'" % (email, password)
	cur.execute(sql)
	for r in cur:
		print('<h3>Name: ',r[1],'</h3>')
		print('<h3>Gender: ',r[2],'</h3>')
		print('<h3>Date Of Birth: ',r[3],'</h3>')
		print('<h3>Mobile',r[5],'</h3>')
		print('<h3>Email: ',r[6],'</h3>')
		print('<h3>Address: ',r[7],'</h3>')
    '''
    
if sts==-1:
	print('<h2>Wrong Password</h2>')
# if sts==-2:
# 	print('<h3>Account not Registered</h3>')
