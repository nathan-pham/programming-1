import discord
from discord.ext import commands, tasks
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    
    # with open("screenshots/2022-01-06-10-06-02.png", "rb") as f:
    #     await bot.user.edit(avatar=f.read())
    #     print("updated avatar")

# @tasks.loop(seconds=10)
# async def change_avatar():
#     with open("screenshots/2022-01-06-10-06-02.png", "rb") as f:
#         await bot.user.edit(avatar=f.read())
#         print("updated avatar")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run('')
# thanks discord for removing my token for me!
