import discord
import asyncio
from discord import Member
from discord.ext import commands

TOKEN = "NzY4NDQwNjY1OTU5ODI1NDA5.X5AgIw.1wvWUBOlAfop8AQq6-QqpSTrci0"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= "+" , intents=intents)

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
@commands.guild_only()
async def ping(ctx):
   "This commands shows the bot latency, also known as the ping of its host server"
   embed = discord.Embed(title = "Want a Ping? Here's a:", description = (f'Pong! {round(client.latency * 1000)}ms'), color = (0xdcddde))
   await ctx.send(embed=embed)

@bot.command()
async def cutg(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/657673094810566656/766280503996448828/video0.mp4")

@bot.command()
async def no(ctx):
    await ctx.send("https://media.discordapp.net/attachments/729229092976722023/767795660782436352/gru_no.jpg")

@bot.command()
async def hug(ctx):
    await ctx.send("Hug has been given to you!!!!")

bot.run(TOKEN)