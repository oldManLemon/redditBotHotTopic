#!/usr/bin/env python3

from dataGather import gatherRedditData,cleanUp
from dataAnalysis import runDataAnalysis
from sql import pushToDataBase
from sql.retrieveData import getData
import config
import post.post as p
import sys



#Connect to Reddit and run the intial data collections
#Results should be a bunch of txt files with thread titles and comments inside of them
def dataCollect():
    for item in config.targetSub:
        gatherRedditData(config.limit, item)
        #Here we scan each of the txt docs and count the total number of times a word is used
        runDataAnalysis(item)
        #SQL DataPush
        pushToDataBase(item)


        #REMOVE AND CLEAN
        cleanUp(config.cleanUp, item, 'txt') #Txt docs

        cleanUp(config.cleanUp, item, 'xml') #XML docs

def postData():
    for item in config.targetSub:
        postdata = getData(item)
        p.postToReddit(item,postdata)


    

if __name__== "__main__":
   
    if not len(sys.argv) == 1:
        ValueError('Expected one argument') 
    arg =str(sys.argv[1])
    if not type(arg) == str:
        raise TypeError("Must be a string")
    # if not arg == 'post' or not arg == 'gather':
    #     raise ValueError('exepcted args are post and gather')
    if arg == 'post':
        postData()
    elif arg == 'gather':
        dataCollect()
   





