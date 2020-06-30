#!/usr/bin/python
import discord
from discord.ext import commands
from discord import Member
from discord.utils import get

class Kickbanmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['KICK'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(aliases=['Ban'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(aliases=['Unban'])
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

    @commands.command(aliases=['Mute'])
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

    @commands.command(aliases=['Unmute'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("Please specify a member")
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f'unmuted {member.mention}')

def setup(client):
    client.add_cog(Kickbanmute(client))
