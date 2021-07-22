import os
import discord
from dotenv import load_dotenv
load_dotenv()

from scripts.utils import createEmbed, createErrorEmbed

client = discord.Client()
aliases = ["!duel", "!d", "!1v1"]

@client.event
async def on_ready():
    print(f"Bot logged in as: {client.user}")
    print("Running...")

    await client.change_presence(status=discord.Status.online, activity=discord.Game("!duel"))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    words = message.content.split()
    if words[0] in aliases:
        if len(words) == 3:
            p1, p2 = words[1], words[2]

            embedStats = createEmbed(p1, p2)
            await message.channel.send(embed=embedStats)

        else:
            embedError = createErrorEmbed()
            await message.channel.send(embed=embedError)

client.run(os.environ["TOKEN"])