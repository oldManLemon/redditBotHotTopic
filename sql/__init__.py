
from sql.sql import sortDataForInsert, getSubRedditResults,insertSqlData
import sql.retrieveData

def pushToDataBase(targetSub):
    theData = sortDataForInsert(getSubRedditResults(targetSub))
    return insertSqlData(targetSub, theData)