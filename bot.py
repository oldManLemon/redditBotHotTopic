# Reddit Bot First Run
import praw
# Inbuilts
from os import rename, listdir, rename, remove, path, mkdir
from collections import Counter


# just import the password
import password
import config
from abandon import allHope


# https://www.reddit.com/prefs/apps

reddit = praw.Reddit(client_id=config.clientID,
                     client_secret=config.clientSecret,
                     # password='popularWordBot!',
                     password=password.password,
                     user_agent=config.agent,
                     username=config.username)

try:
    print(reddit.user.me())
except:
    print('login in issues')
   

sub = reddit.subreddit(config.targetSub)



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
        loging.write(str(comment.body)+'\n')
    loging.close()

def dataGather(limit):
    analyise = gatherHotPage(limit)
    for data in analyise:
        readComments(data)

def listOfData():
    '''
    listOfData()
    returns: array of all txt's in folder
    '''
    listOfFilenames = []
    for filename in listdir():
        if filename.endswith('txt'):
            listOfFilenames.append(filename)
    return listOfFilenames


def wordCounter():
    '''
    wordCounter()
    returns: dict of words and their count
    '''
    wordCount = {}
    dataFiles = listOfData()
    
    for data in dataFiles:
        count = 0
        
        
        thread = open(data, 'r+', encoding="utf-8")
        for word in thread.read().split():
            word = word.lower()
            if word in allHope.badword:
                pass
            elif word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        thread.close()
    print('words scanned: '+ str(count))
    return wordCount

def analysis(dataForAnalysis):
    wordCount = Counter(dataForAnalysis).most_common(150)
    storeData = open(config.targetSub+'_results.xml', 'w+', encoding="utf-8")
    extra = open('working.xml', 'w+', encoding="utf-8")
    extra.write(str(wordCount))
    for item in wordCount:
        storeData.write(str(item))
        storeData.write('\n')
    storeData.close()

def dataCleanup(action):
    getList = listOfData()
    for item in getList:    
        if action:
            remove(item)
            print(item+'.txt removed')
        else:
            if path.isdir('storage/'+config.targetSub):
               rename(item, 'storage/'+config.targetSub+'/'+item) 
            else:
                mkdir('storage/'+config.targetSub)
                rename(item, 'storage/'+config.targetSub+'/'+item)
            
#print()
# dataGather(config.limit)
# analysis(wordCounter())
# dataCleanup(config.cleanUp)



# sortedWords = sorted(dataForAnalysis.keys())
# for key in sorted(dataForAnalysis.keys()):
#     print(key, " :: ", dataForAnalysis[key])
# print(sortedWords)

#print(len(dataForAnalysis))
