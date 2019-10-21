# Reddit Bot First Run
import praw
# Inbuilts
import os
from collections import Counter

# just import the password
import password


# https://www.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='JL53WY5Cw2WK8g',
                     client_secret='fKqCZ44PIIFdqOjemTIKab0BfEs',
                     # password='popularWordBot!',
                     password=password.password,
                     user_agent='popularWordBot Script',
                     username='popularWordBot')

sub = reddit.subreddit('australia')


def gatherHotPage(limit):
    postID = []
    for submission in sub.hot(limit=limit):
        loging = open(submission.id+'.txt', 'w+', encoding="utf-8")
        loging.write(str(submission.title)+'\n')
        loging.close()
        postID.append(submission.id)

    return postID


def readComments(submissionID):

    sub = reddit.submission(id=submissionID)
    sub.comments.replace_more(limit=None)
    # encoding needed to deal with emojis
    # may use another method of getting data.
    loging = open(submissionID+'.txt', 'a+', encoding="utf-8")
    for comment in sub.comments.list():
        loging.write(str(20 * "-"))
        loging.write(str('\n'))
        # loging.write('ID: '+str(comment.id)+'\n')
        # loging.write('Parent ID: '+ str(comment.parent())+'\n')
        loging.write(str(comment.body)+'\n')
    loging.close()

# Main Test


def dataGather():
    analyise = gatherHotPage(25)
    for data in analyise:
        readComments(data)
def listOfData():
    listOfFilenames = []
    for filename in os.listdir():
        if filename.endswith('txt'):
            listOfFilenames.append(filename)
    return listOfFilenames


def wordCounter():
    # print(os.listdir())
    wordCount = {}
    dataFiles = listOfData()
    #print(dataFiles)
    for data in dataFiles:
        thread = open(data, 'r+', encoding="utf-8")
        for word in thread.read().split():
            word = word.lower()
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1

    return wordCount

def analysis(dataForAnalysis):
    wordCount = Counter(dataForAnalysis).most_common(n=None)
    storeData = open('results.xml', 'w+', encoding="utf-8")
    for item in wordCount:
        storeData.write(str(item))
        storeData.write('\n')

def dataCleanup():
    getList = listOfData()
    print(getList)
    for item in getList:
        os.remove(item)
        print(item+'.txt removed')

dataGather()
analysis(wordCounter())

dataCleanup()


# sortedWords = sorted(dataForAnalysis.keys())
# for key in sorted(dataForAnalysis.keys()):
#     print(key, " :: ", dataForAnalysis[key])
# print(sortedWords)

#print(len(dataForAnalysis))
