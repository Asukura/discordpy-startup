import discord
import datetime
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == "output csv":
        client.send_message(message.channel,LIST)

    else:
        dt_now = datetime.datetime.now()
        LIST.append(str(dt_now.year + " ") + str(dt_now.month+ " ") + str(dt_now.day+ " ") + message.author.name)


client.run(TOKEN)
