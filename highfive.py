from ircbot import bot

@bot.hook()
def highfive_hook(bot, channel, sender, message):
    if "\o/" in message:
        bot.message(channel, "\o/")
    elif "o/" in message:
        bot.ctcp(channel, "ACTION", "")
    elif "\o" in message:
        bot.message(channel, "o/")
    elif "👋" in message:
        bot.message(channel, "o/")

