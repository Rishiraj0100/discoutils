# discoutils
discoutils is a module that helps discord bot development easy

# installation
```bash
pip install discoutils
```

# Help Commands
There are two help commands currently but soon there will be more.
## MinimalEmbedHelp

[![MinimalEmbedHelp.png](https://github.com/Rishiraj0100/discoutils/blob/v0.0.3-beta/docs/img/Screenshot_20210309-130459.png)](https://raw.githubusercontent.com/Rishiraj0100/discoutils/v0.0.3-beta/docs/img/Screenshot_20210309-130459.png)
```py

import discord
from discord.ext import commands
from discoutils import MinimalEmbedHelp

bot = commands.Bot(command_prefix=".", help_command=MinimalEmbedHelp())
```

## DefaultEmbedHelp

[![DefaultEmbedHelp.png](https://github.com/Rishiraj0100/discoutils/blob/v0.0.3-beta/docs/img/Screenshot_20210309-130522.png)](https://raw.githubusercontent.com/Rishiraj0100/discoutils/v0.0.3-beta/docs/img/Screenshot_20210309-130522.png)

```py

import discord
from discord.ext import commands
from discoutils import DefaultEmbedHelp

bot = commands.Bot(command_prefix=".", help_command=DefaultEmbedHelp())
```

# Random Functions
There are only 3 functions for now we will be adding more functions soon

## Random Colors For Embeds

```py
randomColor()
```
#### Example:

```py

import discord
from discord.ext import commands
from discoutils import random_things

# test embed

@bot.command()
async def test(ctx):
    embed = discord.Embed(title = 'test',description='test',color=random_things.randomColor())
    await ctx.send(embed=embed)

```

## Random Dog Images

```py
random_dog()
```
#### Example:

```py

import discord
from discord.ext import commands
from discoutils import random_things

# test embed

@bot.command()
async def test(ctx):
    embed = discord.Embed(title = 'test',description='test')
    embed.set_image(url=random_things.random_dog())
    await ctx.send(embed=embed)

```

## Random Cat Images

```py
random_cat()
```
#### Example:

```py

import discord
from discord.ext import commands
from discoutils import random_things

# test embed

@bot.command()
async def test(ctx):
    embed = discord.Embed(title = 'test',description='test')
    embed.set_image(url=random_things.random_cat())
    await ctx.send(embed=embed)

```
