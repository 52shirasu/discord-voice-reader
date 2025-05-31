from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")
