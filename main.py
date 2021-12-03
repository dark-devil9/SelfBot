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
import smtplib
from discord.ext import commands
from asyncio import sleep

class SAAD():
  __version__ = 1.5
  __lines__ = 258
       
with open("config.json","r") as r:
   config = json.load(r)

token = config.get("token")
command_prefix = config.get("prefix")

def mailspam():
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    username = input(f'Gmail: ')
    password = input(f'Gmail Password: ')
    try:
         mail.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
        return  
    target = input(f'Target Gmail: ')
    message = input(f'Message to send: ')
    counter = eval(input(f'Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        mail.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass
def clear():
   os.system("cls")
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
    {Fore.CYAN}Version: {Fore.GREEN}1.5
  """+Fore.RESET)
clear()
colorama.init()
intents = discord.Intents.all()
saad = commands.Bot(
command_prefix = command_prefix,
self_bot = True,
intents = intents,
status = discord.Status.idle
)
saad.remove_command("help")
@saad.event
async def on_command_error(error):
     error_str = str(error)
     error = getattr(error, 'original', error)
     if isinstance(error, commands.CommandNotFound):
        print(f'{Fore.RED}[ERROR]:{Fore.YELLOW}Command not found')
     elif isinstance(error, commands.CheckFailure):
         print(f'{Fore.RED}[ERROR]:{Fore.YELLOW} You\'re missing permission to execute this command')
     elif isinstance(error, commands.MissingRequiredArgument):
         print(f"{Fore.RED}[ERROR]:{Fore.YELLOW} Missing arguments: {error}")
     elif isinstance(error, numpy.AxisError):
         print(f'{Fore.YELLOW}Invalid Image')
     elif isinstance(error, discord.errors.Forbidden):
         print(f"{Fore.RED}[ERROR]:{Fore.YELLOW} 404 Forbidden Access: {error}")
     elif "Cannot send an empty message" in error_str:
         print(f'{Fore.RED}[ERROR]:{Fore.YELLOW} Message contents cannot be null')
     else:
         print(f'{Fore.RED}[ERROR]:{Fore.YELLOW} {error_str}')

@saad.event
async def on_connect():
   StartPrinting()

@saad.command(aliases=["Nitro","NITRO"])
async def nitro(ctx):
   await ctx.message.delete()
   code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
   await ctx.send(f'https://discord.gift/{code}')

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

@saad.command(aliases=["Frog","FROG"])
async def frog(ctx):
   await ctx.message.delete()
   r = requests.get("https://api.animality.xyz/img/frog").json()
   await ctx.send(r["link"])

@saad.command(aliases=["Cat","CAT"])
async def cat(ctx):
   await ctx.message.delete()
   r = requests.get("https://api.animality.xyz/img/cat").json()
   await ctx.send(r["link"])

@saad.command(aliases=["Dog","DOG"])
async def dog(ctx):
   await ctx.message.delete()
   r = requests.get("https://api.animality.xyz/img/dog").json()
   await ctx.send(r["link"])

@saad.command(aliases=["PPsize","Ppsize","ppSize","ppSIZE"])
async def ppsize(ctx,member: discord.Member = None):
   if member == None:
     member = ctx.author
   await ctx.message.delete()
   sizes = ["8=D","8==D","8===D","8====D","8======D","8=========D","8==============D","8===========D","8=======================D"]
   p = random.choice(sizes)
   em = discord.Embed(description=p,color = discord.Color.red())
   em.set_author(name=f"{member.name}'s dick size")
   await ctx.send(embed=em)

@saad.command(aliases=["Kiss","KISS"])
async def kiss(ctx,member : discord.Member):
   l = ["https://images-ext-1.discordapp.net/external/x6lRNcsJXFbajNwazdNEPejeStJsYUkSXcmB0KeOSsY/https/images-ext-1.discordapp.net/external/Gl8911h89Tv6k_12U3G6XOtFbbJQvpGDeb4AxSu2HEE/https/cdn.weeb.sh/images/BkUJNec1M.gif","https://images-ext-2.discordapp.net/external/ThBYZHONG_1x-dRf3A-6KbOEfuPCW1FN088LYg8S1yk/https/cdn.weeb.sh/images/HkZyXs3A-.gif"]
   links = random.choice(l)
   embed = discord.Embed(color = discord.Color.red())
   embed.set_author(name=f"{saad.user.name} kissed {member.name}")
   embed.set_image(url=links)
   await ctx.send(embed=embed)

@saad.command(aliases=["Kick","KICK"])
async def kick(ctx,member : discord.Member):
   await ctx.message.delete()
   await member.kick()
   print(f"{Fore.GREEN} {member} kicked!!")
  
@saad.command(aliases=["Ban","BAN"])
async def ban(ctx,member : discord.Member):
  await ctx.message.delete()
  await member.ban()
  print(f"{Fore.GREEN} {member} banned!!")

@saad.command(aliases=["Massdm","MASSdm","massDm","massDM","MASSDM"])
async def massdm(ctx , *, msg):
  for f in saad.user.friends:
    try:
      await f.send(msg)
      print(f"{Fore.RED}Message sent to {Fore.YELLOW}{f}")
    except:
      pass
  await ctx.send("Done!")

@saad.command(aliases=["Leave","LEAVE"])
async def leave(ctx):
  await ctx.message.delete()
  for guild in saad.guilds:
    try:
      await guild.leave()
      print(f"{Fore.RED}Left the guild {Fore.YELLOW}({guild.name})")
    except:
      pass

@saad.command(aliases=["Guilds","GUILDS"])
async def guilds(ctx):
  with open("txt/guilds.txt","w") as g:
    for i in saad.guilds:
      try:
        g.write(f"Guild owner : {i.owner} , Guild membercount : {i.member_count} , Guild id : {i.id}\n")
      except:
        pass
    g.close()
    await ctx.send("Check guilds.txt file")

@saad.command(aliases=["Friends","FRIENDS"])
async def friends(ctx):
  with open("txt/friends.txt","w") as f:
    for i in saad.user.friends:
      try:
        f.write(f"Name : {i} , id : {i.id}\n")
      except:
        pass
    f.close()
    await ctx.send("check friends.txt file")

@saad.command(aliases=["BombGmail","BOMBGMAIL","Bombgmail","BOMBgmail","bombGMAIL"])
async def bombgmail(ctx):
  await ctx.message.delete()
  await ctx.send("Check the python file output!",delete_after = 3)
  mailspam()

@saad.group(invoke_without_command = True,aliases=["Help","HELP"])
async def help(ctx):
   await ctx.message.delete()
   embed = discord.Embed(title="Saad-Selfbot",color = discord.Color.red())
   embed.add_field(name="Nsfw",value=f"{saad.command_prefix}help nsfw")
   embed.add_field(name="Nuke",value=f"{saad.command_prefix}help nuke")
   embed.add_field(name="Fun",value=f"{saad.command_prefix}help fun")
   await ctx.send(embed=embed)
 
@help.command(aliases=["Nsfw","NSFW"])
async def nsfw(ctx):
  embed = discord.Embed(color = discord.Color.red())
  embed.add_field(name="Nsfw",value="**anal :** random anal pics\n**nudes** : random pictures\n**porn :** gifs\n**boobs :** random boobs pictures")
  await ctx.send(embed=embed)

@help.command(aliases=["Nuke","NUKE"]) 
async def nuke(ctx):
 embed = discord.Embed(color = discord.Color.red())
 embed.add_field(name="Nuke",value="**massban :** bans members\n**masskick :** kicks members\n**nuke :** destroy the server\n**masschannel :** creates channels")
 await ctx.send(embed=embed)

@help.command(aliases=["Fun","FUN"])
async def fun(ctx):
  em = discord.Embed(color = discord.Color.red())
  em.add_field(name="Fun",value="**cat :** random cats pictures\n**frog : ** random frog pictures\n**dog :** random dogs pictures\n**Bombgmail :** spam ur friend's gmail\n**Frog :** random frog pictures\n**kiss :** kiss someone\n**ppsize :** ur dick size ;)\n**massdm :** massdm ur friends\n**kick :** kick someone from the guild\n**ban :** ban someone from the guild\n**leave :** mass leave servers\n**friends :** Your friend list\n**Guilds :** servers that you are in")
  await ctx.send(embed=em)

if __name__ == "__main__":
 run()
