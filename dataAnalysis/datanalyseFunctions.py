from os import rename, listdir, rename, remove, path, mkdir
from collections import Counter
from dataGather import data as dataBoi
from abandon import allHope
#totalWordCounter = 0

def wordScannerCounter(count):
    '''
    Ticker to count numeber of words analyised
    ''' 
    
    newCount=+count
    return newCount
   
def wordCounter():
    '''
    wordCounter()
    returns: dict of words and their count
    '''
    wordCount = {}
    dataFiles = dataBoi.listOfData('txt')
    
    for data in dataFiles:
        thread = open(data, 'r+', encoding="utf-8")
        for word in thread.read().split():
            word = word.lower()
            #totalWordCounter += 1
            if word in allHope.badword:
                pass
            elif not word.isalnum():
                #print(word)
                word = ''.join(e for e in word if e.isalnum())
            elif word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        thread.close()
    #print('Amount of words processed {}'.format(totalWordCounter))
    return wordCount

def analysis(dataForAnalysis,nameOfSubreddit):
    wordCount = Counter(dataForAnalysis).most_common(n=None)
    storeData = open(nameOfSubreddit+'_results.xml', 'w+', encoding="utf-8")
    extra = open('working.xml', 'w+', encoding="utf-8")
    extra.write(str(wordCount))
    for item in wordCount:

        storeData.write(str(item[0])+','+str(item[1]))
       
        storeData.write('\n')
    storeData.close()


