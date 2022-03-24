import os
import math
from discord.ext import commands

# Store commands extension in variable with '!' prefix.
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_command_error(context, error):
    await context.send("I don't understand.")
    print(error)


@client.command(name='add')
async def add(context, x, y):
    await context.send(f"{x} + {y} = {int(x) + int(y)}")


@client.command(name='sub')
async def sub(context, x, y):
    await context.send(f"{x} - {y} = {int(x) - int(y)}")


# TODO: Implement factorial command.


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
