
import dataGather as dat
from dataAnalysis import runDataAnalysis
import config

#Connect to Reddit and run the intial data collections
#Results should be a bunch of txt files with thread titles and comments inside of them
#dat.gatherRedditThreadsAndComments(config.limit)
#Add more config options ehre

#Here we scan each of the txt docs and count then number of time a word is used
#This will need more cleaning to remove words that were missed at first
#analyseFunctions.analysis(analyseFunctions.wordCounter(), config.targetSub)
runDataAnalysis(config.targetSub)

#Here we either remove all the txt files or store them for future use. See config.pu
#dat.dataCleanup(config.cleanUp, config.targetSub)
