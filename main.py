import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
class MeuBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.geral") # comando para puxar a função de outro arquivo 
        await self.load_extension("cogs.convert") #comando de converter moedas
        await self.load_extension("cogs.promo") #comando de automação de promoção
        await self.load_extension("cogs.purge") #comando para limpar chats
bot = MeuBot(".", intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CANAL = int(os.getenv("CANAL_CHEGADA"))
CARGO = int(os.getenv("ID_CARGO"))
SAIDA = int(os.getenv("CANAL_SAIDA"))

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso!")

@bot.event
async def on_member_join(membro: discord.Member):
    canal = bot.get_channel(CANAL)  # add o id do canal desejado
    cargo = membro.guild.get_role(CARGO) #add o id do cargo 
    imagem = discord.File("imagens/doce.gif", "doce.gif")
    minha_embed = discord.Embed()
    minha_embed.title = "Bem-Vindo"
    minha_embed.description = f"vai um docinho ai?{membro.mention}"
    minha_embed.set_image(url="attachment://doce.gif")

    await canal.send(embed=minha_embed, file=imagem)
    await membro.add_roles(cargo) #add o cargo a quem entrar no servidor

@bot.event
async def on_member_remove(membro: discord.Member):
    canal = bot.get_channel(SAIDA)
    imagem = discord.File("imagens/tchau.gif", "tchau.gif")
    card_embed = discord.Embed()
    card_embed.title = f"{membro.mention} Saiu do servidor"
    card_embed.description = "Adeus, cuidado no caminho!!"
    card_embed.set_image(url="attachment://tchau.gif")

    await canal.send(embed=card_embed, file=imagem)


#Avisos de erros nos comandos
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Desculpa mas isso não é um comando valido.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Acho que falta algo no seu comando")
    elif isinstance(error, commands.BadArgument):
        await ctx.reply("Talvez a formato dos valores estão errados.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.reply("Desculpe, mas você não tem permissão para este comando.")  
    else:
        await ctx.reply("Ixi algo de errado não esta certo.")             
    


    


bot.run(TOKEN)