#!/usr/bin/python
import discord
import datetime
import pytz
from pytz import timezone
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands, tasks

class Embeds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Help','HELP'], pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="BOT Commands", description="Random commands", color=0xF8F8FF)
        embed.add_field(name=".50", value=".50 am i cool")
        embed.add_field(name=".mute", value=".mute @user")
        embed.add_field(name=".unmute", value=".unmute @user")
        embed.add_field(name=".clear", value=".clear 5")
        embed.add_field(name=".kick", value=".kick @user")
        embed.add_field(name=".ban", value=".ban @user")
        embed.add_field(name=".unban", value=".unban @user")
        embed.add_field(name=".info", value=".info @user")
        embed.add_field(name=".avatar", value=".avatar @user")
        embed.add_field(name=".level", value=".level @user")
        embed.add_field(name=".leaderboards", value=".ld")
        embed.add_field(name=".time", value="timezones i've added")
        embed.add_field(name='.github', value="Ai code")
        embed.add_field(name='.say', value=".say Hey!")
        await ctx.send(embed=embed)

    @commands.command(aliases=['Info', 'INFO'])
    async def info(self, ctx, member_arg : discord.Member = None):
        member = ctx.author if not member_arg else member_arg
        roles = [role for role in member.roles]
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="∘Discord ID:", value=f"***{ctx.author.id}***")
        embed.add_field(name="∘Status:", value=member.status, inline=False)
        embed.add_field(inline=False ,name=f"∘Roles: ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(inline=False ,name="∘Guild Join Date:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(inline=False ,name="∘Account Creation:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        await ctx.send(content=None, embed=embed)

    @commands.command(aliases=['Avatar', 'AVATAR'])
    async def avatar(self, ctx, member_arg : discord.Member = None):
        member = ctx.author if not member_arg else member_arg
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url=member.avatar_url)
        await ctx.send(content=None, embed=embed)

    @commands.command()
    async def time(self, ctx):
        embed = discord.Embed(color=0xeb3434, timestamp=datetime.datetime.utcnow())
        embed.add_field(name=".timeUTC", value='UTC time') # Current time in UTC
        embed.add_field(name=".timeBST", value='British Summer Time') # Convert to British time zone
        embed.add_field(name=".timeEST", value='Eastern Standard time') # Convert to Eastern time zone
        embed.add_field(name="timeCST", value='Central Standard Time') # Convert to Central time zone
        embed.add_field(name=".timePDT", value='Pacific Daylight Time') # Convert to Pacific time zone
        embed.add_field(name=".timeBRT", value='Brasilia Standard Time') # Convert to Brazil time zone
        embed.add_field(name=".timeCDT", value='Central Daylight Time') # Convert to Central Daylight Time zone
        embed.add_field(name=".timeGTM", value='Guatemala Time Zone') # Convert to Guatemala Time zone
        embed.add_field(name=".timeEDT", value='Eastern Daylight Time Zone') # Convert to Eastern Daylight Time zone
        embed.add_field(name=".timeJP", value='Japan Standard Time') # Convert to Japan Standard Time zone
        embed.add_field(name=".timeSG", value='Convert to Singapore Standard Time') # Convert to Singapore Standard Time zone
        embed.add_field(name=".timeCN", value='Canada/Eastern') # Convert to Canada/Eastern Time zone
        await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Embeds(client))
