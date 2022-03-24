import os
import discord

client = discord.Client()

""" 
Speaker notes:
TODO: Talk about python decorators.
TODO: Events and the on_ready function.
TODO: Async function?
TODO: Bot as a user.
"""


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
