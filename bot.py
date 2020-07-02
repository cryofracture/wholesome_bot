#bot.py
import os
import discord
from dotenv import load_dotenv
import random
import praw

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
reddit = praw.Reddit('wholesome_porn_bot')

food_posts = []
earth_posts = []
library_posts = []
aerial_posts = []

for submission in reddit.subreddit('foodporn+culinaryporn+dessertporn').hot(limit=50):
    food_posts.append(submission.url)

for submission in reddit.subreddit('earthporn+waterporn+skyporn+seaporn').hot(limit=50):
    earth_posts.append(submission.url)

for submission in reddit.subreddit('libraryporn+bookporn').hot(limit=50):
    library_posts.append(submission.url)

for submission in reddit.subreddit('aerialporn').hot(limit=50):
    aerial_posts.append(submission.url)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return 


    if message.content == '!foodporn':
        response = random.choice(food_posts)
        await message.channel.send(f'Wholesome food porn incoming!\n{response}')

    if message.content == '!earthporn':
        response = random.choice(earth_posts)
        await message.channel.send(f'Wholesome earth porn incoming!\n{response}')

    if message.content == '!libraryporn':
        response = random.choice(library_posts)
        await message.channel.send(f'Wholesome library porn incoming!\n{response}')

    if message.content == '!aerialporn':
        response = random.choice(aerial_posts)
        await message.channel.send(f'Wholesome aerial porn incoming!\n{response}')

client.run(TOKEN)