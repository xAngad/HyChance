import os
import discord
from dotenv import load_dotenv
load_dotenv()

from scripts.utils import createEmbed, createErrorEmbed

class HyChance(discord.Client, discord.Embed):
    def __init__(self):
        super().__init__()
        self.aliases = ["!duel", "!d", "!1v1"]

    async def on_ready(self):
        print("~~~~~~~~~~")
        print(f"Bot logged in as: {self.user.name}")
        print("~~~~~~~~~~")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        words = message.content.split()
        if words[0] in self.aliases:
            if len(words) == 3:
                p1, p2 = words[1], words[2]

                embedStats = createEmbed(p1, p2)
                await message.channel.send(embed=embedStats)

            else:
                embedError = createErrorEmbed()
                await message.channel.send(embed=embedError)


client = HyChance()
client.run(os.environ["TOKEN"])