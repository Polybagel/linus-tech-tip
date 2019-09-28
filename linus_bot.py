import discord
from discord.ext import commands
import random

techtip_starts = ['if you unplug ','when you break ','drop ','yell at ','stomp on ','yell bruh as loud as you can to ','spend lots of money on ']
techtip_middles = ['your graphics card ','your ram ','your life support ','your phone ','your computer ','the gamer box ','the bruh machine ','the door ','everything that is expensive']
techtip_ends = ['and only exclusive to you','it will fix it','it will make you live forever','it will make your ram go fast like sonic the blue hedgehog','nothing will happen at all','i will say good job',
                'you will die','you wont die','your graphics card will explode','your processor will scream in agony','i will not be happy','your hard drive will crumple into little bits',
                'your computer will explode','fire will go everywhere','you will get a virus','you will not get a virus','i will give you a high five','nvidia will give you a free 1080ti',
                'a quantum computer will show up on your doorstep','you should run']

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Ready to give tech tips to fellow gamers")

@client.command()
async def tech_tip(ctx):
    await ctx.send(random.choice(techtip_starts)+""+random.choice(techtip_middles)+""+random.choice(techtip_ends))

client.run('NjI3MzM0NjE2MDY3NDczNDE4.XY7JGQ.o4JtQSWunLHireLhptp6CQ1yMac')
