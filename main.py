from bot import Bot

bot = Bot()
web = bot.get_website()
bot.visit_website(web)
bot.search()
