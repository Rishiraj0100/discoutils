import discord, json, random
from discord.ext import commands

class CMDs(commands.Cog, name="discoCMDs"):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def kill(self, ctx, user: discord.Member):
    """used to get some random funny kill message
    parameters
      • user
        use id or mention a user to get message
    """
    with open("discoutils/assets/kill.json", "r") as f:
      kill = json.load(f)
      
    kills = kill["kills"]
    
    response = random.choice(kills)
    
    if "$author" in response:
      response=response.replace("$author", ctx.author.name)
      
    if "$mention" in response:
      response = response.replace("$mention", user.name)
      
    try:
      msg = await ctx.send(response)
      await msg.add_reaction("🤣")
      await msg.add_reaction("😂")
    except:
      pass
    
  @commands.command()
  async def load(self,ctx,cog_name):
    '''
    This command is used to load cogs easily.
    Usage - load [cog_name]
    Example - load cogs.moderation
    '''
    try:
      self.bot.load_extension(f"{name}")
    except Exception as e:
      retrun await ctx.send(f"The cog could not be loaded due to error - \n```{e}```")
    await ctx.send(f"{name} extension loaded successfully!")
     
  
  @commands.command()
  async def unload(self,ctx,cog_name):
    '''
    This command is used to unload cogs easily.
    Usage - unload [cog_name]
    Example - unload cogs.moderation
    '''
    try:
      self.bot.unload_extension(f"{name}")
    except Exception as e:
      retrun await ctx.send(f"The cog could not be unloaded due to error - \n```{e}```")
    await ctx.send(f"{name} extension unloaded successfully!")
    
def setup(bot: commands.Bot):
  bot.add_cog(CMDs)
