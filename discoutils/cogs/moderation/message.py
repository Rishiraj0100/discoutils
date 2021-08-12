import discord
from discord.ext import commands
import asyncio
import typing
from .. import BaseCog


class messagemod(BaseCog, name="moderation"):
  @commands.group(aliases=["c","clear"], invoke_without_command=True)
  @commands.guild_only()
  @commands.has_permissions(manage_messages = True)
  @commands.bot_has_permissions(manage_messages = True)
  async def clean(self, ctx, amount: typing.Optional[int] = 5, member: discord.Member = None):
    """delete a number of your own or another users messages

        Parameters
        ------------
        • amount - the amount of messages to delete, delets 5 messages by default
        • member - the member whose messages are to be deleted, deletes all messages by default
        """
    deleted = 0
    #await ctx.message.delete()
    user = member
    def check(m):
      if user:
        return m.id != ctx.message.id and m.author.id == user.id
      return m.id != ctx.message.id
      
    await ctx.channel.purge(limit=amount, check=check)

  @clean.command(name="reactions", aliases=["rs"])
  async def clear_reactions(self, ctx, message: discord.Message):
    """clears all reactions on a message

        Parameters
        -----------
        • message - the id or link of the message from which to the reactions are to be removed
        """

    if msg:
      await msg.clear_reactions()
      return await ctx.reply(content="Successfully cleared all the reactions of that message")


  @clean.command(name="reaction",aliases=["r"])
  async def clear_reaction(self, ctx, message: discord.Message, emoji: discord.Emoji, user: typing.Optional[discord.Member] = None):
    """clear a specific reaction from the message

        Parameters
        ------------
        • message - id or link of the message from which the reaction has to be removed
        • emoji - the reaction to remove from the message
        • user - the user of whom to reaction is removed, clears all reactions of that emoji is none given
        """
    if user:
      await message.remove_reaction(emoji,user)
      return await ctx.reply(f"Successfully removed reaction of emoji {emoji} of {user.mention}")
      
    await message.clear_reaction(emoji)
    return await ctx.reply(f"Successfully cleared all reactions of emoji {emoji}")



  @clean.command(aliases=["i"])
  async def images(self, ctx, images_to_delete: int = 10):
    """deletes messages containing images

        Parameters 
        ------------
        • images_to_delete - number of images to delete
        """
    deleted = 0
    async for m in ctx.channel.history(limit=200):
      if m.attachments:
        await m.delete(reason=f"Action done by {ctx.author.name}#{ctx.author.discriminator}")
        deleted += 1
        if images_to_delete == deleted:
          break
    await ctx.send(f"Successfully deleted {deleted} messages containing images")

  @clean.command(aliases=["b"])
  async def bots(self, ctx, messages_to_delete: int = 15):
    """deletes messages sent by bots

        Parameters 
        ------------
        • messages_to_delete - number of messages to delete
        """
    deleted = 0
    async for m in ctx.channel.history(limit=200):
      if m.author.bot:
        await m.delete(reason=f"Action done by {ctx.author.name}#{ctx.author.discriminator}")
        deleted += 1
        if deleted == messages_to_delete:
          break
    await ctx.send(f"Successfully deleted {deleted} messages from bots")

  @clean.command(aliases=["w"])
  async def word(self, ctx, messages_to_delete: typing.Optional[int] = 10, *,word: str):
    """deletes messages containing the specified words

        Parameters
        ------------
        • word - the words to search for
        • messages_to_delete - number of messages to delete
        """
    deleted = 0
    async for m in ctx.channel.history(limit=200):
      if word in m.content.lower():
        if not m.id == ctx.message.id:
          await m.delete(reason=f"Action done by {ctx.author.name}#{ctx.author.discriminator}")
          deleted += 1
        if deleted == messages_to_delete:
          break
    await ctx.send(f"Successfully deleted {deleted} message containing {word}")
    



def setup(bot):
  bot.add_cog(messagemod(bot))
