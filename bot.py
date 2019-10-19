# Reddit Bot First Run
import praw

#https://www.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='JL53WY5Cw2WK8g',
                     client_secret='fKqCZ44PIIFdqOjemTIKab0BfEs',
                     password='popularWordBot!',
                     user_agent='popularWordBot Script',
                     username='popularWordBot')


test = reddit.subreddit('testingground4bots')
for submission in reddit.subreddit('testingground4bots').hot(limit=10):
    print(submission)


