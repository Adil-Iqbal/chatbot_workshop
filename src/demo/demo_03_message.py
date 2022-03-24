import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


""" 
Speaker notes:
Goal: Echo each message to the chatroom
TODO: Talk about message param.
TODO: Print chat in terminal.
TODO: Echo chat message.
TODO: Echo chat message properly.
"""


@client.event
async def on_message(message):
    pass


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
