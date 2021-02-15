import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("start to" + client.user.name)
    await client.change_presence(activity=discord.Game(name='Destiny', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('hi'):
        await client.send_message(message.channel, "hello")



ClientCode = os.environ['BOT_TOKEN']
client.run(ClientCode)
