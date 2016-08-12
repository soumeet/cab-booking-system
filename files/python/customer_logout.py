#!C:\Python34\python.exe
import cgi
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
cid=data.getvalue('cid')
sts=-1

if sts==-1:
    sql="SELECT ID FROM SESSIONS WHERE TYPE = 'CID'"
    cur.execute(sql)
    for r in cur:
        cid=r[0]

    sql="UPDATE CUSTOMER SET STATUS = 'OFFLINE' WHERE CUSTOMER_ID = %s" % (cid)
    cur.execute(sql)
    cur.execute("commit")

    sql="DELETE FROM SESSIONS WHERE TYPE = 'CID' AND ID = %s" % (cid)
    cur.execute(sql)
    cur.execute("commit")

    print("location: ../customer.html\r\n\r\n")
else:
    print("location: ../customer_homepage.html\r\n\r\n")
