import discord
from discord.ext import commands
import random
from time import sleep
import os
import sys
import requests as r
from youtubesearchpython import VideosSearch
from pytube import *
import base64
import json

class CustomHelpCommand(commands.DefaultHelpCommand):
    async def send_bot_help(self, mapping):
        # Customize the bot help message here
        bot = self.context.bot
        help_embed = discord.Embed(
            title=f"Need help ?",
            description="Commands prefix : !\nhelp : displays this command\nk (admin use) : kicks users, usage : !k <mention> <reason (optional)>\nb (admin use) : ban users, usage : !b <mention> <reason (optional)>\nytdown : downloads yt vids, usage : !ytdown <youtube url> <vid(for mp4) or song(for mp3)>\nclear (admin use) : clears messages, usage : !clear <amount>\nping : sends bot latency in miliseconds, usage : !ping\npat : pats me :3, usage : !pat\nhi : wave back to you !, usage : !hi",
            color=discord.Color.pink(),
        )

        for cog, commands in mapping.items():
            if cog:
                cog_name = cog.qualified_name
                command_signatures = [self.get_command_signature(c) for c in commands]
                if command_signatures:
                    help_embed.add_field(name=cog_name, value='\n'.join(command_signatures), inline=False)

        await self.get_destination().send(embed=help_embed)


token = "MTE4MzE3NTYzMzUzMTA1NjIzOQ.GOPMQN.YG2rmYSw-OZiI1Fg8HWftStRzgKB-px9GfT_Us"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', help_command=CustomHelpCommand(), intents=intents)

    

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with 9z3cm'))
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if f'{bot.user.mention}' in message.content and message.author.id == 1084599590231224425:
        await message.channel.send(r.get('https://nekos.best/api/v2/blush').json()['results'][0]['url'])
    await bot.process_commands(message)
@bot.command()
@commands.has_permissions(kick_members=True)
async def k(ctx, member:discord.Member,*,reason=None):
    if reason == None:
        reason = 'بس جي'
    await ctx.guild.kick(member)
    await ctx.send(f'تم طرد {member.mention} بسبة : {reason} ')
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def b(ctx, member:discord.Member,*,reason=None):
    if reason == None:
        reason = 'بس جي'
    await ctx.guild.ban(member)
    await ctx.send(f'تم تبنيد الحيوان {member.mention} بسبة : {reason} ')
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,num:int):
    await ctx.channel.purge(limit=num)
    await ctx.send('تم التنظيف بيبي')
    sleep(2)
    await ctx.channel.purge(limit=1)
    
@bot.command()
async def flip(ctx):
    coin = ['دلة','درهم']
    sel = coin[random.randint(0,1)]
    await ctx.send(sel)
    
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    await ctx.send(f"البنق {latency} ms")

@bot.command()
async def hi(ctx):
    await ctx.send(r.get('https://api.waifu.pics/sfw/wave').json()['url'])
    
@bot.command()
async def pat(ctx):
    await ctx.send(r.get('https://api.waifu.pics/sfw/pat').json()['url'])

@bot.command()
async def ytdown(ctx, search:str,type:str):
    if type == 'song':
        YouTube(search).streams.first().download(filename='song.mp3')
        with open('song.mp3', 'rb') as file:
         await ctx.send(file=discord.File(file))
    elif type == 'vid':
        YouTube(search).streams.first().download(filename='video.mp4')
        with open('video.mp4', 'rb') as file:
            await ctx.send(file=discord.File(file))
@bot.command()
async def m(ctx):
    if ctx.author.id == 1084599590231224425:
        url = 'https://api.waifu.im/search?included_tags=milf'

        headers = {
        'Accept-Version': 'v5',
        'Authorization': 'Bearer qOwb5xud29WpVWwj8zHeschF7Rq9E1RP5rcC5WWJqDw7ggWAwGkBxxQ2beLfRQJ5PZKfm7UvScjP9g5gQWKMRu8kDvBsdTlvCf45_NlUGbp92fhWQh0x8du7wyVB0bg341x32Wr6zq3u7dyUD0f1QEVADhTXB_rRa-Nvil5JRyI',
          }
        
        response = r.get(url, headers=headers)
        await ctx.send(response.json()['images'][0]['url'])

 
@bot.command()
async def restart(ctx):
    restart_bot()

bot.run(token)
