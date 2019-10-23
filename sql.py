import datetime
# Connect to the database.
import pymysql
from password import sqlPassword
conn = pymysql.connect(
    db='popular',
    user='popularBot',
    passwd=sqlPassword,
    host='localhost')
c = conn.cursor()

def log(information):
    day = datetime.date.today()
    time = datetime.datetime.now()
    
    log = open(str(day)+'.log', 'a+')
    log.write('{}: {}\n'.format(time, information))
    log.close()





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
    #print(c.fetchone())
    log('Created new table {}'.format(tableToCreate))

def catchError(word, count):
    if not type(word) == str:
        raise TypeError('Word must be a string, please check your data')
    if not type(count) == int:
        raise TypeError('Count must be an int')


def insertSqlData(tableName, data):

    if checkTableExists(tableName):
        
        # Go ahead and insert all the data now
         for item in data:
            #We need to check all the being added so as not to duplicate
            word = item[0]
            count = item[1]
            catchError(word,count)
            
            c.execute("SELECT word, word_count FROM {} WHERE word ='{}';".format(tableName,word))
            request = c.fetchone()
            if request == None:
                #Word not found in list add it with all data
                log('Did not find {} will now add it with count to list'.format(word))
                c.execute("INSERT INTO {} (word, word_count) VALUES ('{}',{});".format(tableName, word, count))
                conn.commit()
            else:
                log('Found word: will add new count to {}'.format(word))
                oldNum = request
                #print(oldNum[1])
                newNum = count + oldNum[1]
                c.execute("UPDATE {} SET word_count = {} WHERE word = '{}';".format(tableName,newNum,word))
                conn.commit()
    else:
        # CREATE THE TABLE THEN ADD THE DATA
        createSqlTable(tableName)
        
        for item in data:
            word = item[0]
            count = item[1]
            log('Did not find {} will now add it with count to list'.format(word))
            c.execute("INSERT INTO {} (word, word_count) VALUES ('{}',{});".format(tableName, word, count))
            conn.commit()

x = sortDataForInsert('brisbane_results.xml')
insertSqlData('brisbane', x)





