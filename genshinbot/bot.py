import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.environ.get("DISCORD_BOT")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
chars = "https://genshin.jmp.blue/characters/{}"
weps = "https://genshin.jmp.blue/weapons/{}"
charpfp = "https://paimon.moe/images/characters/{}.png"
weapimg = "https://paimon.moe/images/weapons/{}.png"

@bot.event
async def on_ready():
    print("rice cooker is now running!")

@bot.command()
async def characters(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(chars.format(ndash)).text
    res = json.loads(r)
    if res['rarity'] == 5:
        embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['description'])
    else:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['description'])
    chpimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=charpfp.format(chpimg))
    
    embeded.add_field(name="Title", value=res['title'], inline=True)
    embeded.add_field(name="Vision", value=res['vision'], inline=True)
    embeded.add_field(name="Weapon", value=res['weapon'], inline=True)
    embeded.add_field(name="Gender", value=res['gender'], inline=True)
    embeded.add_field(name="Nation", value=res['nation'], inline=True)
    embeded.add_field(name="Affiliation", value=res['affiliation'], inline=True)
    embeded.add_field(name="Release", value=res['release'], inline=True)
    embeded.add_field(name="Constellation", value=res['constellation'], inline=True)
    embeded.add_field(name="Birthday", value=res['birthday'].replace("0000-", ""), inline=True)
    await ctx.send(embed=embeded)

@bot.command()
async def weapons(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/weapons/{}".format(arg)).text
    res = json.loads(r)
    embeded = discord.Embed(title=res['name'], description=res['passiveDesc'])
    #if res['rarity'] == 5:
        
    #elif res['rarity'] == 4:

    #elif res['rarity'] == 3:

    #else:

    

    
    weapons = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=weapimg.format(weapons))
    embeded.add_field(name="Type", value=res['type'], inline=True)
    #embeded.add_field(name="Rarity", value=res['rarity'], inline=True)
    embeded.add_field(name="Base ATK", value=res['baseAttack'], inline=True)
    embeded.add_field(name="Sub Stat", value=res['subStat'], inline=True)
    embeded.add_field(name="Passive ", value=res['passiveName'], inline=True)
    embeded.add_field(name="Location", value=res['location'], inline=True)
    embeded.add_field(name="Ascension Material", value=res['ascensionMaterial'], inline=True)
    await ctx.send(embed=embeded)
    
bot.run(TOKEN)