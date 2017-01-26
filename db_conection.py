import cx_Oracle
import sys
import os

os.environ["NLS_LANG"] = "JAPANESE_JAPAN.JA16SJISTILDE"
db_user = 'dynpt01'
db_pass = 'dynpt'
db_host = '(DESCRIPTION=(ADDRESS = (PROTOCOL = TCP)(HOST = 10.6.2.195)(PORT = 1521)) (CONNECT_DATA =(SERVER = DEDICATED)(SID = SETORA)))'
con = cx_Oracle.connect(db_user, db_pass, db_host)

cur = con.cursor()
sql = 'select user_id, agent_name from sys_user order by 1'
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    user_id = row[0]
    agent_name = row[1]
    print( agent_name)


print (sys.stdin.encoding)
print (sys.stdout.encoding)
print (sys.stderr.encoding)
