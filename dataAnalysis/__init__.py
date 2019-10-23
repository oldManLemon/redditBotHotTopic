from dataAnalysis.datanalyseFunctions import analysis, wordCounter

def runDataAnalysis(targetRedditSub):
    if not type(targetRedditSub) == str:
        raise TypeError('Target sub must be a string')
    analysis(wordCounter(),targetRedditSub )





