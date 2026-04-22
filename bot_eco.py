import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

praticas = ["Faça separação do seu lixo", "Diminua o uso de descartáveis", "Não descarte pilhas e baterias em lixo comum", "Reduza o consumo de água", "escolha embalagens reutilizáveis","Mantenha as lâmpadas ligadas apenas quando necessário"]

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def ajuda(ctx):
    await ctx.send("""
📌 Lista de Comandos do Bot

♻️ como_ajudar
→ Eu cito algumas praticas sustentaveis

🌲 praticar
→ Eu vou enviar uma pratica sustentavel aleatoria para você executar

---
💡 Use os comandos com o prefixo $
""")

@bot.command()
async def dicas(ctx):
    await ctx.send("""
♻️→ Redução de Desperdícios (5 Rs): Repensar, recusar, reduzir, reutilizar e reciclar.
                   
💧→ Uso Consciente da Água: Fechar torneiras, consertar vazamentos e reutilizar água da máquina de lavar.

⚡→ Eficiência Energética: Apagar luzes, substituir por lâmpadas LED e tirar aparelhos da tomada.
                   
🌲→ Consumo Sustentável: Levar sacolas reutilizáveis, evitar plásticos de uso único (canudos, copos) e preferir produtos a granel.
                   
🍔→ Alimentação e Compostagem: Reduzir desperdício de comida, comprar de produtores locais e compostar resíduos orgânicos
""")
    
@bot.command()
async def praticar(ctx):
    pratica = random.choice(praticas)
    await ctx.send(pratica)

b
