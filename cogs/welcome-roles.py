import discord
import json
import asyncio
import os
import asyncpg
import random
from discord import Member
from discord.ext import commands
from discord.utils import get

class Welcomeroles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colours = {
            'red' : 0xeb4034,
            'green' : 0x008000,
            'blue' : 0x3434e,
            'brown' : 0xD2691E,
            'purple' : 0x9400D3,
            'yellow' : 0xfce803,
            'orange' : 0xff9b05,
            'lime-green' : 0x61ff05,
            'pink' : 0xffc0cb,
            'light-blue' : 0x03fcf4,
            'light-purple' : 0xd514d9,
            'invisible' : 0x36393f
    }

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='welcome')
        await channel.send(f"Welcome {member.mention}")
        role = get(member.guild.roles, name='gamers')
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='welcome')
        await channel.send(f"Goodbye {member.name}")

    @commands.command(aliases=['colors', 'color', 'Color', 'Colour', 'colours', 'COLOR', 'COLOUR'])
    async def colour(self, ctx, colour, member = None):
        member = ctx.message.author if not member else member
        role = get(ctx.guild.roles, name=colour)

        if not role:
            if colour in self.colours:
                role = await ctx.guild.create_role(name=colour, colour=discord.Colour(self.colours[colour]))
                await ctx.send(f'Role {role.name} was created')
            else:
                await ctx.send('That colour was not found')
                return

        await member.add_roles(role)
        await ctx.send(f'Assigned role {role.name} to {member.display_name}')

    @commands.command(aliases=['nocolour', 'nocolor', 'removecolour', 'removecolor', 'Nocolour', 'Nocolor', 'Removecolour', 'Removecolor'])
    async def removecol(self, ctx, colour, member = None):
        member = ctx.message.author if not member else member
        role = get(ctx.guild.roles, name=colour)

        for colour in self.colours:
            get(ctx.guild.roles, name=colour)
        else:
            await member.remove_roles(role)
            await ctx.send(f'Removed {role.name} from {member.display_name}')
 

    @commands.command()
    async def col(self, ctx):
        embed = discord.Embed(title="Colours", description="", color=0x8634eb)
        for colour in self.colours:
            embed.add_field(name=colour, value=discord.Colour(self.colours[colour]))
            embed.set_footer(text="chad the god helped :)")
        await ctx.send(embed=embed)

def setup(client): 
    client.add_cog(Welcomeroles(client))