import io
import os
import random
import requests
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f"Hello, my name is {client.user}")


@client.event
async def on_command_error(context, error):
    await context.send("I don't understand.")
    print(error)


eight_ball_choices = [
    "It is certain",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

rps_choices = [
    'rock',
    'paper',
    'scissors'
]


def validate_response(response):
    """Ensure response has returned properly."""
    if response.status_code != 200:
        raise Exception('Something wrong with third party API')


def get_random_person(gender):
    """Get a random person from another API."""
    response = requests.get(f"https://randomuser.me/api/?gender={gender}")
    validate_response(response)
    return response.json()['results'][0]


def get_image_file(image_url):
    """Get image from URL."""
    response = requests.get(image_url)
    validate_response(response)
    data = io.BytesIO(response.content)
    return discord.File(data, 'image.jpg')


# Add commands here!


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
