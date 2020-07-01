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

posts = []
for submission in reddit.subreddit('foodporn').hot(limit=50):
    posts.append(submission.url)

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
        response = random.choice(posts)
        await message.channel.send(f'Wholesome food porn incoming!\n{response}')

client.run(TOKEN)