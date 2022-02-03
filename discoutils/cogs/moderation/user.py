import discord
from discord.ext import commands
from .. import BaseCog
import asyncio
import typing


__all__ = ("usermod")

class usermod(BaseCog, name="moderation"):
  @commands.command()
  @commands.has_permissions(kick_members = True)
  @commands.bot_has_permissions(kick_members = True)
  async def kick(self, ctx, member: discord.Member, *,reason: typing.Optional[str] = None):
    """kick someone

        Parameters
        ------------
        • member - the member to kick
        • reason - reason why the member was kicked
        """
    fmt = f"{ctx.author.name}#{ctx.author.discriminator}"
    if reason:
      reason = f"**{fmt}**: " + reason
    else:
      reason = f"Action done by **{fmt}*"
      
    try:
      await member.kick(reason=reason)
    except discord.Forbidden:
      await ctx.send(f"Can't kick {member.mention}, This can be due to discord role hiearchy.")
    else:
      await ctx.send(f"Successfully kicked {member.name}#{member.discriminator}")


  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason: typing.Optional[str] = None):
    """ban someone

        Parameters
        ------------
        • member - the member to ban
        • reason - reason why the member was banned
        """
    fmt = f"{ctx.author.name}#{ctx.author.discriminator}"
    if reason:
      reason = f"**{fmt}**: " + reason
    else:
      reason = f"Action done by **{fmt}*"
      
    try:
      await member.ban(reason=reason)
    except discord.Forbidden:
      await ctx.send(f"Can't ban {member.mention}, This can be due to discord role hiearchy.")
    else:
      await ctx.send(f"Successfully banned {member.name}#{member.discriminator}")


  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(ban_members=True)  
  async def unban(self, ctx, id_or_tag: str, *, reason=None):
    """unban someone

        Parameters
        ------------
        • id_or_tag - id or Tag (user#0001) of the banned user
        • reason - reason why the user is being unbanned
        """
    fmt = f"{ctx.author.name}#{ctx.author.discriminator}"
    
    if reason:
      reason = f"**{fmt}**: " + reason
    else:
      reason = f"Action done by **{fmt}*"

    bans = await ctx.guild.bans()
    unbanned, unbanned_user = False, None
    member_id = None
    member_name, member_discriminator = None, None

    try:
      member_id = int(id_or_tag)
    except ValueError:
      member_name, member_discriminator = id_or_tag.split('#')
      
    for ban_entry in banned_users:
      user = ban_entry.user

      if not member_id and (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user,reason=reason)
        unbanned, unbanned_user = True, user
        break
      elif member_id and member_id == user.id:
        await ctx.guild.unban(user)
        unbanned, unbanned_user = True, user
        break

    if not unbanned:
      return await ctx.send(f"User with id_or_tag {id_or_tag} not found in this server's ban list")
      
    await ctx.send(f"Successfully unbanned {unbanned_user}")

  @commands.group(name="role", invoke_without_command=True)
  async def role(self, ctx):
    e = discord.Embed(title="Role Commands")
    e.add_field(name=f"{ctx.prefix}{ctx.command} add `@user @role`", value="Adds role to the given user")
    e.add_field(name=f"{ctx.prefix}{ctx.command} remove `@user @role`", value="Remove role from the given user")
    await ctx.send(embed=e)

  @role.command(name="add")
  @commands.guild_only()
  @commands.has_permissions(manage_roles=True)
  @commands.bot_has_permissions(manage_roles=True)
  async def role_add(self, ctx, member: discord.Member, *,role: discord.Role):
    """Add a role to someone else

        Parameters
        ------------
        • member - the user to whom role is to be added
        • role - the role which is to be added
        """
    reason = f"Action done by {ctx.author.name}#{ctx.author.discriminator}"
    if role in member.roles:
      return await ctx.send(f"{member.mention} already have this role")
    
    try:
      await member.add_roles(role, reason=reason)
    except:
      await ctx.send("I can't add role to  {member.mention} due to discord role hiearchy")
    else:
      await ctx.send(f"Successfully added the role `{role.name}` to {member.mention}")
  

  @role.command(name="remove")
  @commands.guild_only()
  @commands.has_permissions(manage_roles=True)
  @commands.bot_has_permissions(manage_roles=True)
  async def role_remove(self, ctx, member: discord.Member, *,role: discord.Role):
    """Remove a role from someone else

        Parameters
        ------------
        • member - the user from whom the role is to be taken
        • role - the role which is to be removed
        """
    reason = f"Action done by {ctx.author.name}#{ctx.author.discriminator}"
    if role not in member.roles:
      return await ctx.send(f"{member.mention} doesn't have this role")
    
    try:
      await member.remove_roles(role, reason=reason)
    except:
      await ctx.send("I can't remove roles from {member.mention} due to discord role hiearchy")
    else:
      await ctx.send(f"Successfully removed the role `{role.name}` from {member.mention}")
    

def setup(bot):
  usermod(bot)
