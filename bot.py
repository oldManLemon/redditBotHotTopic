# Reddit Bot First Run
import praw
import pprint

log = open("data.txt","w")

#https://www.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='JL53WY5Cw2WK8g',
                     client_secret='fKqCZ44PIIFdqOjemTIKab0BfEs',
                     password='popularWordBot!',
                     user_agent='popularWordBot Script',
                     username='popularWordBot')

sub = reddit.subreddit('politics')

# for submission in reddit.subreddit('testingground4bots').hot(limit=10):
#     print(submission)

postID =[]
def gatherHotPage(limit):
   for submission in sub.hot(limit=limit):

      postID.append(submission.id)

#gatherHotPage(25)
#print(postID) #Suc


#djf0n7
#loging = open('comments.txt', 'w+')     
#loging.write(str(fullList))
#loging.close()
loging = open('comments2.txt', 'w+',encoding="utf-8")         
sub = reddit.submission(id='dk962x')
sub.comments.replace_more(limit=None)
for comment in sub.comments.list():
     
     #fullList.append(comment.body)
    # print(20 * "-")
     loging.write(str(20 * "-"))
     loging.write(str('\n'))
    # print('ID: ',comment.id)
     loging.write('ID: '+str(comment.id)+'\n')
     #print('Parent ID: ', comment.parent())
     loging.write('Parent ID: '+ str(comment.parent())+'\n')
     #print(comment.body)
     loging.write(str(comment.body)+'\n')

   #   if len(comment.replies) > 0:
   #      for reply in comment.replies:
   #          print('Reply: ',reply.body)

#loging = open('comments.txt', 'w+')     
#loging.write(str(fullList))
#loging.close()    

# for id in postID:
#    sub = reddit.submission(id=id)
#    for top_level_comment in sub.comments:
#     print(top_level_comment.body)

   
