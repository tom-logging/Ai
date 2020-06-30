#!/usr/bin/python
import discord
import random
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get

class Randomcommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='WELCOME')
        await channel.send(f"Welcome {member.mention}")
        role = get(member.guild.roles, name="ROLE")
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='WELCOME')
        await channel.send(f"Goodbye {member.name}")

    @commands.command(aliases=['50/50', '50', 'yes', 'no' ])
    async def yesorno(self, ctx, *, question):
        responses = ['yes', 'no']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def send_dm(self, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)

    @commands.command(aliases=['Clear', 'CLEAR'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Randomcommands(client))
