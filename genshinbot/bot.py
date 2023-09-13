import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
import bulk 
import links

load_dotenv()
TOKEN = os.environ.get("DISCORD_BOT")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

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
    r = requests.get(links.chars.format(ndash)).text
    res = json.loads(r)

    if res['name'] in bulk.char_desc:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=bulk.char_desc[res['name']], color=bulk.colors_dict[res['vision']])
    else:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=res['description'], color=bulk.colors_dict[res['vision']])

    chpimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=links.charpfp.format(chpimg))
    
    if res['name'] in bulk.char_title:
        embeded.add_field(name="Title", value=bulk.char_title[res['name']], inline=True)
    else:
        embeded.add_field(name="Title", value=res['title'], inline=True)

    embeded.add_field(name="Vision", value=res['vision'], inline=True)
    embeded.add_field(name="Weapon", value=res['weapon'], inline=True)
    
    if res['name'] in bulk.char_gender:
        embeded.add_field(name="Gender", value=bulk.char_gender[res['name']], inline=True)
    else:
        embeded.add_field(name="Gender", value=res['gender'], inline=True)

    embeded.add_field(name="Nation", value=res['nation'], inline=True)

    if res['name'] in bulk.char_aff:
        embeded.add_field(name="Affiliation", value=bulk.char_aff[res['name']], inline=True)
    else:
        embeded.add_field(name="Affiliation", value=res['affiliation'], inline=True)

    embeded.add_field(name="Release", value=res['release'], inline=True)
    embeded.add_field(name="Constellation", value=res['constellation'], inline=True)
    embeded.add_field(name="Birthday", value=res['birthday'].replace("0000-", ""), inline=True)
    await ctx.send(embed=embeded)

@bot.command()
async def skills(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(links.chars.format(ndash)).text
    res = json.loads(r)

    if res['name'] in bulk.char_desc:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=bulk.char_desc[res['name']], color=bulk.colors_dict[res['vision']])
    else:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=res['description'], color=bulk.colors_dict[res['vision']])
    
    chpimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=links.charpfp.format(chpimg))

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
    r = requests.get(links.chars.format(arg)).text
    res = json.loads(r)

    if res['name'] in bulk.char_desc:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=bulk.char_desc[res['name']], color=bulk.colors_dict[res['vision']])
    else:
        embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=res['description'], color=bulk.colors_dict[res['vision']])

    charimg = res['name'].replace(" ", "_").lower()
    embeded.set_thumbnail(url=links.charpfp.format(charimg))

    for i in res['constellations']:
        embeded.add_field(name="{} : {}".format(i['unlock'], i['name']), value=i['description'], inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def weapons(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/weapons/{}".format(arg)).text
    res = json.loads(r)

    embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['rarity']]), description=res['passiveDesc'], color=bulk.colors_dict[res['rarity']])
    
    if res['name']in w2:
        weapons = res['name'].replace("'s ", "s_").lower()
    elif res['name'] == "Amos' Bow":
        weapons = res['name'].replace("s' ", "s_").lower()
    elif res['name'] in w3:
        weapons = res['name'].replace("'s", "s").replace(" ", "_").lower()
    else:
        weapons = res['name'].replace(" ", "_").lower()

    embeded.set_thumbnail(url=links.weapimg.format(weapons))
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

    embeded = discord.Embed(title="{}    {}".format(res['name'], bulk.rarity_dict[res['max_rarity']]), color=bulk.colors_dict[res['max_rarity']])

    if res['name'] in a1:
        artifacts = res['name'].replace("'s ", "s_").lower()
    else: 
        artifacts = res['name'].replace(" ", "_").lower()

    if res['name'] in a2:
        embeded.set_thumbnail(url=links.circlet.format(artifacts))
    else:
        embeded.set_thumbnail(url=links.artiimg.format(artifacts))

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

    embeded = discord.Embed(title="{}".format(res['name']), description=bulk.nations_dict[res['name']], color=bulk.colors_dict[res['element']])
    embeded.set_thumbnail(url=links.nation_icon[res['name']])
    embeded.set_image(url=links.nation_img[res['name']])

    embeded.add_field(name="Element", value=res['element'], inline=True)
    embeded.add_field(name="Archon", value=res['archon'], inline=True)
    embeded.add_field(name="Controlling Entity", value=res['controllingEntity'], inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def elements(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get("https://genshin.jmp.blue/elements/{}".format(arg)).text
    res = json.loads(r)

    embeded = discord.Embed(title="{}".format(res['name']), description=bulk.elements_dict[res['name']], color=bulk.colors_dict[res['name']])
    embeded.set_thumbnail(url=links.ele_icon[res['name']])

    for i in res['reactions']:
            embeded.add_field(name="{} - {}".format(i['name'], i['elements']), value=i['description'], inline = False)

    if res['name'] == "Hydro":
        embeded.add_field(name="Bloom - ['Dendro']", value=bulk.elements_dict["Bloom"], inline = False)
        embeded.add_field(name="Hyperbloom - ['Dendro', 'Electro']", value=bulk.elements_dict["Hyperbloom"], inline = False)
        embeded.add_field(name="Burgeon - ['Dendro', 'Pyro']", value=bulk.elements_dict["Burgeon"], inline = False)

    if res['name'] == "Pyro":
        embeded.add_field(name="Burgeon - ['Dendro', 'Hydro']", value=bulk.elements_dict["Burgeon"], inline = False)
    
    if res['name'] == "Electro":
        embeded.add_field(name="Hyperbloom - ['Dendro', 'Hydro']", value=bulk.elements_dict["Hyperbloom"], inline = False)
        embeded.add_field(name="Catalyze - ['Dendro']", value=bulk.elements_dict["Catalyze"], inline = False)

    if res['name'] == "Dendro":
        embeded.add_field(name="Bloom - ['Hydro']", value=bulk.elements_dict["Bloom"], inline = False)
        embeded.add_field(name="Hyperbloom - ['Hydro', 'Electro']", value=bulk.elements_dict["Hyperbloom"], inline = False)
        embeded.add_field(name="Burgeon - ['Hydro', 'Pyro']", value=bulk.elements_dict["Burgeon"], inline = False)
        embeded.add_field(name="Catalyze - ['Electro']", value=bulk.elements_dict["Catalyze"], inline = False)
    
    await ctx.send(embed=embeded)
    
@bot.command()
async def boss(ctx, *, arg):
    ndash = arg.replace(" ", "-").lower()
    r = requests.get(links.bosses.format(ndash)).text
    res = json.loads(r)

    embeded = discord.Embed(title=res['name'], description=res['description'])
    embeded.set_thumbnail(url=links.weekly_icon[res['name']])
    
    for i in res['drops']:
        embeded.add_field(name="{}    ★★★★★".format(i['name']), value="• From: {}".format(i['source']), inline = False)

    embeded.add_field(name="Artifacts:\n", value="• Wanderer's Troupe    ★★★★★\n• Gladiator's Finale    ★★★★★\n• The Exile    ★★★★\n• Instructor    ★★★★\n• Berserker    ★★★★", inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def enemy(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.enemies.format(arg)).text
    res = json.loads(r)

    if res['name'] in bulk.enemy_dict:
        embeded = discord.Embed(title=res['name'], description=bulk.enemy_dict[res['name']])
    else:
        embeded = discord.Embed(title=res['name'], description=res['description'])

    embeded.set_thumbnail(url=links.ene_img[res['name']])
    embeded.add_field(name="Region", value=res['region'], inline=True)
    embeded.add_field(name="Type", value=res['type'], inline=True)

    if res['name'] == "Fatui Cicin Mage":
        embeded.add_field(name="Elements", value=res['element'], inline=True)
    else:
        embeded.add_field(name="Elements", value=res['elements'], inline=True)

    if "drops" in res:
        if res['drops'] != "None":
            for i in res['drops']:
                embeded.add_field(name=i['name'], value="• Rarity: {}\n• Minimum Level: {}".format(bulk.rarity_dict[i['rarity']], i['minimum-level']), inline=False)
    
    if "artifacts" in res:
        for i in res['artifacts']:
            embeded.add_field(name=i['name'], value="• Set: {}".format(i['set']), inline=False)

    if "descriptions" in res:
        if res['name'] == "The Eremite":
            for i in res['descriptions']:
                embeded.add_field(name=i['name'], value="A member of a loosely-organized mercenary corps from the golden desert sands.", inline=False)
        else:
            for i in res['descriptions']:
                embeded.add_field(name=i['name'], value=i["description"], inline=False)

    if "elemental-descriptions" in res:
        for i in res['elemental-descriptions']:
            embeded.add_field(name="Variation: {}".format(i['element']), value=i["description"], inline=False)
    if "mora-gained" in res:
        embeded.add_field(name="Mora Gained", value=res["mora-gained"], inline=False)

    embeded.set_footer(text="Thumbnails may not be representative of all enemy subtypes.", icon_url=None)

    await ctx.send(embed=embeded)

bot.run(TOKEN)