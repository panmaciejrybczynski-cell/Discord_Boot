import discord
from password import gen_pass
from discord.ext import commands
import mytoken

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

bot.run(mytoken.TOKEN)