import os
import discord
import json

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
    # print(f"User:{message.author} Message:{message.content}")

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
