import discord
from discord.ext import commands

# Configuração das permissões obrigatórias (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de palavras bloqueadas (adicione as palavras que quiser filtrar aqui)
PALAVRAS_PROIBIDAS = ["palavrao1", "palavrao2", "ofensa1", "ofensa2"]

@bot.event
async def on_ready():
    print(f"🤖 {bot.user.name} está online e protegendo o servidor!")

@bot.event
async def on_message(message):
    # Evita que o bot filtre as suas próprias mensagens
    if message.author == bot.user:
        return

    # Converte o texto para minúsculo para rastrear melhor
    mensagem_texto = message.content.lower()

    # Verifica se alguma palavra proibida está na mensagem
    for palavra in PALAVRAS_PROIBIDAS:
        if palavra in mensagem_texto:
            try:
                # Apaga a mensagem inadequada
                await message.delete()
                
                # Envia um aviso no chat marcando o usuário
                aviso = await message.channel.send(f"⚠️ {message.author.mention}, mantenha o chat limpo! Palavras inadequadas não são permitidas no Slap & Style Studios.")
                
                # (Opcional) Deleta o aviso do bot após 5 segundos para não poluir o chat
                await aviso.delete(delay=5)
                return
            except discord.Forbidden:
                print("Erro: O bot não tem permissão de 'Gerenciar Mensagens' neste canal.")
            except discord.NotFound:
                pass

    await bot.process_commands(message)

# Substitua pelo Token que você copiou lá no Discord Developer Portal
bot.run(MTUwNTI5OTc4ODk2OTY3NjgzMg.GL82eP.r_JrzHT7RY1FIB8-Z1znyigSoCkWfkJZ5baUbw)
