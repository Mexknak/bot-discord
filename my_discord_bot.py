import sys
import discord

TOKEN = ''
f = open("token", "r")
TOKEN = f.read()
if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ping':
        await message.channel.send(f'Par contre tu te calmes tout de suite {message.author.display_name}!')
        return

    if message.content.lower() == 'pong':
        await message.channel.send(f'T\'es con ou quoi ? c\'est ping le bon mot {message.author.display_name}!')
        return

client.run(TOKEN)