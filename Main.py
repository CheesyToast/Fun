import discord
import asyncio
from discord.ext import commands

TOKEN = "NzY4NDQwNjY1OTU5ODI1NDA5.X5AgIw.1wvWUBOlAfop8AQq6-QqpSTrci0"
intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix= "+" , intents=intents)

@bot.event()
async def on_ready():
    print("Bot is online!")

@bot.command()
@commands.guild_only()
async def ping(ctx):
   "This commands shows the bot latency, also known as the ping of its host server"
   embed = discord.Embed(title = "Want a Ping? Here's a:", description = (f'Pong! {round(client.latency * 1000)}ms'), color = (0xdcddde))
   await ctx.send(embed=embed)  

bot.run(TOKEN)