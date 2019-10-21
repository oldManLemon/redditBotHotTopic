# Reddit Bot First Run
import praw
import os
import password



# https://www.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='JL53WY5Cw2WK8g',
                     client_secret='fKqCZ44PIIFdqOjemTIKab0BfEs',
                     #password='popularWordBot!',
                     password=password.password,
                     user_agent='popularWordBot Script',
                     username='popularWordBot')

sub = reddit.subreddit('testingground4bots')


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


dataGather()

def wordCounter():
    # print(os.listdir())
   wordCount = {}
   
   for filename in os.listdir():
      print(filename)
      if filename.endswith('txt'):
         thread = open(filename, 'r+', encoding="utf-8")
         for word in thread.read().split():
            word =  word.lower()
            if word not in wordCount:
               
               wordCount[word] = 1
            else:
               
               wordCount[word] +=1

   return wordCount
         



print(wordCounter())

# loging = open('comments2.txt', 'w+',encoding="utf-8")
# sub = reddit.submission(id='dk962x')
# sub.comments.replace_more(limit=None)
# for comment in sub.comments.list():

#      #fullList.append(comment.body)
#     # print(20 * "-")
#      loging.write(str(20 * "-"))
#      loging.write(str('\n'))
#     # print('ID: ',comment.id)
#      loging.write('ID: '+str(comment.id)+'\n')
#      #print('Parent ID: ', comment.parent())
#      loging.write('Parent ID: '+ str(comment.parent())+'\n')
#      #print(comment.body)
#      loging.write(str(comment.body)+'\n')
