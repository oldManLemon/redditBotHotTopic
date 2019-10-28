#from dataGather.data import reddit
# Reddit Bot First Run
import praw
import config
import password
import time
from dataGather.data import reddit


def postToReddit(targetSub, data, topWordLimit=25):
    #sub = reddit.subreddit('testingground4bots')
    tableGen = []
    top = data[0]
    top = top.capitalize()
    
    for rank, item in enumerate(data):

        
        table = "| {} | {} |\n".format(rank, item)
        tableGen.append(table)


    
    


    title = '{} was last months top word from r/{}'.format(top,targetSub)
    body = ("""
Here are the top {} words from r/{}\n\n


| Rank | Word |
|------|------|
""").format(topWordLimit, targetSub)
    for line in tableGen:
        body += line
    body += '''

I am a bot, possibly a poorly programmed one. 
I am in beta and I will continue to wittle down important words and even phrases to see more interesting patterns. 
If you have any suggestions/complaints/issues please PM me

    '''
    hasPosted = False    
    while hasPosted == False:
        
        try:
            reddit.subreddit('testingground4bots').submit(title, selftext=body)
            # f=open('table.txt', 'a+', encoding='utf8')
            # f.write(title)
            # f.write(body)
            # f.close()
            print('Success')
            hasPosted= True

        except:
        
            print('This has Failed, most likely due to rate limit')
            time.sleep(120)
            print('Trying again ...')
            hasPosted=  False




