#!/usr/bin/env python
import requests
import discord
import os


public_ip = requests.get('http://ip.42.pl/raw').text
with open('network.txt', 'r') as f:
    lines = f.readlines()
    port = lines[1]
    stored_ip = lines[0]

global full_address

if stored_ip == public_ip:
    full_address = stored_ip + ':' + port
    print('if statement')
    print(full_address)
else:
    full_address = public_ip + ':' + port
    lines[0] = public_ip
    with open('network.txt', "w") as f:
        f.write('\n'.join(lines) + '\n')


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents = intents)

token = 'My Token'

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(Channel ID)
    await channel.send(full_address)
    exit()

client.run(token)
