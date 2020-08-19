import discord
import random

bot_invocation_str = '/roll'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    print('We have joined server', guild)

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith(bot_invocation_str):
        tokens = message.content.split(' ')

        lower_bound = 1
        upper_bound = 100
        if len(tokens) >= 2: 
            upper_bound = int(tokens[1])
        
        if not upper_bound > 0:
            return

        roll = random.randint(lower_bound, upper_bound)
        
        msg = f'{message.author.mention} rolls {roll} ({lower_bound}-{upper_bound})'
        await message.channel.send(msg)


client.run('secret key')
