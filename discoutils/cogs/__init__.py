from discord.ext import commands
import discord
import traceback
import sys

class BaseCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  async def cog_command_error(self, ctx, error):
    """The event triggered when an error is raised in this cpg while invoking a command.

        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
    if hasattr(ctx.command, 'on_error'):
      return


    ignored = (commands.CommandNotFound, )
    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
      return
    if isinstance(error, commands.DisabledCommand):
      await ctx.send(f'{ctx.command} has been disabled.')
    elif isinstance(error, commands.NoPrivateMessage):
      try:
        await ctx.author.send(
            f'{ctx.command} can not be used in DMs.')
      except discord.HTTPException:
        pass
    else:
      print('Ignoring exception in command {}:'.format(ctx.command),
            file=sys.stderr)
      traceback.print_exception(type(error),
                                error,
                                error.__traceback__,
                                file=sys.stderr)



