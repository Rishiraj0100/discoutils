import discord
from discord.ext import commands
import asyncio
import typing
from discoutils.cogs import BaseCog


class mod(BaseCog):
  @commands.command(aliases = ["crs"])
  @commands.has_permissions(manage_messages = True)
  async def clearreactions(self, ctx, message: int):
    try:
      msg = await ctx.channel.fetch_message(message)
    except:
      return await ctx.reply(content="Message not found with id {}".format(message))

    if msg:
      await msg.clear_reactions()
      return await ctx.reply(content="Successfully cleared all the reactions of that message")

    return await ctx.reply(content="Message not found with id {}".format(message))


def setup(bot):
  bot.add_cog(mod(bot))
