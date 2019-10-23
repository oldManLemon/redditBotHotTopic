from dataGather.data import gatherRedditThreadsAndComments
from dataGather.dataClean import dataCleanup




def gatherRedditData(limit):
    if not type(limit) == int or not limit == 'n=None':
        TypeError("Limits must be an int or n=None")
    gatherRedditThreadsAndComments(limit)

def cleanUp(action, targetedSub, dataType):
    dataCleanup(action, targetedSub, dataType)

