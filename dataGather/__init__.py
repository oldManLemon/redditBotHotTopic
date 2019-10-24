from dataGather.data import gatherRedditThreadsAndComments
from dataGather.dataClean import dataCleanup




def gatherRedditData(limit, targetSub):
    if not type(limit) == int or not limit == 'n=None':
        TypeError("Limits must be an int or n=None")
    if not type(targetSub) == str:
        raise TypeError("targetSub is the target subreddit and must be a string")
    gatherRedditThreadsAndComments(limit, targetSub)

def cleanUp(action, targetedSub, dataType):
    dataCleanup(action, targetedSub, dataType)

