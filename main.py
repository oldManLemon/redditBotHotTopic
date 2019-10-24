from dataGather import gatherRedditData,cleanUp
from dataAnalysis import runDataAnalysis
from sql import pushToDataBase
import config

#Connect to Reddit and run the intial data collections
#Results should be a bunch of txt files with thread titles and comments inside of them
#dat.gatherRedditThreadsAndComments(config.limit)
for item in config.targetSub:

    gatherRedditData(config.limit, item)
    #Add more config options ehre

    #Here we scan each of the txt docs and count then number of time a word is used
    #This will need more cleaning to remove words that were missed at first
    #analyseFunctions.analysis(analyseFunctions.wordCounter(), config.targetSub)

    runDataAnalysis(item)

    #SQL Stuff
    pushToDataBase(item)


    #REMOVE AND CLEAN
    cleanUp(config.cleanUp, item, 'txt') #Txt docs

    cleanUp(config.cleanUp, item, 'xml') #XML docs

    #Here we either remove all the txt files or store them for future use. See config.pu
    #dat.dataClean.dataCleanup(config.cleanUp, config.targetSub, 'txt')
    #dat.dataClean.dataCleanup(config.cleanUp, config.targetSub, 'xml')

