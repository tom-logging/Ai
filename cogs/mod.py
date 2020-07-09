#!/usr/bin/python
import discord
from discord.ext import commands
from discord import Member
from discord.utils import get

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['KICK', 'Kick'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to kick people")

    @commands.command(aliases=['Ban', 'BAN'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to ban people")

    @commands.command(aliases=['Unban', 'UNBAN'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to unban people")

    @commands.command(aliases=['Mute', 'MUTED'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("Please specify a member")
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f'Muted {member.mention}')
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to mute people")

    @commands.command(aliases=['Unmute', 'UNMUTE'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("Please specify a member")
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f'unmuted {member.mention}')
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to unmute people")

def setup(client):
    client.add_cog(mod(client))
