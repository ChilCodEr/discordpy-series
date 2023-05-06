import discord
from discord import app_commands, Embed
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    commands.Cog.listener()
    async def on_ready(self):
        print("Ping Cog is ready!!!!!!!")

    @commands.command()
    async def sync(self, ctx):
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands.")

    @app_commands.command(name="ping", description="the bots ping.")
    async def ping(self, interaction: discord.Interaction):
        bot = self.bot
    
        embed=discord.Embed(title="The bots ping", description=f"`{round(bot.latency * 1000)}ms`")
        await interaction.response.send_message("**Pong!**", embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot), guilds=[discord.Object(id=Your guild id)])
