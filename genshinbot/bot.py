import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
import bulk

load_dotenv()
TOKEN = os.environ.get("DISCORD_BOT")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

chars = "https://genshin.jmp.blue/characters/{}"
weps = "https://genshin.jmp.blue/weapons/{}"
charpfp = "https://paimon.moe/images/characters/{}.png"
weapimg = "https://paimon.moe/images/weapons/{}.png"
artiimg = "https://paimon.moe/images/artifacts/{}_flower.png"
circlet = "https://paimon.moe/images/artifacts/{}_circlet.png"

ina = "https://static.wikia.nocookie.net/gensin-impact/images/9/9e/Emblem_Inazuma.png/revision/latest?cb=20230127155005"
ina_big = "https://static.wikia.nocookie.net/gensin-impact/images/4/43/Inazuma_City.png/revision/latest?cb=20220629030636"
liy = "https://genshin.honeyhunterworld.com/img/acat_5.webp"
liy_big = "https://static.wikia.nocookie.net/gensin-impact/images/0/0c/Liyue_Harbor.png/revision/latest?cb=20220612170326"
mon = "https://genshin.honeyhunterworld.com/img/acat_4.webp?x25384"
mon_big = "https://static.wikia.nocookie.net/gensin-impact/images/d/d6/Mondstadt_City.png/revision/latest?cb=20230810074558"
sum = "https://www.hoyobuilds.com/img/gi/icon/Emblem_Sumeru_transparent.webp"
sum_big = "https://static.wikia.nocookie.net/gensin-impact/images/1/11/Sumeru.png/revision/latest?cb=20221123012821"

ane = "https://static.wikia.nocookie.net/gensin-impact/images/1/10/Element_Anemo.svg/revision/latest/scale-to-width-down/100?cb=20220119211128"
cry = "https://static.wikia.nocookie.net/gensin-impact/images/7/72/Element_Cryo.svg/revision/latest/scale-to-width-down/100?cb=20220119211508"
den = "https://static.wikia.nocookie.net/gensin-impact/images/7/73/Element_Dendro.svg/revision/latest/scale-to-width-down/100?cb=20220119211226"
ele = "https://static.wikia.nocookie.net/gensin-impact/images/f/ff/Element_Electro.svg/revision/latest/scale-to-width-down/100?cb=20220119211156"
geo = "https://static.wikia.nocookie.net/gensin-impact/images/9/9b/Element_Geo.svg/revision/latest/scale-to-width-down/100?cb=20220119211105"
hyd = "https://static.wikia.nocookie.net/gensin-impact/images/8/80/Element_Hydro.svg/revision/latest/scale-to-width-down/100?cb=20220119211435"
pyr = "https://static.wikia.nocookie.net/gensin-impact/images/2/2c/Element_Pyro.svg/revision/latest/scale-to-width-down/100?cb=20220119211527"

l1 = ["Dehya", "Lisa", "Nahida", "Nilou"]
l2 = ["Cyno", "Wanderer", "Traveler"]

s1 = ["Kamisato Ayato", "Dehya", "Freminet", "Kirara", "Layla", "Lynette", "Lyney", "Nahida", "Nilou", "Raiden Shogun", "Sayu", "Wanderer", "Yaoyao", "Zhongli"]

w1 = ["Freedom-Sworn", "Primordial Jade Cutter", "Sword of Descension"]
w2 = ["Apprentice's Notes", "Beginner's Protector", "Dragon's Bane", "Hunter's Bow", "Hunter's Path", "Lion's Roar", 
      "Sharpshooter's Oath", "Wolf's Gravestone", "Kagura's Verity", "Mouun's Moon", "Wavebreaker's Fin", 
      "Tulaytullah's Remembrance"]
w3 = ["Old Merc's Pal", "Seasoned Hunter's Bow", "Traveler's Handy Sword"]

a1 = ["Defender's Will", "Gladiator's Finale", "Nymph's Dream", "Shimenawa's Reminiscence", "Vourukasha's Glow", 
      "Wanderer's Troupe"]
a2 = ["Prayers for Destiny", "Prayers for Illumination", "Prayers for Wisdom", "Prayers to Springtime", 
      "Sacrifieur to the Firmament"]

@bot.event
async def on_ready():
    print("rice cooker is now running!")

@bot.command()
async def characters(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(chars.format(ndash)).text
    res = json.loads(r)
    clr = 0x000000

    if res['vision'] == "Pyro":
        clr = 0xea7838
    elif res['vision'] == "Cryo":
        clr = 0xa4d6e3
    elif res['vision'] == "Hydro":
        clr = 0x5fc1f1
    elif res['vision'] == "Electro":
        clr = 0xb38dc1
    elif res['vision'] == "Geo":
        clr = 0xf2b723
    elif res['vision'] == "Dendro":
        clr = 0x9cc928
    else:
        clr = 0x71c2a7


    if res['rarity'] == 5:
        if res['name'] == "Aloy":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.aloy_desc, color=clr)
        elif res['name'] == "Wanderer":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.wanderer_desc, color=clr)
        else:
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['description'], color=clr)
    else:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['description'], color=clr)

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
async def skills(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(chars.format(ndash)).text
    res = json.loads(r)

    clr = 0x000000

    if res['vision'] == "Pyro":
        clr = 0xea7838
    elif res['vision'] == "Cryo":
        clr = 0xa4d6e3
    elif res['vision'] == "Hydro":
        clr = 0x5fc1f1
    elif res['vision'] == "Electro":
        clr = 0xb38dc1
    elif res['vision'] == "Geo":
        clr = 0xf2b723
    elif res['vision'] == "Dendro":
        clr = 0x9cc928
    else:
        clr = 0x71c2a7

    if res['rarity'] == 5:
        if res['name'] == "Aloy":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.aloy_desc, color=clr)
        elif res['name'] == "Wanderer":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.wanderer_desc, color=clr)
        else:
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['description'], color=clr)
    else:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['description'], color=clr)
    
    chpimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=charpfp.format(chpimg))

    if res['name'] in s1:
        for st in res['skillTalents']:
            if st['unlock'] == "Normal Attack":
                if res['name'] == "Lyney":
                    embeded.add_field(name="Card Force Translocation: Normal Attack (I)", value=bulk.lyney_atk_1, inline=False)
                    embeded.add_field(name="Card Force Translocation: Normal Attack (II)", value=bulk.lyney_atk_2, inline=False)
                    embeded.add_field(name="Card Force Translocation: Normal Attack (III)", value=bulk.lyney_atk_3, inline=False)
                else:
                    embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=st['description'].replace("\n\n", "\n"), inline=False)
            elif st['unlock'] == "Elemental Skill":
                if res['name'] == "Kamisato Ayato":
                    embeded.add_field(name="Kamisato Art: Kyouka : Elemental SKill (I)", value=bulk.ayato_skill_1, inline=False)
                    embeded.add_field(name="Kamisato Art: Kyouka : Elemental SKill (II)", value=bulk.ayato_skill_2, inline=False)
                elif res['name'] == "Dehya":
                    embeded.add_field(name="Molten Inferno: Elemental Skill (II)", value=bulk.dehya_skill_1, inline=False)
                    embeded.add_field(name="Molten Inferno: Elemental Skill (II)", value=bulk.dehya_skill_2, inline=False)
                    embeded.add_field(name="Molten Inferno: Elemental Skill (III)", value=bulk.dehya_skill_3, inline=False)
                    embeded.add_field(name="Molten Inferno: Elemental Skill (IV)", value=bulk.dehya_skill_4, inline=False)
                elif res['name'] == "Freminet":
                    embeded.add_field(name="Pressurized Flow: Elemental Skill (I)", value=bulk.freminet_skill_1, inline=False)
                    embeded.add_field(name="Pressurized Flow: Elemental Skill (II)", value=bulk.freminet_skill_2, inline=False)
                    embeded.add_field(name="Pressurized Flow: Elemental Skill (III)", value=bulk.freminet_skill_3, inline=False)
                elif res['name'] == "Kirara":
                    embeded.add_field(name="Meow-teor Kick: Elemental Skill (I)", value=bulk.kirara_skill_1, inline=False)
                    embeded.add_field(name="Meow-teor Kick: Elemental Skill (II)", value=bulk.kirara_skill_2, inline=False)
                    embeded.add_field(name="Meow-teor Kick: Elemental Skill (III)", value=bulk.kirara_skill_3, inline=False)
                elif res['name'] == "Layla":
                    embeded.add_field(name="Nights of Formal Focus: Elemental Skill (I)", value=bulk.layla_skill_1, inline=False)
                    embeded.add_field(name="Nights of Formal Focus: Elemental Skill (II)", value=bulk.layla_skill_2, inline=False)
                elif res['name'] == "Lynette":
                    embeded.add_field(name="Enigmatic Feint: Elemental Skill (I)", value=bulk.lynette_skill_1, inline=False)
                    embeded.add_field(name="Enigmatic Feint: Elemental Skill (II)", value=bulk.lynette_skill_2, inline=False)
                    embeded.add_field(name="Enigmatic Feint: Elemental Skill (III)", value=bulk.lynette_skill_3, inline=False)
                    embeded.add_field(name="Enigmatic Feint: Elemental Skill (IV)", value=bulk.lynette_skill_4, inline=False)
                elif res['name'] == "Nahida":
                    embeded.add_field(name="All Schemes to Know: Elemental Skill (I)", value=bulk.nahida_skill_1, inline=False)
                    embeded.add_field(name="All Schemes to Know: Elemental Skill (II)", value=bulk.nahida_skill_2, inline=False)
                    embeded.add_field(name="All Schemes to Know: Elemental Skill (III)", value=bulk.nahida_skill_3, inline=False)
                elif res['name'] == "Nilou":
                    embeded.add_field(name="Dance of Haftkarsvar: Elemental Skill (I)", value=bulk.nilou_skill_1, inline=False)
                    embeded.add_field(name="Dance of Haftkarsvar: Elemental Skill (II)", value=bulk.nilou_skill_2, inline=False)
                elif res['name'] == "Sayu":
                    embeded.add_field(name="Yoohoo Art: Fuuin Dash: Elemental Skill (I)", value=bulk.sayu_skill_1, inline=False)
                    embeded.add_field(name="Yoohoo Art: Fuuin Dash: Elemental Skill (II)", value=bulk.sayu_skill_2, inline=False)
                    embeded.add_field(name="Yoohoo Art: Fuuin Dash: Elemental Skill (III)", value=bulk.sayu_skill_3, inline=False)
                elif res['name'] == "Wanderer":
                    embeded.add_field(name="Hanega: Song of the Wind: Elemental Skill (I)", value=bulk.wanderer_skill_1, inline=False)
                    embeded.add_field(name="Hanega: Song of the Wind: Elemental Skill (II)", value=bulk.wanderer_skill_2, inline=False)
                    embeded.add_field(name="Hanega: Song of the Wind: Elemental Skill (III)", value=bulk.wanderer_skill_3, inline=False)
                elif res['name'] == "Yaoyao":
                    embeded.add_field(name="Raphanus Sky Cluster: Elemental Skill (I)", value=bulk.yaoyao_skill_1, inline=False)
                    embeded.add_field(name="Raphanus Sky Cluster: Elemental Skill (II)", value=bulk.yaoyao_skill_2, inline=False)
                    embeded.add_field(name="Raphanus Sky Cluster: Elemental Skill (III)", value=bulk.yaoyao_skill_3, inline=False)
                elif res['name'] == "Zhongli":
                    embeded.add_field(name="Dominus Lapidus: Elemental Skill (I)", value=bulk.zhongli_skill_1, inline=False)
                    embeded.add_field(name="Dominus Lapidus: Elemental Skill (II)", value=bulk.zhongli_skill_2, inline=False)
                    embeded.add_field(name="Dominus Lapidus: Elemental Skill (III)", value=bulk.zhongli_skill_3, inline=False)
                    embeded.add_field(name="Dominus Lapidus: Elemental Skill (IV)", value=bulk.zhongli_skill_4, inline=False)
                else:
                    embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=st['description'].replace("\n\n", "\n"), inline=False)
            else:
                if res['name'] == "Dehya":
                    embeded.add_field(name="Leonine Bite: Elemental Burst", value=bulk.dehya_burst_1, inline=False)
                    embeded.add_field(name="Leonine Bite: Elemental Burst (II)", value=bulk.dehya_burst_2, inline=False)
                elif res['name'] == "Raiden Shogun":
                    embeded.add_field(name="Secret Art: Musou Shinsetsu: Elemental Skill (I)", value=bulk.raiden_burst_1, inline=False)
                    embeded.add_field(name="Secret Art: Musou Shinsetsu: Elemental Skill (II)", value=bulk.raiden_burst_2, inline=False)
                    embeded.add_field(name="Secret Art: Musou Shinsetsu: Elemental Skill (III)", value=bulk.raiden_burst_3, inline=False)
                else:
                    embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=st['description'].replace("\n\n", "\n"), inline=False)

    elif res['name'] == "Shenhe":
        for st in res['skillTalents']:
            if st['unlock'] == "Elemental skill":
                embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=bulk.shenhe_skill, inline=False)
            else:
                embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=st['description'].replace("\n\n", "\n"), inline=False)
    else:
        for st in res['skillTalents']:
            embeded.add_field(name="{} : {}".format(st['unlock'], st['name']), value=st['description'].replace("\n\n", "\n"), inline=False)
    
    if res['name'] == "Kuki Shinobu":
        for pt in res['passiveTalents']:
            if pt['unlock'] == "Unlocked Automatically":
                embeded.add_field(name="{} : {}".format(pt['unlock'], pt['name']), value=bulk.kuki_3rd_passive, inline=False)
            else:    
                embeded.add_field(name="{} : {}".format(pt['unlock'], pt['name']), value=pt['description'], inline=False)
    else:
        for pt in res['passiveTalents']:
            embeded.add_field(name="{} : {}".format(pt['unlock'], pt['name']), value=pt['description'], inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def cons(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(chars.format(arg)).text
    res = json.loads(r)

    clr = 0x000000

    if res['vision'] == "Pyro":
        clr = 0xea7838
    elif res['vision'] == "Cryo":
        clr = 0xa4d6e3
    elif res['vision'] == "Hydro":
        clr = 0x5fc1f1
    elif res['vision'] == "Electro":
        clr = 0xb38dc1
    elif res['vision'] == "Geo":
        clr = 0xf2b723
    elif res['vision'] == "Dendro":
        clr = 0x9cc928
    else:
        clr = 0x71c2a7

    if res['rarity'] == 5:
        if res['name'] == "Aloy":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.aloy_desc, color=clr)
        elif res['name'] == "Wanderer":
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=bulk.wanderer_desc, color=clr)
        else:
            embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['description'], color=clr)
    else:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['description'], color=clr)

    charimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=charpfp.format(charimg))

    for i in res['constellations']:
        embeded.add_field(name="{} : {}".format(i['unlock'], i['name']), value=i['description'], inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def weapons(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/weapons/{}".format(arg)).text
    res = json.loads(r)

    if res['rarity'] == 5:
        embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), description=res['passiveDesc'], color=0xd49548)
    elif res['rarity'] == 4:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), description=res['passiveDesc'], color=0x935c9d)
    elif res['rarity'] == 3:
        embeded = discord.Embed(title="{}    ★★★".format(res['name']), description=res['passiveDesc'], color=0x5d839a)
    elif res['rarity'] == 2:
        embeded = discord.Embed(title="{}    ★★".format(res['name']), description=res['passiveDesc'], color=0x5d8771)
    else:
        embeded = discord.Embed(title="{}    ★".format(res['name']), description=res['passiveDesc'], color=0x7f7d81)
    
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
    embeded.add_field(name="Passive", value=res['passiveName'], inline=True)
    embeded.add_field(name="Location", value=res['location'], inline=True)
    embeded.add_field(name="Ascension Material", value=res['ascensionMaterial'], inline=True)
    
    await ctx.send(embed=embeded)

@bot.command()
async def artifacts(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/artifacts/{}".format(arg)).text
    res = json.loads(r)

    if res['max_rarity'] == 5:
        embeded = discord.Embed(title="{}    ★★★★★".format(res['name']), color=0xd49548)
    elif res['max_rarity'] == 4:
        embeded = discord.Embed(title="{}    ★★★★".format(res['name']), color=0x935c9d)
    else:
        embeded = discord.Embed(title="{}    ★★★".format(res['name']), color=0x5d839a)

    if res['name'] in a1:
        artifacts = res['name'].replace("'s ", "s_").lower()
    else: 
        artifacts = res['name'].replace(" ", "_").lower()

    if res['name'] in a2:
        embeded.set_thumbnail(url=circlet.format(artifacts))
    else:
        embeded.set_thumbnail(url=artiimg.format(artifacts))

    if res['name'] in a2:
        embeded.add_field(name="1-Piece Bonus", value=res['1-piece_bonus'], inline=False)
    else:
        embeded.add_field(name="2-Piece Bonus", value=res['2-piece_bonus'], inline=False)
        embeded.add_field(name="4-Piece Bonus", value=res['4-piece_bonus'], inline=False)
    
    await ctx.send(embed=embeded)

@bot.command()
async def nations(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/nations/{}".format(arg)).text
    res = json.loads(r)

    if res['name'] == "Inazuma":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.inazuma, color=0xb38dc1)
        embeded.set_thumbnail(url=ina)
        embeded.set_image(url=ina_big)
    elif res['name'] == "Liyue":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.liyue, color=0xf2b723)
        embeded.set_thumbnail(url=liy)
        embeded.set_image(url=liy_big)
    elif res['name'] == "Mondstadt":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.mondstadt, color=0x71c2a7)
        embeded.set_thumbnail(url=mon)
        embeded.set_image(url=mon_big)
    else:
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.sumeru, color=0x9cc928)
        embeded.set_thumbnail(url=sum)
        embeded.set_image(url=sum_big)

    embeded.add_field(name="Element", value=res['element'], inline=True)
    embeded.add_field(name="Archon", value=res['archon'], inline=True)
    embeded.add_field(name="Controlling Entity", value=res['controllingEntity'], inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def elements(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/elements/{}".format(arg)).text
    res = json.loads(r)

    if res['name'] == "Anemo":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.anemo, color=0x71c2a7)
        embeded.set_thumbnail(url=ane)
        
    elif res['name'] == "Cryo":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.cryo, color=0xa4d6e3)
        embeded.set_thumbnail(url=cry)

    elif res['name'] == "Dendro":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.dendro, color=0x9cc928)
        embeded.set_thumbnail(url=den)

    elif res['name'] == "Electro":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.electro, color=0xb38dc1)
        embeded.set_thumbnail(url=ele)

    elif res['name'] == "Geo":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.geo, color=0xf2b723)
        embeded.set_thumbnail(url=geo)

    elif res['name'] == "Hydro":
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.hydro, color=0x5fc1f1)
        embeded.set_thumbnail(url=hyd)

    else:
        embeded = discord.Embed(title="{}".format(res['name']), description=bulk.pyro, color=0xea7838)
        embeded.set_thumbnail(url=pyr)

    for i in res['reactions']:
            embeded.add_field(name="{} - {}".format(i['name'], i['elements']), value=i['description'], inline = False)

    #if res['name'] == "Dendro" or "Hydro" or "Electro":
        

    await ctx.send(embed=embeded)
    
bot.run(TOKEN)