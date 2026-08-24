#Conversor de moeda
import discord
from discord.ext import commands
import requests

class Convert(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def converter(self,ctx: commands.Context, valor: float, origem: str, destino: str):
         url = f"https://api.frankfurter.dev/v2/rates?base={origem}&quotes={destino}" #API usada para dados de conversão
         resposta = requests.get(url)
         dados = resposta.json()
         taxa = dados[0]["rate"]
         resultado = valor * taxa
         await ctx.reply(f"{valor} {origem} equivale a {resultado: .2f} {destino}")
        



async def setup(bot):
    await bot.add_cog(Convert(bot))