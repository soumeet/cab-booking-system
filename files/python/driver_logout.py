#!C:\Python34\python.exe
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
sts=-1

if sts==-1:
        sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
        cur.execute(sql)
        for r in cur:
            did=r[0]
            
        sql="UPDATE DRIVER SET STATUS = 'OFFLINE' WHERE DRIVER_ID = %s" % (did)
        cur.execute(sql)
        cur.execute("commit")

        sql="DELETE FROM SESSIONS WHERE TYPE = 'DID' AND ID = %s" % (did)
        cur.execute(sql)
        cur.execute("commit")

        print("location: ../driver.html\r\n\r\n")
else:
        print("location: ../driver_homepage.html\r\n\r\n")
