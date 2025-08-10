import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#
#╔══════════════════════╗
#║      discord:        ║
#║   .gg/toprakates     ║
#╚══════════════════════╝
#

load_dotenv()  # .env dosyasına tokeninizi girin
TOKEN = os.getenv("DISCORD_TOKEN")

SUGGESTION_CHANNEL_ID = channelid

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Giriş yapıldı: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != SUGGESTION_CHANNEL_ID:
        return

    await message.delete()

    embed = discord.Embed(
        title="🗳️ Oylama Başladı!",
        description=message.content,
        color=discord.Color.blue()
    )
    embed.set_footer(
        text=f"Gönderen: {message.author.display_name}",
        icon_url=message.author.avatar.url if message.author.avatar else None
    )

    embed_message = await message.channel.send(embed=embed)

    await embed_message.add_reaction("✅")
    await embed_message.add_reaction("❌")

    await bot.process_commands(message)

bot.run(TOKEN)

#
