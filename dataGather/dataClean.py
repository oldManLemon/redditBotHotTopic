
import config
from dataGather.data import listOfData
from os import rename, listdir, rename, remove, path, mkdir

def dataCleanup(action, targetedSub, dataType):
    '''
    Args: [bool]action, [string]Target_Subreddit, [string]File ending
    Will remove or store all data generated in process of running this bot
    Returns: NONE
    '''
    getList = listOfData(dataType)
    for item in getList:    
        if action:
            remove(item)
            
            print('{}.{} removed'.format(item, dataType))
            #print(item+'.txt removed')
        else:
            if path.isdir('storage/'+targetedSub):
               rename(item, 'storage/'+targetedSub+'/'+item) 
            else:
                mkdir('storage/'+targetedSub)
                rename(item, 'storage/'+targetedSub+'/'+item)

