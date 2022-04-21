import os
import discord
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

    if message.author == client.user:
        return 

    if message.content.startswith('$elo'):
        await message.channel.send('eldoka na wolno')


@client.event
async def on_message(message):
  if message.content.startswith('!profile'):
    embedVar = discord.Embed(title="Hero Name:", description="Cygański Druid", color=0xfa1414)
    embedVar.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embedVar.set_image(url="https://static.wikia.nocookie.net/diablo/images/5/58/Druid_Artwork.jpg/revision/latest?cb=20080828143217")
    embedVar.add_field(name="Experience:", value="780xp", inline=False)
    embedVar.add_field(name="Weapon:", value="Spear", inline=False)
    embedVar.add_field(name="Sub-weapon:", value="Black Pigeon", inline=False)
    embedVar.add_field(name="Mount:", value="Dzik", inline=False)
    embedVar.add_field(name="Current status:", value="IDLE", inline=False)
    embedVar.set_thumbnail(url=message.author.avatar_url)


    await message.channel.send(embed=embedVar)





bot = commands.Bot(command_prefix='!')

left = '⏪'
right = '⏩'

messages = ("1", "2", "3")

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == bot.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check


@bot.command(pass_context=True)
async def series(ctx):
    index = 0
    while True:
        msg = await bot.say(messages[index])
        l = index != 0
        r = index != len(messages) - 1
        if l:
            await bot.add_reaction(msg, left) 
        if r:
            await bot.add_reaction(msg, right)
        # bot.wait_for_reaction
        react, user = await bot.wait_for_reaction(check=predicate(msg, l, r))
        if react.emoji == left:
            index -= 1
        elif react.emoji == right:
            index += 1
        await bot.delete_message(msg)





client.run(os.environ['TOKEN'])