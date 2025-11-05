import discord
from discord.ext import commands
import os  
import dotenv  
dotenv.load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)
bot.run(bot_token)