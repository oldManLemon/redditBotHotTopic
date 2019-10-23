
import config
from dataGather.data import listOfData
from os import rename, listdir, rename, remove, path, mkdir

def dataCleanup(action, targetedSub, dataType):
    getList = listOfData(dataType)
    for item in getList:    
        if action:
            remove(item)
            print('{}.{} removed'.format(targetedSub, dataType))
            #print(item+'.txt removed')
        else:
            if path.isdir('storage/'+targetedSub):
               rename(item, 'storage/'+targetedSub+'/'+item) 
            else:
                mkdir('storage/'+targetedSub)
                rename(item, 'storage/'+targetedSub+'/'+item)

