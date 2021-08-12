import discord, requests
from discord.ext import commands
from .. import BaseCog

class Kill(BaseCog, name="fun"):
  "Fun commands"

  @commands.command()
  async def kill(self, ctx, user: discord.Member):
    """used to get some random funny kill message

    Parameters
    -------------
      • user - the user to whom you wanna kill
    """
    kill = requests.get("https://api.rrrdev.cf/api/kill").json()
    if user.id == ctx.author.id:
      return await ctx.send("Why do u want to kill yourself??")
      
    response = kill.get("args")
    if "$author" in response:
      response=response.replace("$author", ctx.author.name)
      
    if "$mention" in response:
      response = response.replace("$mention", user.name)
      
    await ctx.send(response)


def setup(bot):
  bot.add_cog(Kill(bot))
