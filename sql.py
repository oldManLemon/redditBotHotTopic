#sql password KWD65@`b3*HgM6b5
# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
# print("Content-Type: text/html")
# print()

# Connect to the database.
import pymysql
from password import sqlPassword
conn = pymysql.connect(
    db='popular',
    user='popularBot',
    passwd=sqlPassword,
    host='localhost')
c = conn.cursor()
#c.execute('SHOW VARIABLES LIKE "%version%";')
c.execute("SELECT VERSION()")
res = c.fetchall()
print(res)

# Insert some example data.
#c.execute("INSERT INTO numbers VALUES (1, 'One!')")
#c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
#c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
#conn.commit()

# Print the contents of the database.
##c.execute("SELECT * FROM numbers")
#print([(r[0], r[1]) for r in c.fetchall()])c.execute("INSERT INTO numbers VALUES (1, 'One!')")
