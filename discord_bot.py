import os

import discord
import dotenv


dotenv.load_dotenv()
discord_client = discord.Client(intents=discord.Intents.all())


@discord_client.event
async def on_message(message):
    bot_user = discord_client.user
    if message.author.id is not bot_user.id:
        await message.channel.send("Sup Elon Musk")


discord_client.run(os.environ["discord_secret_token"])
