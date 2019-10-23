from dataGather.data import gatherRedditThreadsAndComments




def gatherRedditData(limit):
    if not type(limit) == int or not limit == 'n=None':
        TypeError("Limits must be an int or n=None")
    gatherRedditThreadsAndComments(limit)

