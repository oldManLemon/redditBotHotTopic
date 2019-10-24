#from dataGather.data import reddit
# Reddit Bot First Run
import praw
import config
import password
from dataGather.data import reddit

sub = reddit.subreddit('testingground4bots')


title = 'This is a test'
url = "As always I need more Karma"
try:
    reddit.subreddit(sub).submit(title, selftext=url)
        
except:

    print('This has Failed, most likely due to rate limit') 
    


