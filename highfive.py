from ircbot import bot

@bot.hook
def message_hook(bot, channel, sender, message):
    if "\o/" in message:
        bot.message(channel, "\o/")
    elif "o/" in message:
        bot.message(channel, "\o")
    elif "\o" in message:
        bot.message(channel, "o/")