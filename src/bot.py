import asyncio
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_COMMAND_PREFIX = getenv("DISCORD_COMMAND_PREFIX")
if not DISCORD_COMMAND_PREFIX:
    raise ValueError("DISCORD_COMMAND_PREFIX not found")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=DISCORD_COMMAND_PREFIX, intents=intents)


@bot.command()
async def test(ctx: commands.Context):
    print(ctx)
    await ctx.reply("ok")


async def main():
    token = getenv("DISCORD_TOKEN")
    await bot.load_extension("commands.jokes")
    await bot.load_extension("commands.discord")
    await bot.start(token)


asyncio.run(main())
