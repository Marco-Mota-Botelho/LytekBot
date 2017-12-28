#Lytek bot to manage the Exalted Hub

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='$')
client = discord.Client ()

@bot.event
async def on_ready():
    print("Ready when you are xD")
    print ("I am running on " + bot.user.name)  
    print ("With the ID: "+ bot.user.id)


@bot.command(pass_context = True)
async def info (ctx, user: discord.Member):
    embed = discord.Embed (title = "{}'s information.".format(user.name), description = "Here's what I could find.", color = 0x00ff00)
    embed.add_field(name="Name", value = user.name, inline = True)
    embed.add_field(name = "ID", value = user.id, inline = True)
    embed.add_field(name = "Status", value = user.status, inline = True)
    embed.add_field(name = "Table", value = user.top_role, inline = True)
    embed.add_field(name ="Joined", value = user.joined_at, inline = True)
    embed.set_thumbnail(url = user.avatar_url)
    await bot.say(embed = embed)


@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    await bot.say(':boot: The Bureaucracy isn\'t pleased with your actions {}. Good Bye'.format(user.name))
    await bot.kick(user)
    print("User {} has been kicked".format(user.name))

@bot.command(pass_context = True)
async def embed(ctx):
    embed = discord.Embed(title = 'Test', description = "my name is Lytek", color = 0x00ff00)
    embed.set_footer(text = 'this is a footer')
    embed.set_author(name = "Lytek of the celestial bureaucracy")
    embed.add_field( name = "This is a field", value = "no it isn't", inline = True)
    await bot.say (embed = embed)



bot.run('Mzk0OTYzNzIzMzc2Mzk0MjQw.DSSjfA.kZAWFfyMYm8pO3mVtxjQEAxKa8k')# Token to run bot, we may need to change it.
