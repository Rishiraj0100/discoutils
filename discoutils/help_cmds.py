import discord
from discord.ext import commands

class MinimalEmbedHelp(commands.MinimalHelpCommand):
  def __init__(self, **options):
    self.options = options
    self.embed_template = options.get("embed_template", discord.Embed)
    if not isinstance(self.embed_template, discord.Embed):
      raise TypeError(f"Embed template must be a subclass of discord.Embed not {type(self.embed_template)!r}")
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
    self.embed_template = options.get("embed_template", discord.Embed)
    if not isinstance(self.embed_template, discord.Embed):
      raise TypeError(f"Embed template must be a subclass of discord.Embed not {type(self.embed_template)!r}")
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
