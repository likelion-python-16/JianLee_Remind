from scraper import MusinsaAPI
from dotenv import load_dotenv
import os
import discord



load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def build_message(item):
    embed = discord.Embed(type="rich", title=item["goodsName"], url=["linkUrl"])
    embed.set_thumbnail(url=item["imageUrl"])
    embed.description = item["brandName"]
    embed.add_field(name="정가", value=item["normalPrice"], inline=True)
    embed.add_field("할인가", value=item["price"], inline=True)

    return embed