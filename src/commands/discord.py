import discord
from discord.ext import commands


@commands.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f"{member} joined on {member.joined_at}")


@commands.command()
async def role(ctx, *, role: discord.Role):
    msg = """{role}:
    color: {color}
    created_at: {created_at}
    permissions: {permissions}
    members: {members}
    """.format(
        role=role,
        color=role.color,
        created_at=role.created_at,
        permissions=role.permissions.value,
        members=",".join([_.name for _ in role.members]),
    )
    await ctx.send(msg)


async def setup(bot):
    bot.add_command(joined)
    bot.add_command(role)
