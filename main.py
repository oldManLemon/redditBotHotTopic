from dataGather import gatherRedditData,cleanUp
from dataAnalysis import runDataAnalysis
from sql import pushToDataBase
from sql.retrieveData import getData
import config
import post.post as p

#Connect to Reddit and run the intial data collections
#Results should be a bunch of txt files with thread titles and comments inside of them

# for item in config.targetSub:

#     gatherRedditData(config.limit, item)
    

#     #Here we scan each of the txt docs and count the total number of times a word is used
#     runDataAnalysis(item)

#     #SQL DataPush
#     pushToDataBase(item)


#     #REMOVE AND CLEAN
#     cleanUp(config.cleanUp, item, 'txt') #Txt docs

#     cleanUp(config.cleanUp, item, 'xml') #XML docs

for item in config.targetSub:
    postdata = getData(item)
    p.postToReddit(item,postdata)



