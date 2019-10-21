
from dataGather import data
from analyse import analyseFunctions
import config

data.dataGather(5)
analyseFunctions.analysis(analyseFunctions.wordCounter(), config.targetSub)
data.dataCleanup(config.cleanUp, config.targetSub)
