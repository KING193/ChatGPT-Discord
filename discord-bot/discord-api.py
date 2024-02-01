from dotenv import load_dotenv
import discord
import os

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as:", self.users)

    async def on_message(self, message):
        print(message.content)