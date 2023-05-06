import discord
from discord import Embed
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("The bot is online!!")

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="Embed Title", description="Embed description / Embed text")

    await ctx.reply(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong! : `{round(bot.latency * 1000)}ms`")

bot.run(TOKEN)
