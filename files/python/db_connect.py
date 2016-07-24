#!C:\Python34\python.exe
import cx_Oracle
con=cx_Oracle.connect('cbs/apss@localhost/xe')
print(con, ' ', con.version)