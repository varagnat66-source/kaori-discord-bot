import discord #caso precise usar file, member, etc...
from discord.ext import commands

class Geral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Comandos aqui: 
    @commands.command()
    async def ola(self, ctx: commands.Context):
        nome = ctx.author.name
        imagem = discord.File("imagens/kaori_ola.gif")
        await ctx.reply(f"Olá, {nome}! Eu sou a Kaori sua ajudante virtual", file=imagem)

async def setup(bot):
    await bot.add_cog(Geral(bot))