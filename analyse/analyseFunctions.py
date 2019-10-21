from os import rename, listdir, rename, remove, path, mkdir
from collections import Counter
from dataGather import data as dataBoi
from abandon import allHope

def wordCounter():
    '''
    wordCounter()
    returns: dict of words and their count
    '''
    wordCount = {}
    dataFiles = dataBoi.listOfData()
    
    for data in dataFiles:
        thread = open(data, 'r+', encoding="utf-8")
        for word in thread.read().split():
            word = word.lower()
            wordScannerCounter(wordScannerCounter(1))
            if word in allHope.badword:
                pass
            elif word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        thread.close()
    print(wordScannerCounter(0, 'call'))
    return wordCount

def analysis(dataForAnalysis,nameOfSubreddit):
    wordCount = Counter(dataForAnalysis).most_common(n=None)
    storeData = open(nameOfSubreddit+'_results.xml', 'w+', encoding="utf-8")
    extra = open('working.xml', 'w+', encoding="utf-8")
    extra.write(str(wordCount))
    for item in wordCount:
        storeData.write(str(item))
        storeData.write('\n')
    storeData.close()


def wordScannerCounter(count, call= None):
    '''
    doesn't work yet suppose to be a ticker 
    ''' 
    if call == 'call':
        return count
    newCount=+count
    return newCount
   
