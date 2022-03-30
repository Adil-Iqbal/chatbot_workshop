import os
import discord


client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    # Ignore bot messages.
    if message.author == client.user:
        return

    # Ignore messages that do not start with the prefix.
    if not message.content.startswith("!"):
        return

    print(message.content)
    # -> "!add 2 3"

    content = message.content[1:].split(" ")
    # -> ['add', '2', '3']

    if len(content) < 3:
        # Error: incorrect number of args
        await message.channel.send("I don't understand.")
        return

    # Extract values from content
    command = content[0]  # -> 'add'
    x = int(content[1])  # -> 2
    y = int(content[2])  # -> 3

    # Execute command
    if command == 'add':
        await message.channel.send(f"{x} + {y} = {x + y}")

    elif command == 'sub':
        await message.channel.send(f"{x} - {y} = {x - y}")

    # TODO: Talk about factorial command.

    else:
        # Error: unsupported command
        await message.channel.send("I don't understand.")

    return


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
