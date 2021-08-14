import discord
from discord.ext import commands

class MinimalEmbedHelp(commands.MinimalHelpCommand):
  def __init__(self, **options):
    self.options = options
    super().__init__(**options)
    
  async def send_pages(self):
    channel = self.get_destination()
    embeds = []
    for page in self.paginator.pages:
      e = discord.Embed(description=page)
      if self.options.get("color"):
      	e.color=self.options.get("color")
      embeds.append(e)
    for embed in embeds:
      await channel.send(embeds=embeds)

class DefaultEmbedHelp(commands.DefaultHelpCommand):
  def __init__(self, **options):
    self.options = options
    super().__init__(**options)
    
  async def send_pages(self):
    channel = self.get_destination()
    embeds = []
    for page in self.paginator.pages:
      e = discord.Embed(description=page)
      if self.options.get("color"):
      	e.color=self.options.get("color")
      embeds.append(e)
    for embed in embeds:
      await channel.send(embeds=embeds)
