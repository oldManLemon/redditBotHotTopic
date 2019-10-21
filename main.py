
import bot
import config

bot.dataGather(config.limit)
bot.analysis(bot.wordCounter())
bot.dataCleanup(config.cleanUp)

