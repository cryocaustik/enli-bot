import requests
from discord.ext import commands


@commands.command()
async def joke(ctx):
    api = "https://v2.jokeapi.dev/joke/Programming,Dark?blacklistFlags=racist"
    resp = requests.get(api)
    if not resp.ok:
        return None
    data = resp.json()
    await ctx.send(data["joke"])


@commands.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}.")


async def setup(bot):
    bot.add_command(joke)
    bot.add_command(hello)
