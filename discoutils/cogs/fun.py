"""
MIT License

Copyright (c) 2021 Rishiraj0100

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""




import discord, json, random
from discord.ext import commands

class fun(commands.Cog, name="fun"):
  """Fun Commands"""
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def kill(self, ctx, user: discord.Member):
    """used to get some random funny kill message
    parameters
      • user
        use id or mention a user to get message
    """
    kill = requests.get("https://raw.githubusercontent.com/Rishiraj0100/discoutils/main/discoutils/assets/kill.json").json()

      
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
    
def setup(bot: commands.Bot):
  bot.add_cog(fun(bot))
