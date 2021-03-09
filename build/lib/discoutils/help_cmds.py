import discord
from discord.ext import commands

class MinimalEmbedHelp(commands.MinimalHelpCommand):
  def __init__(self, **options):
    self.options = options
    super().__init__(**options)
    
  async def send_pages(self):
    channel = self.get_destination()
    embed = discord.Embed(description=self.paginator.pages[0])
    await channel.send(embed=embed)

class DefaultEmbedHelp(commands.DefaultHelpCommand):
  def __init__(self, **options):
    self.options = options
    super().__init__(**options)
    
  async def send_pages(self):
    channel = self.get_destination()
    embed = discord.Embed(description=self.paginator.pages[0])
    await channel.send(embed=embed)
