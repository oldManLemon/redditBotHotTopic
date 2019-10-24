#from dataGather.data import reddit
import praw
import config
import password

reddit = praw.Reddit(client_id=config.clientID,
                     client_secret=config.clientSecret,
                     # password='popularWordBot!',
                     password=password.password,
                     user_agent=config.agent,
                     username=config.username)


sub = reddit.subreddit(targetSub)

