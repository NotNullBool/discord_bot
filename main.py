import discord
from discord import app_commands
import json

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="ping the bot!", guild=discord.Object(id=1004855799044120699))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1004855799044120699))
    print(f"Logged in as {client.user}")

#load token from json
token = {"token": ""}

try:
    with open("token.json","r") as fp:
        token = json.load(fp)
except Exception as e:
    with open("token.json", "w+") as fp:
        json.dump(token, fp)
    print("Please provide token in token.json!")
    raise

client.run(token["token"])
