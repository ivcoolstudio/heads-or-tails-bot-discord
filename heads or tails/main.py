import discord, random
from discord.ext import commands

bot = commands.Bot(command_prefix='>', intents = discord.Intents.all())

@bot.command()
async def орелилирешка(ctx):
    await ctx.send(random.choice(['орел 🌕', 'решка 🌑']))

bot.run('token')