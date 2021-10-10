#if your account gets banned or disable then I am not the responsible for it. Because slefbot is illeagal
#also thanks to nekobot for the api:)
import discord
import random
import colorama
from colorama import Fore
import json
import requests
import numpy
import string
import os
from discord.ext import commands
from asyncio import sleep

with open("config.json","r") as r:
  config = json.load(r)

token = config.get("token")
command_prefix = config.get("prefix")

def clear():
  os.system("cls")
def nitro():
   code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
   return f'https://discord.gift/{code}'
def run():
    token = config.get('token')
    try:
        saad.run(token, bot=False, reconnect=True)
        os.system(f'title (Saad Selfbot)')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')
def StartPrinting():
  print(f"""
    {Fore.CYAN} ░██████╗░█████╗░░█████╗░██████╗░{Fore.CYAN}
    {Fore.CYAN} ██╔════╝██╔══██╗██╔══██╗██╔══██╗{Fore.CYAN}
    {Fore.CYAN} ╚█████╗░███████║███████║██║░░██║{Fore.CYAN}
    {Fore.CYAN} ░╚═══██╗██╔══██║██╔══██║██║░░██║{Fore.CYAN}
    {Fore.CYAN} ██████╔╝██║░░██║██║░░██║██████╔╝{Fore.CYAN}
    {Fore.CYAN} ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░{Fore.CYAN}
    {Fore.GREEN}Logged in as: {saad.user.name}#{saad.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{saad.user.id}
    {Fore.CYAN}Guilds: {Fore.GREEN}{len(saad.guilds)}
    {Fore.CYAN}Prefix: {Fore.GREEN}{saad.command_prefix}
  """)
   
colorama.init()
saad = commands.Bot(command_prefix=command_prefix,self_bot=True)
saad.remove_command("help")
@saad.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=5)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=5)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=5)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=5)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=5)

@saad.event
async def on_connect():
  StartPrinting()

@saad.command(aliases=["Nitro","NITRO"])
async def nitro(ctx):
  await ctx.message.delete()
  await ctx.send(nitro())

@saad.command(aliases=["Nuke","NUKE"])
async def nuke(ctx):
  members = ctx.guild.members
  guild = ctx.guild
  name = "Saad-selfbot"
  await ctx.message.delete()
  for channel in list(ctx.guild.channels):
    try:
      await channel.delete()
      print(f"{Fore.YELLOW}{channel.name} deleted"+Fore.GREEN)
    except:
      pass
  for i in range(500):
    try:
      await guild.create_text_channel(name=name)
    except:
      pass
  for member in members:
    try:
      await member.ban()
      print(f"{Fore.GREEN}{member} was banned "+Fore.GREEN)
    except:
      pass

@saad.command(aliases=["MassChannel","MASSCHANNEL","Masschannel"])
async def masschannel(ctx,num : int, *, name):
  guild = ctx.guild
  if name is None:
    name = "saad-selfbot"
  for i in range(num):
    try:
      await guild.create_text_channel(name=name)
      print(f"{Fore.GREEN} Created.")
    except:
      pass

@saad.command(aliases=["MassBan","MASSBAN","Massban"])
async def massban(ctx):
  await ctx.message.delete()
  for m in ctx.guild.members:
    try:
      await m.ban()
      print(f"{Fore.GREEN}{m} was banned "+Fore.GREEN)
    except:
      pass

@saad.command(aliases=["MASSDEL","Massdel"])
async def massdel(ctx):
  guild = ctx.guild
  for channel in list(guild.channels):
    try:
      await channel.delete()
      print(Fore.YELLOW+f"{channel.name} deleted")
    except:
      pass

@saad.command(aliases=["MassKick","MASSKICK","Masskick"])
async def masskick(ctx):
  for m in ctx.guild.members:
    try:
      await m.kick()
      print(f"{Fore.GREEN}{m} was kicked "+Fore.GREEN)
    except:
      pass

@saad.command(aliases=["Cls","CLS"])
async def cls(ctx):
  clear()
  await ctx.message.delete()
  await ctx.send("cls")

@saad.command(aliases=["Membercount","MEMBERCOUNT"])
async def membercount(ctx):
  guild = ctx.guild
  embed = discord.Embed(description=guild.member_count,color=discord.Color.red())
  embed.set_author(name="Membercount",icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed) 

@saad.command(aliases=["Boobs","BOOBS"])
async def boobs(ctx):
  await ctx.message.delete()
  get = requests.get("https://nekobot.xyz/api/image?type=boobs").json()
  await ctx.send(get["message"])

@saad.command(aliases=["Porn","PORN"])
async def porn(ctx):
  await ctx.message.delete()
  get = requests.get("https://nekobot.xyz/api/image?type=pgif").json()
  await ctx.send(get["message"])

@saad.command(aliases=["4k","4K","Nudes","NUDES"])
async def nudes(ctx):
  await ctx.message.delete()
  get = requests.get("https://nekobot.xyz/api/image?type=4k").json()
  await ctx.send(get["message"])

@saad.command(aliases=["Anal","ANAL"])
async def anal(ctx):
  await ctx.message.delete()
  get = requests.get("https://nekobot.xyz/api/image?type=anal").json()
  await ctx.send(get["message"])

@saad.group(invoke_without_command = True,aliases=["Help","HELP"])
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Saad-Selfbot",color = discord.Color.red())
  embed.add_field(name="Nsfw",value=f"{saad.command_prefix}help nsfw")
  embed.add_field(name="Nuke",value=f"{saad.command_prefix}help nuke")
  await ctx.send(embed=embed)
@help.command(aliases=["Nsfw","NSFW"])
async def nsfw(ctx):
  embed = discord.Embed(color = discord.Color.red())
  embed.add_field(name="Nsfw",value="**anal :** random anal pics\n**nudes** : random pictures\n**porn :** gifs\n**boobs :** random boobs pictures")
  await ctx.send(embed=embed)

@help.command(aliases=["Nuke","NUKE"])
async def nuke(ctx):
  embed = discord.Embed(color = discord.Color.red())
  embed.add_field(name="Nuke",value="**massban :** bans members\n**masskick :** kicks members\n**nuke :** destroy the server\n**masschannel : creates channels**")
  await ctx.send(embed=embed)
  
run()
