#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
type=data.getvalue('type')
name=""
sts=-1

if sts==-1:
    if type=='did':
        sql="SELECT NAME FROM SESSIONS WHERE TYPE = 'DID'"
    if type=='cid':
        sql="SELECT NAME FROM SESSIONS WHERE TYPE = 'CID'"
    cur.execute(sql)
    for r in cur:
        name=r[0]
    print("[\"", name, "\"]")