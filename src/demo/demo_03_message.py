import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
  # Show message object.
  # print(message)
  
  # Show message content.
  # print(message.content)

  # send message
  # await message.channel.send(message.content)
  
  # Show infinite loop issue.
  if client.user == message.author: return
  await message.channel.send(message.content)


def main():
  BOT_TOKEN = os.getenv('BOT_TOKEN')
  client.run(BOT_TOKEN)


if __name__ == "__main__":
  main()