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
aloy_desc = "Formerly an outcast, now a hunter of unparalleled skill. Ready to do the right thing at any time."
wanderer_desc = "A wayfaring figure whose identity is a mystery. He dresses like a mountain ascetic, but he certainly does not act the part."
l1 = ["Dehya", "Lisa", "Nahida", "Nilou"]
l2 = ["Cyno", "Wanderer", "Traveler"]
w1 = ["Freedom-Sworn", "Primordial Jade Cutter", "Sword of Descension"]
w2 = ["Apprentice's Notes", "Beginner's Protector", "Dragon's Bane", "Hunter's Bow", "Hunter's Path", "Lion's Roar", 
      "Sharpshooter's Oath", "Wolf's Gravestone", "Kagura's Verity", "Mouun's Moon", "Wavebreaker's Fin", 
      "Tulaytullah's Remembrance"]
w3 = ["Old Merc's Pal", "Seasoned Hunter's Bow", "Traveler's Handy Sword"]

@bot.event
async def on_ready():
    print("rice cooker is now running!")

@bot.command()
async def characters(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(chars.format(ndash)).text
    res = json.loads(r)
    if res['rarity'] == 5:
        if res['name'] == "Aloy":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=aloy_desc)
        elif res['name'] == "Wanderer":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=wanderer_desc)
        else:
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['description'])
    else:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['description'])

    chpimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=charpfp.format(chpimg))
    
    if res['name']=="Collei":
        embeded.add_field(name="Title", value="Sprout of Rebirth", inline=True)
    elif res['name']=="Traveler":
        embeded.add_field(name="Title", value="Outlander", inline=True)
    else:
        embeded.add_field(name="Title", value=res['title'], inline=True)

    embeded.add_field(name="Vision", value=res['vision'], inline=True)
    embeded.add_field(name="Weapon", value=res['weapon'], inline=True)
    
    if res['name'] in l2:
        embeded.add_field(name="Gender", value="Male", inline=True)
    elif res['name'] in l1:
        embeded.add_field(name="Gender", value="Female", inline=True)
    elif res['name']=="Traveler":
        embeded.add_field(name="Gender", value="Chosen by player", inline=True)
    else:
        embeded.add_field(name="Gender", value=res['gender'], inline=True)

    embeded.add_field(name="Nation", value=res['nation'], inline=True)

    if res['name']=="Chongyun":
        embeded.add_field(name="Affiliation", value="Tianheng Thaumaturges", inline=True)
    elif res['name']=="Xinyan":
        embeded.add_field(name="Affiliation", value="The Red Strings", inline=True)
    elif res['name']=="Shenhe":
        embeded.add_field(name="Affiliation", value="Cloud Retainer's Abode", inline=True)
    elif res['name']=="Yanfei":
        embeded.add_field(name="Affiliation", value="Yanfei Legal Consultancy", inline=True)
    else:
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

    if res['rarity'] == 5:
        embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['passiveDesc'])
    elif res['rarity'] == 4:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['passiveDesc'])
    elif res['rarity'] == 3:
        embeded = discord.Embed(title="{}    ★★★".format(res['name']), description=res['passiveDesc'])
    elif res['rarity'] == 2:
        embeded = discord.Embed(title="{}    ★★".format(res['name']), description=res['passiveDesc'])
    else:
        embeded = discord.Embed(title="{}    ★".format(res['name']), description=res['passiveDesc'])
    
    if res['name']in w2:
        weapons = res['name'].replace("'s ", "s_").lower()
    elif res['name'] == "Amos' Bow":
        weapons = res['name'].replace("s' ", "s_").lower()
    elif res['name'] in w3:
        weapons = res['name'].replace("'s", "s").replace(" ", "_").lower()
    else:
        weapons = res['name'].replace(" ", "_").lower()

    embeded.set_thumbnail(url=weapimg.format(weapons))
    embeded.add_field(name="Type", value=res['type'], inline=True)

    if res['name'] in w1:
        embeded.add_field(name="Base ATK", value=res['BaseAttack'], inline=True)
    else:
        embeded.add_field(name="Base ATK", value=res['baseAttack'], inline=True)


    embeded.add_field(name="Sub Stat", value=res['subStat'], inline=True)
    embeded.add_field(name="Passive ", value=res['passiveName'], inline=True)
    embeded.add_field(name="Location", value=res['location'], inline=True)
    embeded.add_field(name="Ascension Material", value=res['ascensionMaterial'], inline=True)
    await ctx.send(embed=embeded)
    
bot.run(TOKEN)