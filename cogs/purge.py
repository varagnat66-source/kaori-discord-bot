import discord
from discord.ext import commands
import requests

class Purge(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self,ctx, quantidade: int = 100):
        deleted = await ctx.channel.purge(limit=quantidade)
        await ctx.send(f"{len(deleted)} mensagens apagadas!!")




async def setup(bot): 
    await bot.add_cog(Purge(bot))