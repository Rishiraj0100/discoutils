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
      return await ctx.reply(f'This command has been disabled.')
    elif isinstance(error, commands.NoPrivateMessage):
      try:
        return await ctx.author.send(
            f'`{ctx.prefix}{ctx.command}` can not be used in DMs.')
      except discord.HTTPException:
        pass
    elif isinstance(error, commands.BotMissingPermissions):
      fmt = self.get_missing_perms(error)
      return await ctx.reply(content=f"I don't have {fmt} permission(s) to run this command.")
    elif isinstance(error, commands.MissingPermissions):
      fmt = self.get_missing_perms(error)
      return await ctx.reply(content=f"You don't have {fmt} permission(s) to run this command.")
    else:
      print('Ignoring exception in command {}:'.format(ctx.command),
            file=sys.stderr)
      traceback.print_exception(type(error),
                                error,
                                error.__traceback__,
                                file=sys.stderr)


  def get_missing_perms(self, exc):
    missing_permissions = exc.missing_permissions
    missing = [
        perm.replace('_', ' ').replace('guild', 'server').title()
        for perm in missing_permissions
    ]
    if len(missing) > 2:
      fmt = '{}, and {}'.format(", ".join(missing[:-1]), missing[-1])
    else:
      fmt = ' and '.join(missing)
    #message = f"I don't have {fmt} permission(s) to run this command."
    return fmt
  
