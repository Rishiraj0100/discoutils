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




import discord
from discord.ext import commands
import asyncio
import typing


class mod(commands.Cog, name="moderation"):
	"""useful commands for moderation"""
	def __init__(self, bot):
		self.bot = bot

	async def format_mod_embed(self, ctx, user, success,method, duration=None, location=None):
		"""Helper func to format an embed to prevent extra code"""
		if type(user) == int:
			user = await self.bot.fetch_user(user)
		emb = discord.Embed()
		emb.set_author(name=method.title(),
		               icon_url=user.avatar_url_as(static_format="png"))
		emb.color = await ctx.get_dominant_color(user.avatar_url)
		emb.set_footer(text=f"User ID: {user.id}")
		if success:
			if method == "ban" or method == "hackban":
				emb.description = f"{user} was just {method}ned."
			else:
				emb.description = f"{user} was just {method}ed."
		else:
			emb.description = (
			    f"You do not have the permissions to {method} {user.name}.")
		return emb



	@commands.command(aliases=["cr"])
	@commands.has_permissions(manage_messages = True)
	async def clearreaction(self, ctx, message: typing.Optional[int] = 1, emoji: discord.Emoji = None):
		"""clear a specific reaction from the message
        Parameters
        • message - the message number from which to remove the reaction
        • emoji - the reaction to remove from the message
        """
		for i, m in enumerate(await ctx.channel.history().flatten()):
			if i == message:
				await m.clear_reaction(emoji)

	@commands.command(aliases=["crs"])
	@commands.has_permissions(manage_messages = True)
	async def clearreactions(self, ctx, message: int):
		"""clears all reactions on a message
        Parameters
        • message - the number of the message from which to remove the reactions
        """
		for i, m in enumerate(await ctx.channel.history().flatten()):
			if i == message:
				await m.clear_reactions()

	@commands.command()
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: discord.Member, *,reason="No reason given"):
		"""kick someone
        Parameters
        • member - the member to kick
        • reason - reason why the member was kicked
        """
		self.saved_roles[member.id] = member.roles[1:]
		try:
			await ctx.guild.kick(member, reason=reason)
		except:
			success = False
		else:
			success = True

		emb = await self.format_mod_embed(ctx, member, success, "kick")

		await ctx.send(embed=emb)

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason="No reason given",
	):
		"""ban someone, can also be used to ban someone not in the guild using their id
        Parameters
        • member - the member to ban
        • reason - reason why the member was banned
        """
		if type(member) == discord.Member:
			await ctx.guild.ban(member, reason=reason, delete_message_days=0)
		else:
			await ctx.guild.ban(discord.Object(member), reason=reason, delete_message_days=0)
		emb = await self.format_mod_embed(ctx, member, True, "ban")
		await ctx.send(embed=emb)

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, name_or_id, *, reason=None):
		"""unban someone
        Parameters
        • name_or_id - name or id of the banned user
        • reason - reason why the user was unbanned
        """
		ban = await ctx.get_ban(name_or_id)

		try:
			await ctx.guild.unban(ban.user, reason=reason)
		except:
			success = False
		else:
			success = True

		emb = await self.format_mod_embed(ctx, ban.user, success, "unban")

		await ctx.send(embed=emb)

	@commands.command(aliases=["prune", "clear"])
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount: int = 10, *, ignore_pins=True):
		"""purge a number of messages
        Parameters
        • amount - the amount of messages to purge
        • ignore_pins - pass a truthy value to ignore pinned messages, defaults to True
        """
		if ignore_pins:
			try:
				await ctx.channel.purge(limit=amount + 1,
				                check=lambda m: m.pinned == False)
			except Exception as e:
				print(f"Error\n> {e}")
		else:
			try:
				await ctx.purge(limit=amount + 1)
			except Exception as e:
				print(f"Error\n> {e}")

	def message_author(self, message, member):
		message.author.id == member.id

	@commands.group(aliases=["c"], invoke_without_command=True)
	@commands.has_permissions(manage_messages=True)
	async def clean(self, ctx, amount: typing.Optional[int] = 0, member: discord.Member = None):
		"""delete a number of your own or another users messages
        Parameters
        • amount - the amount of messages to delete, delets ∞ messages by default
        • member - the member whose messages are to be deleted, deletes your own messages by default
        """
		deleted = 0
		await ctx.message.delete()
		user = member or ctx.message.author
		async for m in ctx.channel.history(limit=100):
			if m.author.id == user.id:
				try:
					await m.delete()
					deleted += 1
					if deleted == amount:
						break
				except Exception as e:
					print(
					    f"Error while deleting messege. Probably a system message\nError: {e}"
					)

	@clean.command(aliases=["i"])
	async def images(self, ctx, images_to_delete: int = 10):
		"""deletes messages containing images
        Parameters
        • images_to_delete - number of images to delete
        """
		deleted = 0
		async for m in ctx.channel.history(limit=200):
			if m.attachments:
				await m.delete()
				deleted += 1
				if images_to_delete == deleted:
					break
		await ctx.message.delete()

	@clean.command(aliases=["b"])
	async def bots(self, ctx, messages_to_delete: int = 15):
		"""deletes messages sent by bots
        Parameters
        • messages_to_delete - number of messages to delete
        """
		deleted = 0
		async for m in ctx.channel.history(limit=200):
			if m.author.bot:
				await m.delete()
				deleted += 1
				if deleted == messages_to_delete:
					break
		await ctx.message.delete()

	@clean.command(aliases=["w"])
	async def word(self, ctx, messages_to_delete: typing.Optional[int] = 10, *,words: str):
		"""deletes messages containing the specified words
        Parameters
        • words - the words to search for
        • messages_to_delete - number of messages to delete
        """
		deleted = 0
		async for m in ctx.channel.history(limit=200):
			if words in m.content.lower():
				await m.delete()
				deleted += 1
				if deleted == messages_to_delete + 1:
					break
		await ctx.message.delete()

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def addrole(self, ctx, member: discord.Member, *,role: discord.Role):
		"""Add a role to someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role"""
		if not role:
			return await ctx.send("That role does not exist.")
		await member.add_roles(role)
		await ctx.send(f"Added: `{role.name}`")

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def removerole(self, ctx, member: discord.Member, *,role: discord.Role):
		"""Remove a role from someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role"""
		await member.remove_roles(role)
		await ctx.send(f"Removed: `{role.name}`")


def setup(bot):
	bot.add_cog(mod(bot))
