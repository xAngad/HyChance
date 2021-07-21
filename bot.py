import os
import discord
import asyncio
from dotenv import load_dotenv
load_dotenv()

from utils import createEmbed

class HyChance(discord.Client, discord.Embed):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("~~~~~~~~~~")
        print(f"Bot logged in as: {self.user.name}")
        print("~~~~~~~~~~")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!duel "):
            # embedVar = discord.Embed(title="Title", description="Desc", color=discord.Color.gold())
            # embedVar.add_field(name="Field1", value="hi", inline=True)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            # await message.channel.send(embed=embedVar)
            players = message.content.split()
            p1, p2 = players[1], players[2]

            embed = createEmbed(p1, p2)

            # Embed with stats
            await message.channel.send(embed=embed)


client = HyChance()
client.run(os.getenv("TOKEN"))