import discord
import os
from python_aternos import Client
import time

TOKEN = 'MTI1Mjg5MTE0NjE5MTkwMDY3NA.GB52ka.3tpZwX8DajZGt29cF0UpAsDcR1UkZbdMVT00xQ'

client = discord.Client()

aternos = Client('Moses3031', password='gyatgyatgyatgyat1234^*$$$$%^&&^^%$#@#@#$%ohiorizz')

atservers = aternos.servers

myserv = atservers[0]

@client.event
async def on_ready():
    print('we have logged in a {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?hello':
            await message.channel.send(f'Hello {username}!')
            return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?server_start':
          myserv.start()
          while True:
            ping = str(os.popen('mcstatus darkplaysmp.aternos.me status | grep description').read())
            if "offline" in ping:
              time.sleep(1)
            else:
              break
          await message.channel.send("server is now alive!!! you can join in 2-3 minutes by pasting ||darkplaysmp.aternos.me:43102|| in the server address.")
          return

    if message.channel.name == 'bot-cmnds':
        if user_message.lower() == '?server_stop':
          myserv.stop()
          await message.channel.send(f'server stopped')
          return

client.run(TOKEN)
