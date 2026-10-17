import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import requests
import os 

class Promo(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
        self.jogos_anteriores = [] #começa vazia
        load_dotenv()
        self.CHAT_PROMO = int(os.getenv("CANAL_PROMO"))
        self.CONTATO = os.getenv("CONTATO")
        self.minha_tarefa.start()



    #comando manual de lista de promoção
    @commands.command()
    async def promo(self,ctx:commands.Context):
        url ="https://www.cheapshark.com/api/1.0/deals?storeID=1&onSale=1&sortBy=Savings&pageSize=10"
        headers = {"User-Agent": f"KaoriBot/1.0 ({self.CONTATO})"}
        resposta = requests.get(url, headers=headers)
        dados = resposta.json()
        texto = ""
        for jogo in dados:
            titulo = jogo["title"]
            preco_original = jogo["normalPrice"]
            preco_promocional = jogo["salePrice"]
            desconto = float(jogo["savings"])
            texto = texto + f"**{titulo}** | De ${preco_original} por ${preco_promocional} ({desconto:.1f}% off)\n\n"
        list_embed = discord.Embed()
        list_embed.title = "🔥 Promoção da Steam"
        list_embed.description = texto
        list_embed.color = discord.Color.yellow()
        await ctx.reply(embed=list_embed)

    #aviso de promoção individual e automatico
    @tasks.loop(minutes=50)
    async def minha_tarefa(self):
        url ="https://www.cheapshark.com/api/1.0/deals?storeID=1&onSale=1&sortBy=Savings&pageSize=10"
        headers = {"User-Agent": f"KaoriBot/1.0 ({self.CONTATO})"}
        puxada = requests.get(url, headers=headers)
        dados = puxada.json()
        canal = self.bot.get_channel(self.CHAT_PROMO)
        for  jogo in dados: 
            titulo = jogo["title"]
            preco_original = jogo["normalPrice"]
            preco_promocional = jogo["salePrice"]
            desconto = float(jogo["savings"])
            capa = jogo["thumb"]

            if titulo not in self.jogos_anteriores:        
             promo_embed = discord.Embed()
             promo_embed.title = titulo
             promo_embed.description = f"De ${preco_original} por ${preco_promocional} ({desconto:.1f}% off)"
             promo_embed.color = discord.Color.yellow()
             promo_embed.set_image(url=capa)
             await canal.send(embed=promo_embed)

        self.jogos_anteriores = [jogo["title"] for jogo in dados]       

    @minha_tarefa.before_loop
    async def antes_da_tarefa(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Promo(bot))