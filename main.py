import discord
import os
from pprint import pprint
from keep_alive import keep_alive
from ArcanasData import ArcanasData

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    try:
        if message.author != client.user:
            tokens = message.content.split()
            response = [] 
            if tokens[0] == "!fusion":
                TargetArcana = tokens[1]
                Combos = ArcanasData[TargetArcana]
                for combo in Combos:
                    response.append(f"{combo[0]} and {combo[1]}")
                await message.channel.send("\n".join(response))
    except:
        pass

        #await client.send_message(message.channel, message.content[::-1])


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
