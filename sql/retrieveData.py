from sql.sql import c as c

def getData(targetSub,topWordLimit=25):
    """
    Args: targetSug, topWordLimit=25\n
    Return: Array of words in thier ranked order\n

    """
    topRankedWords =[]

    if not type(targetSub) == str:
        raise TypeError('Please make sure the the target sub is a stirng')

    if not type(topWordLimit) == int:
        raise TypeError('The limit on the top words must be a int')
    c.execute('SELECT word FROM {} ORDER BY word_count DESC;'.format(targetSub))
    x = c.fetchall()
    if len(x) < topWordLimit:
        raise ValueError ('Limit is to big {} only contains {} entries'.format(targetSub,len(x)))
    for item in range(topWordLimit):
            stringifyWord = x[item][0]
            topRankedWords.append(stringifyWord)
    return topRankedWords
 
 


