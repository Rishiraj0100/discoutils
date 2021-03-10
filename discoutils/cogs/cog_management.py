import discord
from discord.ext import commands
from discoutils.settings import cog_managers


class COG_manager(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
    

  

  
  @commands.command()
  @commands.check(cog_managers)
  async def load(self,ctx,cog_name):
    '''
    This command is used to load cogs easily.
    Usage - load [cog_name]
    Example - load cogs.moderation
    '''
    try:
      self.bot.load_extension(f"{name}")
    except Exception as e:
      await ctx.send(f"The cog could not be loaded due to error - \n```py\n{e}\n```")
      return
    else:
      await ctx.send(f"{name} extension loaded successfully!")

     

  

  @commands.command()
  @commands.check(cog_managers)
  async def unload(self,ctx,cog_name):
    '''
    This command is used to unload cogs easily.
    Usage - unload [cog_name]
    Example - unload cogs.moderation
    '''
    try:
      self.bot.unload_extension(f"{name}")
    except Exception as e:
      await ctx.send(f"The cog could not be unloaded due to error - \n```py\n{e}\n```")
      return
    else:
      await ctx.send(f"{name} extension unloaded successfully!")
      

def setup(bot: commands.Bot):
  bot.add_cog(COG_manager(bot=bot))
