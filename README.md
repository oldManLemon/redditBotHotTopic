
# Reddit Bot Hot Topic

A reddit bot that scans specified subs and ranking the most popular words. It will store the data in a database and post at the end of the month.

  
  

# Installation

## Requirements

You will need to install [python3](https://www.python.org/downloads/), and [MySQL](https://www.mysql.com/) database. I would of course recommend using a virtuenv for this. From there you will need to run `$ pip install -r requirements.txt`.  

## Installation steps

To gather data, create a directory called storage inside of redditbot. 
Please check the config.py file and [the reddit api page]( https://github.com/reddit-archive/reddit/wiki/OAuth2) to understand the config page first section, this is how we connect to reddits api. 

Underneath there will be an array of target subs. You can have one or as many as you want. 
Eg: `targetSub = ['testabot','australia']`
This will scan through both those subs

Limit is the limit of top hot posts to be scanned, default is 25
Eg `limit =  25`

Clean up will either keep or remove the files with the posts and comments text. Your reasoning for keeping these files may vary.

Eg: `cleanUp =  True  # True deletes file False will Store them in a folder`
 ### Manual Steps

 1. In the main directory, please create a folder called storage.
    
 2. In the main directory create a file called `password.py`
 3. Inside add the following items 

   ` password = 'a-password'`
    
    sqlPassword = 'a-password'

The password being for your reddit account and sqlPassword being for your sql user. 

Finally in folder `sql/sql.py` you will find the following code:

    conn = pymysql.connect(
    
    db='myWordCollectionDatabase',
    
    user='iAmUser',
    
    passwd= sqlPassword,
    
    host='localhost')
    
    c = conn.cursor()
 This is where you will need to change the database settings. I will move this in future updates.  For more information please check the documentation [here](https://pymysql.readthedocs.io/en/latest/user/examples.html)

# Usage
The bot accepts two command line arguments. `gather` and `post` these must be included or the script through an error telling you need an arg.  ie: `$python main.py gather`
## Gather
The gather command will scan your selected subreddits for the top posts. It will then scan all the words and add them to their respective sub databases. Note it will not rescan posts it has already checked. If you wish it to rescan a post it has already scanned go to `storage/subIDList` and you can remove the id string. 

The id can be found in the post link `https://www.reddit.com/r/amazon/comments/`**dnzhwz**`/is_amazon_prime_having_issues_completing_orders/` 
Completed looks like https://www.reddit.com/r/amazon/comments/dnzhwz/is_amazon_prime_having_issues_completing_orders/

## Post
Post will take all the data that has being collected and post it to their respective subreddits. Please note that it will fail regularly if you do not have enough karma. You will need karma to post more than once every 10 minutes. The script will keep trying every two minutes. It will eventually get through the list. Currently the limit is set to 25. In the main.py page you will see `p.postToReddit(item,postdata)` you may include a different word rank limit if you wish `p.postToReddit(item,postdata,60)` will return the top 60 words

# License 
Standard MIT

# Tests
Coming, maybereddit bot licence



