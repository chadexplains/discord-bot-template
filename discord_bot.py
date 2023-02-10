import os
import discord
import dotenv

from airtable_client import AirtableClient
from command_handler import CommandHandler
from slash_command import SlashCommand

dotenv.load_dotenv()
airtable_api_key = os.environ["airtable_api_key"]
airtable_database_id = os.environ["airtable_database_id"]
discord_guild_id = int(os.environ["discord_guild_id"])

state = State(
    airtable_client=airtable_client,
    discord_client=discord_client
)
discord_client = discord.Client(intents=discord.Intents.all())
airtable_client = AirtableClient(api_key=airtable_api_key, base_id=airtable_database_id)
command_handler = CommandHandler(state=state)


def register_slash_command(slash_command_to_register: SlashCommand):                                                
    return discord_client.command_tree.command(
        name=slash_command_to_register.name(),
        description=slash_command_to_register.description(),
        guild=discord.Object(id=discord_guild_id),
    )
 
# ======================= #
# === Player commands === #
# ======================= #
@register_slash_command(SlashCommand(SlashCommand.train))
async def register_train_command(interaction: discord.Interaction):
    await interaction.response.defer()
    return await command_handler.train_command(interaction)

# ====================== #
# ===== Bot events ===== #
# ====================== #
@discord_client.event
async def on_message(message):
    bot_user = discord_client.user
    if message.author.id is not bot_user.id:
        await message.channel.send("Sup Elon Musk")


discord_client.run(os.environ["discord_secret_token"])
