import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone

class Time(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['TIMEUTC', 'TimeUTC', 'timeutc'])
    async def timeUTC(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Current time in UTC
        now_utc = datetime.now(timezone('UTC'))
        await ctx.send (now_utc.strftime(date) + " (UTC)")

    @commands.command(aliases=['TIMEBST', 'TimeBST', 'timebst', 'UK', 'uk', 'Britian', 'britian'])
    async def timeBST(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to British time zone
        now_utc = datetime.now(timezone('UTC'))
        now_london = now_utc.astimezone(timezone('Europe/London'))
        await ctx.send (now_london.strftime(date) + " (British Summer Time)")


    @commands.command(aliases=['TIMEEST', 'TimeEST', 'timeest', 'florida', 'Florida'])
    async def timeEST(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Eastern time zone
        now_utc = datetime.now(timezone('UTC'))
        now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
        await ctx.send (now_canada_east.strftime(date) + "(Eastern Standard Time)")

    @commands.command(aliases=['TIMECST', 'TimeCST', 'timecst'])
    async def timeCST(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Central time zone
        now_utc = datetime.now(timezone('UTC'))
        now_central = now_utc.astimezone(timezone('US/Central'))
        await ctx.send (now_central.strftime(date) + " (Central Standard Time)")

    @commands.command(aliases=['TIMEPDT', 'TimePDT', 'timepdt', 'California', 'california'])
    async def timePDT(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Pacific time zone
        now_utc = datetime.now(timezone('UTC'))
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        await ctx.send (now_pacific.strftime(date) + " (Pacific Daylight Time)")

    @commands.command(aliases=['TIMEBRT', 'TimeBRT', 'timebrt', 'Brazi', 'brazil'])
    async def timeBRT(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Brazil time zone
        now_utc = datetime.now(timezone('UTC'))
        now_brasilia = now_utc.astimezone(timezone('Brazil/East'))
        await ctx.send (now_brasilia.strftime(date)+ " (Brasilia Standard Time)")

    @commands.command(aliases=['TIMECDT', 'TimeCDT', 'timecdt', 'Texas', 'texas'])
    async def timeCDT(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Central Daylight Time zone
        now_utc = datetime.now(timezone('UTC'))
        now_cdt = now_utc.astimezone(timezone('CST6CDT'))
        await ctx.send (now_cdt.strftime(date)+ " (Central Daylight Time)")
    
    @commands.command(aliases=['TIMEGTM', 'TimeGTM', 'timegtm', 'Gutemala', 'gutemala'])
    async def timeGTM(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Gutemala time zone
        now_utc = datetime.now(timezone('UTC'))
        now_guatemala = now_utc.astimezone(timezone('America/Guatemala'))
        await ctx.send (now_guatemala.strftime(date)+ " (Guatemala Time)")

    @commands.command(aliases=['TIMEEDT', 'TimeEDT', 'timeedt', 'ny', 'NY'])
    async def timeEDT(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Eastern Daylight Time zone
        now_utc = datetime.now(timezone('UTC'))
        now_edt = now_utc.astimezone(timezone('EST5EDT'))
        await ctx.send (now_edt.strftime(date)+ " (Eastern Daylight Time)")

    @commands.command(aliases=['TIMEJP', 'TimeJP', 'timejp', 'Tokyo', 'tokyo'])
    async def timeJP(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Japan Standard Time zone
        now_utc = datetime.now(timezone('UTC'))
        now_jp = now_utc.astimezone(timezone('Asia/Tokyo'))
        await ctx.send (now_jp.strftime(date)+ " (Japan Standard Time)")

    @commands.command(aliases=['TIMESG', 'TimeSG', 'timesg', 'singapore', 'Singapore'])
    async def timeSG(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Singapore Standard Time zone
        now_utc = datetime.now(timezone('UTC'))
        now_sig = now_utc.astimezone(timezone('Asia/Singapore'))
        await ctx.send (now_sig.strftime(date)+ " (Singapore Standard Time)")
    
    @commands.command(aliases=['TimeCN', 'TIMECN', 'timecn', 'Canada', 'canada'])
    async def timeCN(self, ctx):
        date = "%Y/%m/%d %I:%M:%S%p"

        # Convert to Canada/Eastern Time zone
        now_utc = datetime.now(timezone('UTC'))
        now_cn = now_utc.astimezone(timezone('Canada/Eastern'))
        await ctx.send (now_cn.strftime(date)+ " (Canada/Eastern)")

def setup(client):
    client.add_cog(Time(client))
