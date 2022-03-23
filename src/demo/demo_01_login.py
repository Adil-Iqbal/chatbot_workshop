import os
import discord

# Store all methods needed to use API in variable named client.
client = discord.Client()


def main():
    # Securely retrieve the bot's token from environment variables.
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    # Run the bot with all of its associated functions.
    client.run(BOT_TOKEN)


# See: https://tinyurl.com/4km4hf45
if __name__ == "__main__":
    main()