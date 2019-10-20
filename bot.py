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

sub = reddit.subreddit('testingground4bots')
# for submission in reddit.subreddit('testingground4bots').hot(limit=10):
#     print(submission)
postID =[]
for submission in sub.hot(limit=25):

   postID.append(submission.id)


#print(postID) #Suc
for id in postID:
   sub = reddit.submission(id=id)
   for top_level_comment in sub.comments:
    print(top_level_comment.body)

   
