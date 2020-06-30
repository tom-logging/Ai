import discord
import datetime
from datetime import timezone, tzinfo, timedelta
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands, tasks

class Embeds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Blank1'], pass_context=True)
    async def blank1(self, ctx):
        embed = discord.Embed(title="TITLE", description="DESCRIPTION", color=0xeb7434)
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        await ctx.send(embed=embed)

    @commands.command(aliases=['BLANK2'], pass_context=True)
    async def blank2(self, ctx):
        embed = discord.Embed(title="TITLE", description="DESCRIPTION", color=0xeb7434)
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        await ctx.send(embed=embed)

    @commands.command(aliases=['Blank3'])
    async def blank3(self, ctx):
        embed = discord.Embed(title="TITLE", description="DESCRIPTION", color=0xeb7434)
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        embed.add_field(name="Name", value="VALUE")
        await ctx.send(embed=embed)

    @commands.command(aliases=['Info'])
    async def info(self, ctx, member_arg : discord.Member = None):
        member = ctx.author if not member_arg else member_arg
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)
        embed.add_field(name="Joined server at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role: ", value=member.top_role.mention)
        embed.add_field(name="Status", value=member.status)
        embed.add_field(name="Bot?", value=member.bot)
        embed.set_footer(text=f"Requested by: {ctx.author.name}")
        await ctx.send(content=None, embed=embed)

    @commands.command(aliases=['Avatar'])
    async def avatar(self, ctx, member_arg : discord.Member = None):
        member = ctx.author if not member_arg else member_arg
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested by: {ctx.author.name}")
        await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Embeds(client))
