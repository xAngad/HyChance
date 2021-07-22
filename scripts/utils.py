import discord
import numpy as np
from mojang import MojangAPI

def toPercentage(victories, defeats):
    return (victories / (victories + defeats))

def winner(p1, p2):
    probability_p1 = (p1*(1-p2)) / (p1*(1-p2) + p2*(1-p1))
    probability_p2 = 1 - probability_p1

    return [probability_p1, probability_p2]

def playerStats(p):
    from scripts.stats import Player
    player = Player(p)
    player_preds = player.predict()

    return player_preds

def createEmbed(p1, p2):
    UUIDs = [MojangAPI.get_uuid(p1), MojangAPI.get_uuid(p2)]
    IGNs = [MojangAPI.get_username(UUID) for UUID in UUIDs]
    # players = [p1, p2]


    # Create player predictions
    p1_probs = playerStats(p1)
    p2_probs = playerStats(p2)

    sw_probs = winner(p1_probs["sw"], p2_probs["sw"])
    bw_probs = winner(p1_probs["bw"], p2_probs["bw"])
    duels_probs = winner(p1_probs["duels"], p2_probs["duels"])

    sw_winner = IGNs[np.argmax(sw_probs)]
    bw_winner = IGNs[np.argmax(bw_probs)]
    duels_winner = IGNs[np.argmax(duels_probs)]

    # Initialization
    embed = discord.Embed(type="rich", color=discord.Color.gold())

    # Author (comment out most probably)
    embed.set_author(name="HyChance - 1v1 Win Predictor",
                     icon_url="https://crafatar.com/avatars/6327b3fb426b4b6a92fba78e13173a22?size=400")

    # Thumbnail
    embed.set_thumbnail(url="https://assets.change.org/photos/8/bv/gd/yuBVGDPtWevQvmQ-800x450-noPad.jpg?1571761596")

    # Stats fields
    embed.add_field(
        name="SkyWars",
        value=f"`{sw_winner}` (`{round(max(sw_probs)*100, 2)}% chance`)",
        inline=False
    )
    embed.add_field(
        name="Bedwars",
        value=f"`{bw_winner}` (`{round(max(bw_probs)*100, 2)}% chance`)",
        inline=False
    )
    embed.add_field(
        name="Duels",
        value=f"`{duels_winner}` (`{round(max(duels_probs)*100, 2)}% chance`)",
        inline=False
    )

    # Footer w contact me
    embed.set_footer(text="See any bugs? DM me: xAngad#4229" )


    return embed

def createErrorEmbed():
    embed = discord.Embed(type="rich", color=discord.Color.red())

    embed.set_author(name="HyChance - 1v1 Win Predictor",
                     icon_url="https://crafatar.com/avatars/6327b3fb426b4b6a92fba78e13173a22?size=400")

    embed.set_thumbnail(url="https://www.freeiconspng.com/uploads/error-icon-4.png")

    embed.add_field(
        name="Error",
        value="Please use format: `!duel <Player #1> <Player #2>`",
        inline=False
    )

    embed.set_footer(text="See any bugs? DM me: xAngad#4229")

    return embed


# def swXPtoLVL(xp):
#     xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
#     if xp >= 15000:
#         return (xp - 15000)/10000 + 12
#     else:
#         for i in range(len(xps)):
#             if xp < xps[i]:
#                 return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])