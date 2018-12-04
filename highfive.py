from ircbot import bot

@bot.hook()
def highfive_hook(bot, channel, sender, message):
    if message == "\o/":
        bot.message(channel, "\o/")
    elif message == "o/":
        bot.ctcp(channel, "ACTION")
    elif message == "\o":
        bot.message(channel, "o/")
    elif "👋" in message:
        bot.message(channel, "o/")

