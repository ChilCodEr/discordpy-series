import discord
from discord.ext import commands
from config import TOKEN
import os
import asyncio

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("The bot is online!!")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
