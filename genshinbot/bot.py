import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
import bulk 
import links
import string

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

c1 = ["hilichurl-horns", "ley-line", "bone-shards", "mist-grass", "fatui-knives", "chaos-parts"]
c2 = ["slime", "hilichurl-masks", "hilichurl-arrowheads", "samachurl-scrolls", "treasure-hoarder-insignias", "fatui-insignias", "whopperflower-nectar"]

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

@bot.command()
async def food(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.food).text
    res = json.loads(r)

    if res[arg]['name'] == "Invigorating Kitty Meal":
        embeded = discord.Embed(title="{}    {}".format(res[arg]['name'], bulk.rarity_dict[res[arg]['rarity']]), description=bulk.kitty_meal, color=bulk.colors_dict[res[arg]['rarity']])
    else:
        embeded = discord.Embed(title="{}    {}".format(res[arg]['name'], bulk.rarity_dict[res[arg]['rarity']]), description=res[arg]['description'], color=bulk.colors_dict[res[arg]['rarity']])
    if res[arg]['name'] in links.food_p1:
        embeded.set_thumbnail(url=links.food_img1.format(links.food_p1[res[arg]['name']]))
    else:
        embeded.set_thumbnail(url=links.food_img2.format(links.food_p2[res[arg]['name']]))
    if "proficiency" in res[arg]:
        embeded.add_field(name="Proficiency", value=res[arg]['proficiency'], inline=True)
    embeded.add_field(name="Type", value=res[arg]['type'], inline=True)
    embeded.add_field(name="Effect", value=res[arg]['effect'], inline=False)
    if res[arg]['hasRecipe'] == True:
        recipe_str = ""
        for j in res[arg]['recipe']:
            recipe_str += "\- {} {}\n".format(j['quantity'], j['item'])
            
        embeded.add_field(name="Recipe", value=recipe_str, inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def potion(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.potion).text
    res = json.loads(r)

    embeded = discord.Embed(title="{}    {}".format(res[arg]['name'], bulk.rarity_dict[res[arg]['rarity']]), description=bulk.potion_desc[res[arg]['name']], color=bulk.colors_dict[res[arg]['rarity']])
    embeded.set_thumbnail(url=links.potion_img.format(links.potion_dict[res[arg]['name']]))
    embeded.add_field(name="Effect", value=res[arg]['effect'], inline=False)
    crafting_str = ""
    for j in res[arg]['crafting']:
        crafting_str += "\- {} {}\n".format(j['quantity'], j['item'])
            
    embeded.add_field(name="Crafting", value=crafting_str, inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def bm(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.materials.format("boss-material")).text
    res = json.loads(r)
    ldash = res[arg]['name'].replace(" ", "_").replace("'", "").lower()
    
    embeded = discord.Embed(title="{}    ★★★★".format(res[arg]['name']), description=bulk.bm[res[arg]['name']], color=bulk.colors_dict[4])
    embeded.set_thumbnail(url=links.mats_img.format(ldash))
    embeded.add_field(name="Source", value=res[arg]['source'], inline=True)
    embeded.add_field(name="Characters", value=res[arg]['characters'], inline=True)

    await ctx.send(embed=embeded)
    
@bot.command()
async def ca(ctx, arg1, arg2):
    arg2 = arg2.replace(" ", "-").lower()
    r = requests.get(links.materials.format("character-ascension")).text
    res = json.loads(r)
    rock = ""
    source_list = ""

    if "sliver" in arg2:
        rock = "sliver"
    elif "fragment" in arg2:
        rock = "fragment"
    elif "chunk" in arg2:
        rock = "chunk"
    else:    
        rock = "gemstone"

    embeded = discord.Embed(title="{}    {}".format(res[arg1][rock]['name'], bulk.rarity_dict[res[arg1][rock]['rarity']]), description=bulk.ca[res[arg1][rock]['name']], color=bulk.colors_dict[res[arg1][rock]['rarity']])
    embeded.set_thumbnail(url=links.gem_img.format(links.ca_img[res[arg1][rock]['name']]))
    for i in res[arg1][rock]['sources']:
        source_list += "\- {}\n".format(i)
    embeded.add_field(name="Sources", value=source_list, inline=False)

    await ctx.send(embed=embeded)
        
@bot.command()
async def ce(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.materials.format("character-experience")).text
    res = json.loads(r)

    if arg == "wanderer's-advice":
        embeded = discord.Embed(title="{}    {}".format(res['items'][0]['name'], bulk.rarity_dict[res['items'][0]['rarity']]), description=bulk.ce[res['items'][0]['name']], color=bulk.colors_dict[res['items'][0]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.ce_img[res['items'][0]['name']]))
        embeded.add_field(name="Experience", value=res['items'][0]['experience'], inline=False)
    elif arg == "adventurer's-experience":
        embeded = discord.Embed(title="{}    {}".format(res['items'][1]['name'], bulk.rarity_dict[res['items'][1]['rarity']]), description=bulk.ce[res['items'][1]['name']], color=bulk.colors_dict[res['items'][1]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.ce_img[res['items'][1]['name']]))
        embeded.add_field(name="Experience", value=res['items'][1]['experience'], inline=False)
    else:
        embeded = discord.Embed(title="{}    {}".format(res['items'][2]['name'], bulk.rarity_dict[res['items'][2]['rarity']]), description=bulk.ce[res['items'][2]['name']], color=bulk.colors_dict[res['items'][2]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.ce_img[res['items'][2]['name']]))
        embeded.add_field(name="Experience", value=res['items'][2]['experience'], inline=False)


    await ctx.send(embed=embeded)

@bot.command()
async def ci(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.materials.format("cooking-ingredients")).text
    res = json.loads(r)
    rare = 1
    source_list = ""
    if 'rarity' in res[arg]:
        rare = res[arg]['rarity']

    embeded = discord.Embed(title="{}    {}".format(res[arg]['name'], bulk.rarity_dict[rare]), description=res[arg]['description'], color=bulk.colors_dict[rare])
    embeded.set_thumbnail(url=links.mats_img.format(links.ci_img[res[arg]['name']]))
    for i in res[arg]['sources']:
        source_list += "\- {}\n".format(i)
    embeded.add_field(name="Sources", value=source_list, inline=False)


    await ctx.send(embed=embeded)

@bot.command()
async def coa(ctx, arg1, arg2):
    arg1 = arg1.replace(" ", "-").lower()
    arg2 = arg2.replace(" ", "-").lower()
    r = requests.get(links.materials.format("common-ascension")).text
    res = json.loads(r)
    char = ""
    sour = ""

    if arg2 in bulk.coa2_dict:
        co = res[arg1]['items'][bulk.coa2_dict[arg2]]['name']
        embeded = discord.Embed(title="{}    {}".format(co, bulk.rarity_dict[res[arg1]['items'][bulk.coa2_dict[arg2]]['rarity']]), description=bulk.coa_desc[co], color=bulk.colors_dict[res[arg1]['items'][bulk.coa2_dict[arg2]]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.coa_img[co]))

    if arg1 in c1:
        for i in res[arg1]['weapons']:
            char += "\• {}\n".format(string.capwords(i))
        embeded.add_field(name="Weapons", value=char, inline=True)
    elif arg1 in c2:
        for i in res[arg1]['characters']:
            char += "\• {}\n".format(string.capwords(i))
        embeded.add_field(name="Characters", value=char, inline=True)
        
    for j in res[arg1]['sources']:
        sour += "\• {}\n".format(j)
    embeded.add_field(name="Sources", value=sour, inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def ls(ctx, arg1, arg2):
    arg2 = arg2.replace(" ", "-").lower()
    r = requests.get(links.materials.format("local-specialties")).text
    res = json.loads(r)
    formatting = res[arg1][bulk.ls[arg2]]
    char_list = ""

    embeded = discord.Embed(title="{}".format(formatting['name']), description=bulk.ls_desc[formatting['name']], color=bulk.colors_dict[1])
    embeded.set_thumbnail(url=links.mats_img.format(links.ls_img[formatting['name']]))
    for i in formatting['characters']:
        char_list += "\- {}\n".format(string.capwords(i))
    embeded.add_field(name="Characters", value=char_list, inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def tb(ctx, arg1, arg2):
    arg2 = arg2.replace(" ", "-").lower()
    r = requests.get(links.materials.format("talent-book")).text
    res = json.loads(r)
    formatting = res[arg1]['items'][bulk.tb[arg2]]
    char_list = ""
    ava_list = ""
    source = res[arg1]['source'].replace("-", " ")

    embeded = discord.Embed(title="{}    {}".format(formatting['name'], bulk.rarity_dict[formatting['rarity']]), description=bulk.tb_desc[arg2], color=bulk.colors_dict[formatting['rarity']])
    embeded.set_thumbnail(url=links.mats_img.format(links.tb_img[arg2]))
    for i in res[arg1]['availability']:
        ava_list += "\- {}\n".format(string.capwords(i))
    embeded.add_field(name="Availability", value=ava_list, inline=True)
    embeded.add_field(name="Source", value=string.capwords(source), inline=True)
    for j in res[arg1]['characters']:
        char_list += "\- {}\n".format(string.capwords(j))
    embeded.add_field(name="Characters", value=char_list, inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def tbs(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.materials.format("talent-boss")).text
    res = json.loads(r)
    char_list = ""

    embeded = discord.Embed(title="{}".format(res[arg]['name']), description=bulk.tbs_desc[res[arg]['name']], color=bulk.colors_dict[5])
    embeded.set_thumbnail(url=links.mats_img.format(links.tbs_img[res[arg]['name']]))
    for i in res[arg]['characters']:
        char_list += "\- {}\n".format(string.capwords(i))
    embeded.add_field(name="Used By", value=char_list, inline=False)

    await ctx.send(embed=embeded)

@bot.command()
async def wa(ctx, arg1, arg2):
    arg2 = arg2.replace(" ", "-").lower()
    r = requests.get(links.materials.format("weapon-ascension")).text
    res = json.loads(r)

    weap = ""
    avab = ""
    sour = res[arg1]['source'].replace("-", " ")

    if arg2 in bulk.wa:
        co = res[arg1]['items'][bulk.wa[arg2]]['name']
        embeded = discord.Embed(title="{}    {}".format(co, bulk.rarity_dict[res[arg1]['items'][bulk.wa[arg2]]['rarity']]), description=bulk.wa_desc[co], color=bulk.colors_dict[res[arg1]['items'][bulk.wa[arg2]]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.wa_img[co]))
        
    for i in res[arg1]['weapons']:
        low = i.replace("-", " ")
        weap += "\• {}\n".format(string.capwords(low))
    embeded.add_field(name="Weapons", value=weap, inline=True)

    for j in res[arg1]['availability']:
        avab += "\• {}\n".format(string.capwords(j))
    embeded.add_field(name="Availability", value=avab, inline=True)
        
    embeded.add_field(name="Source", value=string.capwords(sour), inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def we(ctx, *, arg):
    arg = arg.replace(" ", "-").lower()
    r = requests.get(links.materials.format("weapon-experience")).text
    res = json.loads(r)

    if arg == "enhancement-ore":
        embeded = discord.Embed(title="{}    {}".format(res['items'][0]['name'], bulk.rarity_dict[res['items'][0]['rarity']]), description=bulk.we_desc[arg], color=bulk.colors_dict[res['items'][0]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.we_img[arg]))
        embeded.add_field(name="Experience", value=res['items'][0]['experience'], inline=True)
        embeded.add_field(name="Source", value="Crafting", inline=True)
    elif arg == "fine-enhancement-ore":
        embeded = discord.Embed(title="{}    {}".format(res['items'][1]['name'], bulk.rarity_dict[res['items'][1]['rarity']]), description=bulk.we_desc[arg], color=bulk.colors_dict[res['items'][1]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.we_img[arg]))
        embeded.add_field(name="Experience", value=res['items'][1]['experience'], inline=True)
        embeded.add_field(name="Source", value="Crafting", inline=True)
    else:
        embeded = discord.Embed(title="{}    {}".format(res['items'][2]['name'], bulk.rarity_dict[res['items'][2]['rarity']]), description=bulk.we_desc[arg], color=bulk.colors_dict[res['items'][2]['rarity']])
        embeded.set_thumbnail(url=links.mats_img.format(links.we_img[arg]))
        embeded.add_field(name="Experience", value=res['items'][2]['experience'], inline=True)
        embeded.add_field(name="Source", value="Crafting", inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def domain(ctx, arg1, arg2=None, arg3=None):
    arg1 = arg1.replace(" ", "-").lower()
    r = requests.get(links.domains.format(arg1)).text
    res = json.loads(r)
    ele_list = ""

    if res['type'] == "Forgery":
        embeded = discord.Embed(title=res['name'], description=res['description'])
        embeded.add_field(name="Type", value=res['type'], inline=True)
        embeded.add_field(name="Location", value=res['location'], inline=True)
        embeded.set_image(url=links.domain_img[res['name']])
        embeded.set_thumbnail(url=links.nation_icon[res['nation']])
        for i in res['recommendedElements']:
            ele_list += "\- {}\n".format(i)
        embeded.add_field(name="Recommended Elements", value=ele_list, inline=True)

        if arg2 == "reqs":
            for i in res['requirements']:
                req_list = "\- Adventure Rank: {}\n\- Recommended Level: {}\n\- Leyline Disorder: {}".format(i['adventureRank'], i['recommendedLevel'], i['leyLineDisorder'])
                embeded.add_field(name="Level: {}".format(i['level']), value=req_list, inline=False)

        elif arg2 == "rewards":
            for j in res['rewards'][bulk.days[arg3]]['details']:
                rewards_list = "\- Adventure Experience: {}\n\- Companion Experience: {}\n\- Mora: {}\n".format(j['adventureExperience'], j['companionshipExperience'], j['mora'])
                if "drops" not in j:
                    for k in j['items']:
                        rewards_list += "\- {}\n".format(k['name'])
                else:
                    for k in j['drops']:
                        rewards_list += "\- {}\n".format(k['name'])
                if arg3 == "mon" or arg3 =="thu":            
                    embeded.add_field(name="Monday/Tuesday - Level: {}".format(j['level']), value=rewards_list, inline=False)
    
                elif arg3 == "tue" or arg3 == "fri":
                    embeded.add_field(name="Tuesday/Friday - Level: {}".format(j['level']), value=rewards_list, inline=False)

                elif arg3 == "wed" or arg3 == "sat":
                    embeded.add_field(name="Wednesday/Saturday - Level: {}".format(j['level']), value=rewards_list, inline=False)

                elif arg3 == "sun":
                    embeded.add_field(name="Sunday - Level: {}".format(j['level']), value=rewards_list, inline=False)

    else:
        embeded = discord.Embed(title=res['name'], description=res['description'])
        embeded.add_field(name="Type", value=res['type'], inline=True)
        embeded.add_field(name="Location", value=res['location'], inline=True)
        embeded.set_image(url=links.domain_img[res['name']])
        embeded.set_thumbnail(url=links.nation_icon[res['nation']])
        for i in res['recommendedElements']:
            ele_list += "\- {}\n".format(i)
        embeded.add_field(name="Recommended Elements", value=ele_list, inline=True)

        if arg2 == "reqs":
            for i in res['requirements']:
                req_list = "\- Adventure Rank: {}\n\- Recommended Level: {}\n\- Leyline Disorder: {}".format(i['adventureRank'], i['recommendedLevel'], i['leyLineDisorder'])
                embeded.add_field(name="Level: {}".format(i['level']), value=req_list, inline=False)

        elif arg2 == "rewards":
            for j in res['rewards'][0]['details']:
                rewards_list = "\- Adventure Experience: {}\n\- Companion Experience: {}\n\- Mora: {}\n".format(j['adventureExperience'], j['companionshipExperience'], j['mora'])
                for k in j['drops']:
                    rewards_list += "\- {}\n".format(k['name'])
                embeded.add_field(name="Rewards - Level: {}".format(j['level']), value=rewards_list, inline=False)

    await ctx.send(embed=embeded)

bot.run(TOKEN)