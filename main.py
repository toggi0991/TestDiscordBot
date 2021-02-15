import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Destiny 2', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('hi'):
        await message.channel.send('hello')



ClientCode = os.environ['BOT_TOKEN']
client.run(ClientCode)
