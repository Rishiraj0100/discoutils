import discord, json, random
from discord.ext import commands

class CMDs(command.Cog, name="discoCMDs"):
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
      await msg.add_reaction("🤣)
      await msg.add_reaction("😂")
    except:
      pass
    
def setup(bot: commands.Bot):
  bot.add_cog(CMDs)
