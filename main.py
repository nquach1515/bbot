import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  messageCon = message.content
  msgArr = []
  if message.author == client.user:
    return

  # changes first letter to b
  msgArr = messageCon.split()

  for i in range(len(msgArr)):
    word = msgArr[i]
    wordSplit = []

    # splits word into array of letters
    wordSplit = list(word)
    # wordSplit[0] = 'B'
    if wordSplit[0] == '<':
      continue
    elif wordSplit[0].isupper():
      wordSplit[0] = 'B'
    else:
      wordSplit[0] = 'b'

    # joins word together after changed to b
    wordJoined = ''.join(wordSplit)
    msgArr[i] = wordJoined

  # rejoins word with replaced letter 
  msgString = ' '.join(msgArr)
    
  await message.channel.send(msgString)

keep_alive()
botToken = os.environ['TOKEN']
client.run(botToken)