from discord.ext import commands
import discord
import time as t
import asyncio
import datetime
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected, logged in as {bot.user}, ID {bot.user.id}')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="Ban Bot"))
    time = datetime.datetime.now
    while True:
        guild = bot.get_guild(ID) # manual guild id
        channel= guild.get_channel(ID) # manual channel id
        if time().hour == 23 and time().minute == 59:
            memberlist = []
            fulldata = []
            async for guild in bot.fetch_guilds(limit=None):
                async for i in guild.fetch_members(limit=None):
                    if i.bot == False:
                        memberlist.append(i.name + "#" + i.discriminator)
                        fulldata.append(i)
                rannum = random.randint(0, len(memberlist) - 1)
                ranmember = memberlist[rannum]
                ranmemdata = fulldata[rannum]
                print("Ban time! Banning " + ranmember)
                await channel.send("Ban time! Banning " + ranmember)
                await ranmemdata.send(content=f"You got banned from `{guild.name}`!")
                await ranmemdata.ban(reason="Banned by BanBot")
        await asyncio.sleep(60)


bot.run('TOKEN')
