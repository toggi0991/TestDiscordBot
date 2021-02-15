import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("start to" + client.user.name)
    await client.change_presence(activity=discord.Game(name='Destiny 2', type=1))


ClientCode == os.environ["BOT_TOKEN"]
client.run(ClientCode)
