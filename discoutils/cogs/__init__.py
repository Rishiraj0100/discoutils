from discord.ext import commands
import discord
import traceback
import sys

class BaseCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    if self.qualified_name in bot.cogs:
      cls = bot.cogs.get(self.qualified_name)
      if cls:
        cmd_attrs = cls.__cog_settings__
        cls.__cog_commands__ = tuple(c._update_copy(cmd_attrs) for c in cls.__cog_commands__)
        for cmd in self.__cog_commands__:
          setattr(cls, cmd.callback.__name__, cmd)
      else:
        self.bot.add_cog(self)
    else:
      self.bot.add_cog(self)

  async def cog_command_error(self, ctx, error):
    """The event triggered when an error is raised in this cpg while invoking a command.

        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
    # handler
    if hasattr(ctx.command, 'on_error'):
      return


    ignored = (commands.CommandNotFound, )
    send_raw_error = (commands.MissingRequiredArgument, commands.MemberNotFound, commands.MessageNotFound,commands.RoleNotFound,commands.EmojiNotFound)
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
    elif isinstance(error, send_raw_error):
      return await ctx.reply(content=str(error))
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
    return fmt
  
  def is_int_formatting(self, exc):
    if not isinstance(exc, commands.BadArgument):
      return False

    exc = str(exc)

    if not exc.startswith('Converting to "'):
      return False

    exc = exc.lstrip('Converting to "')
    if str(exc[0:3]) == "int":
      return True
    
    return False
    

def setup(bot):
  bot.load_extension("discoutils.cogs.moderation")
  bot.load_extension("discoutils.cogs.fun")

