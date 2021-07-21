import discord


def swXPtoLVL(xp):
    xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    if xp >= 15000:
        return (xp - 15000)/10000 + 12
    else:
        for i in range(len(xps)):
            if xp < xps[i]:
                return i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])

def createEmbed(p1, p2):
    # Initialization
    embed = discord.Embed(
        # title="1v1",
        # description=f"1v1 between {p1} and {p2}",
        # url="https://25karma.xyz/",
        type="rich",
        color=discord.Color.gold()
    )
    # Author (comment out most probably)
    embed.set_author(
        name="HyChance - 1v1 Win Predictor",
        # url="https://github.com/xAngad",
        icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg"
    )

    # Thumbnail
    embed.set_thumbnail(
        url="https://cdn.freebiesupply.com/logos/large/2x/minecraft-1-logo-png-transparent.png"
    )

    # Stats fields
    embed.add_field(
        name="1v1 Winner",
        value=p1,
        inline=False
    )
    embed.add_field(
        name="SW K/D",
        value="SkyWars K/D comparison",
        inline=False
    )
    embed.add_field(
        name=f"{p1}",
        value="R",
        inline=True
    )
    embed.add_field(
        name=f"{p2}",
        value="G",
        inline=True
    )

    # Footer w contact me
    embed.set_footer(
        text="See any bugs? DM me: angad#4229"
    )

    return embed