from .message import messagemod
from .user import usermod

def setup(bot):
  bot.add_cog(messagemod(bot))
  bot.add_cog(usermod(bot))
