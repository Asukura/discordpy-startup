import discord
import datetime
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content:
        dt_now = datetime.datetime.now()
        with open("rollcall/rollcall_data.txt","a",encoding="utf_8") as file:
            file.write(str(dt_now.year + " ") + str(dt_now.month+ " ") + str(dt_now.day+ " ") + message.author.name + "\n")


client.run(TOKEN)
