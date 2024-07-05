import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='REPLACE_WITH_PREFIX', intents=intents)

@bot.event
async def on_ready():
    print(f'| > |  - - - - - - - - - - - - - -')
    print(f'| > | ')
    print(f'| > | Current Bot : {bot.user.name}!')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'|<->| Loaded cog sucessfully: {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

async def main():
    await load_cogs()
    await bot.start('REPLACE_WITH_TOKEN')

if __name__ == "__main__":
    asyncio.run(main())
