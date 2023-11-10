from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @app_commands.command(name = "say", description = "大聲說出來")
    @app_commands.describe(name = "輸入人名", text = "輸入要說的話")
    async def say(self, interaction: discord.Interaction, name: str, text: Optional[str] = None):
        if text == None:
            text = "。。。"
        await interaction.response.send_message(f"{name} 說 「{text}」")
    
    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("succeed!")

async def setup(bot):
    await bot.add_cog(Main(bot))