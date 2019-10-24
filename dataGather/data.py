# Reddit Bot First Run
import praw

# Inbuilts
from os import listdir



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
   if reddit.user.me() == 'popularWordBot':
       print('Login Successful')
except:
    print('Login Unsuccesful')
   





def gatherHotPage(limit, targetSub):
    '''
    Args: Limit: number, targetSub: str
    limit is the amount of posts to scan
    Returns array of reddit PostID's
    '''
    sub = reddit.subreddit(targetSub)
    postID = []
    for submission in sub.hot(limit=limit):
        loging = open(submission.id+'.txt', 'w+', encoding="utf-8")
        loging.write(str(submission.title)+'\n')
        loging.close()
        postID.append(submission.id)

    return postID


def readComments(submissionID):
    '''
    Returns nothing.
    Write all comments from Reddit post based on postID.
    Creates a txt file with postID name
    Prints comments all comments in there

    '''

    sub = reddit.submission(id=submissionID)
    sub.comments.replace_more(limit=None)
    # encoding needed to deal with emojis
    loging = open(submissionID+'.txt', 'a+', encoding="utf-8")
    for comment in sub.comments.list():
        loging.write(str(20 * "-"))
        loging.write(str('\n'))
        loging.write(str(comment.body)+'\n')
    loging.close()


def gatherRedditThreadsAndComments(limit, targetSub):
    '''
    Combines two functions together\n
    RETURNS: None, will create a LIMIT of txt files with comments\n
    gatherHotPage(limit): returns Array of PostID's\n
    readComments(postID): creates postID.txt with all comments of postID\n
    CALL THIS FUNCTION IN MAIN!
    '''
    analyse = gatherHotPage(limit, targetSub)
    for data in analyse:
        readComments(data)


def listOfData(endingType):
    '''
    listOfData()
    returns: array of all txt's in folder
    '''
    listOfFilenames = []
    for filename in listdir():
        if filename.endswith(endingType):
            listOfFilenames.append(filename)
    return listOfFilenames




         
