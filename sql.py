# sql password KWD65@`b3*HgM6b5
# Turn on debug mode.
# import cgitb
# cgitb.enable()

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
#c.execute("SELECT VERSION()")
#res = c.fetchall()
# print(res)

# Create Table for data


def sortDataForInsert(filename):
    dataXml = open(filename, 'r+', encoding='utf8')
    arrayOfData = []
    for line in dataXml:
        line = line.split(',')
        word = line[0]
        count = int(line[1])
        arrayOfData.append([word, count])
    return arrayOfData


def checkTableExists(tableToCheck):
    if not type(tableToCheck) == str:

        raise TypeError('Table name must be in string form')
    # if not tableToCheck.isalnum():
    #     print('NO')
    #     raise ValueError('Must be no contain alphanumeric characters')

    c.execute(
        "   SELECT * FROM information_schema.tables WHERE table_name = '"+tableToCheck+"';")

    if(c.fetchone() == None):
        return False
    else:
        return True


def createSqlTable(tableToCreate):
    c.execute('CREATE TABLE IF NOT EXISTS '+tableToCreate +
              '( word VARCHAR(225) NOT NULL, word_count INT NOT NULL, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );')
    print(c.fetchone())


def insertSqlData(tableName, data):

    if checkTableExists(tableName):
        # Go ahead and insert all the data now
         for item in data:
            word = item[0]
            count = item[1]
            c.execute("INSERT INTO {} (word, word_count) VALUES ('{}',{});".format(tableName, word, count))
            conn.commit()
    else:
        # CREATE THE TABLE THEN ADD THE DATA
        createSqlTable(tableName)
        for item in data:
            word = item[0]
            count = item[1]
            c.execute("INSERT INTO {} (word, word_count) VALUES ('{}',{});".format(tableName, word, count))
            conn.commit()

x = sortDataForInsert('melbourne_results.xml')
insertSqlData('melbourne', x)


# Insert some example data.
#c.execute("INSERT INTO numbers VALUES (1, 'One!')")
#c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
#c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
# conn.commit()

# Print the contents of the database.
##c.execute("SELECT * FROM numbers")
# print([(r[0], r[1]) for r in c.fetchall()])c.execute("INSERT INTO numbers VALUES (1, 'One!')")
