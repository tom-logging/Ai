#!/usr/bin/python
import discord
import os
import asyncio
import asyncpg
import datetime
from datetime import datetime
from discord.utils import get
from discord.ext import commands, tasks
from discord.utils import get
from discord import Game

client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def statuschange():
    await client.wait_until_ready()
    while True:
        await client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity (type = discord.ActivityType.watching, name = "TEST1"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity (type = discord.ActivityType.watching, name = "TEST2"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity (type = discord.ActivityType.watching, name = "TEST3"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity (type = discord.ActivityType.watching, name = "TEST4"))
        await asyncio.sleep(5)

@client.event
async def on_ready(member: discord.Member=None, pass_context=True):
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')
    await statuschange()
    client.loop.create_task(statuschange())


client.run('TOKEN HERE')
