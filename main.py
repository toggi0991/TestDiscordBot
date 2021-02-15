import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("start to" + client.user.name)
    await client.change_presence(activity=discord.Game(name='Destiny 2', type=1))

client.run('NjcxMjcyMzYwMzMwMDAyNDUy.Xi6hGg.QZc9DGlynhr-0e9yZgXtwtE5d1Q')
