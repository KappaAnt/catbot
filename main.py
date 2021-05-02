import discord
import os
from discord.ext import commands
from api1 import CatPic
from api2 import CatFact
from api3 import CatGif

def Command():
    client = commands.Bot(command_prefix = '.')
    discID = 751548629004582935
    channel = client.get_channel(discID)
    
    @client.event
    async def on_ready():
        print("\nBot is ready")

    @client.event
    async def on_member_join(member):
        print(f" {member} has joined the server.")
        
    @client.event
    async def on_member_remove(member):
        print(f" {member} has left the server.")


    @client.command(aliases=["ping","Cat","CAT"])
    async def cat(ctx):
        cat_pic = CatPic()
        cat_pic.get()
        cat_pic.useData()
        cat_fact = CatFact()
        cat_fact.get()
        meow = cat_fact.fact_json['fact']
        await ctx.send(file=discord.File('cat_pic1.jpg'))
        await ctx.send("CAT FACT: " + meow)
        #with open('cat_pic1.jpg', 'rb') as f:
            #picture = discord.File(f)
            #await channel.send("Picture")
    #async def on_message(message):
        #if message.content.startswith('.cat'):
            #await channel.send(file=discord.File('cat_pic1.jpg'))
            #await channel.send("Hello")
        #now we have to reset the pic and fact
        
    @client.command(aliases=["catgif","CatGif","cgif","CGIF","pur","PUR"])
    async def cat(ctx):
        cat_gif = CatGif()
        cat_gif.get()
        cat_gif.useData()
        await ctx.send(file=discord.File('cat_gif.gif'))
        
    client.run(os.environ["DISCORD_TOKEN"])
    
    
def main():
  
    Command()
    
main()

    
    
