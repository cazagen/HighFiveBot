from ircbot import bot

@bot.hook()
def highfive_hook(bot, channel, sender, message):
    print("test")
    if message == "\o/":
        bot.message(channel, "\o/")
    elif message == "o/":
        bot.message(channel, "\o")
    elif message == "\o":
        bot.message(channel, "o/")