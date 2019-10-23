
from sql.sql import sortDataForInsert, getSubRedditResults,insertSqlData

def pushToDataBase(targetSub):
    theData = sortDataForInsert(getSubRedditResults(targetSub))
    return insertSqlData(targetSub, theData)