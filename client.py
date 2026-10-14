import discord
import os
import random
from password import gen_pass
from discord.ext import commands
import mytoken
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_message_edit( before, after):
    await after.channel.send(f'wiadomość została edytowana z: {before.content}!')
    
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def song(ctx):
    await ctx.send("Never gona give you up, never gona let you down")

@bot.command()
async def calc(ctx, a = 1, op="+", b = 1):
    if op=="+":
        await ctx.send(f"wynik {a + b}")
    elif op=="-":
        await ctx.send(f"wynik {a - b}")
    elif op=="*":
            await ctx.send(f"wynik {a * b}")
    elif op=="/":
            await ctx.send(f"wynik {a / b}")
    else:
            await ctx.send(f"Co to jest '{op}'?")
          

@bot.command()
async def boo(ctx):
    await ctx.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!")


@bot.command()
async def mem(ctx):
    ings = os.listdir('images')
    img = random.choice(ings)
    with open(f'images/{img}', 'rb') as f:
                picture = discord.File(f)
    await ctx.send(file=picture)


def mem_godzina():
      teraz = datetime.datetime.now()
      if teraz.hour < 12:
        return 'images/rano'
      elif teraz.hour > 20:
        return 'images/wieczor'
      else:
        return 'images/poludnie'

@bot.command()
async def memV2(ctx): 
    sciezka = mem_godzina()
    ings = os.listdir(sciezka)
    img = random.choice(ings)
    with open(f'{sciezka}/{img}', 'rb') as f:
                picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(mytoken.TOKEN)
