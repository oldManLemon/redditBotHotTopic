#sql password KWD65@`b3*HgM6b5
# Turn on debug mode.
# import cgitb
# cgitb.enable()

# Print necessary headers.
# print("Content-Type: text/html")
# print()
import numpy as np
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
#c.execute("SELECT VERSION()")
#res = c.fetchall()
#print(res)

#Create Table for data
def insertData(filename):
    dataXml = open(filename,'r+', encoding='utf8')
    arrayOfData =[]
    for line in dataXml:
        #print(line[-2])
        line = stringToTuple(line)
        arrayOfData.append(line)
    return arrayOfData
        


#conver str to tupel
def stringToTuple(tupleString):
    

    # print(type(tupleString))
    #print(tupleString[-2])
    print(tupleString[0] , tupleString[-2])
    assert tupleString[0] == "(" and tupleString[-2] == ")"
    elements = tupleString[1:-2].split(",") #tupleString[1:-1] all elements but last one. Then spliT
    mytuple = tuple(elements)
    return mytuple


            
demoFile = 'melbourne_results.xml'
demoWorking = 'working.xml'
#print(insertData(demoFile))
string = "Special: $#! characters.   sp,aces 888323"
string = ''.join(e for e in string if e.isalnum())
print(string)

# Insert some example data.
#c.execute("INSERT INTO numbers VALUES (1, 'One!')")
#c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
#c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
#conn.commit()

# Print the contents of the database.
##c.execute("SELECT * FROM numbers")
#print([(r[0], r[1]) for r in c.fetchall()])c.execute("INSERT INTO numbers VALUES (1, 'One!')")
