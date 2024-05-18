import discord
import asyncio
from discord.utils import find
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    general_channel = client.get_channel(98241607127556096)
    await general_channel.send('ConchBot Ready To Blow :shell: type !doot to blow into this mysterious item. I have returned from my sabbatical.')

@client.command()
async def doot(ctx):
    await ctx.send('<@155556141949124608> <@162071402747265024> <@170013015796744192> <@159444753186947074> <@176881949866983424> <@193819505162584064> Lets go bois')
    await ctx.send(file=discord.File('ronconch.gif'))
 
@client.command()
async def executivedoot(ctx):
    await ctx.send('<@155556141949124608> <@162071402747265024> <@98241017400016896> <@159444753186947074> <@176881949866983424> <@193819505162584064> Lets go bois')
    await ctx.send(file=discord.File('ronconch.gif'))

@client.command()
async def lgbtdoot(ctx):
    await ctx.send('<@155556141949124608> <@162071402747265024> <@98241017400016896> <@159444753186947074> <@176881949866983424> <@193819505162584064> Lets go bois')
    await ctx.send(file=discord.File('caramelldansen-the-caramell-dance.gif'))

@client.command()
async def oiwazzock(ctx):
    await ctx.send('<@155556141949124608> <@89553381395275776> <@162071402747265024> <@98241017400016896> <@159444753186947074> <@176881949866983424> <@193819505162584064> Lets go bois')
    await ctx.send(file=discord.File('lootrat.gif'))

@client.command()
async def mychest(ctx):
    await ctx.send('Our Chest')
    await ctx.send(file=discord.File('commie.gif'))

@client.command()
async def dmbook(ctx):
    await ctx.send('...rebalancing the encounter...')
    await ctx.send(file=discord.File('cheating.gif'))

@client.command()
async def dumpchest(ctx):
    await ctx.send('There is no dump chest.')

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('ConchBot Ready To Blow :shell: type !doot to blow into this mysterious item.')

client.run()
