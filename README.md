# discoutils
discoutils is a module that helps discord bot development easy

# installation
```bash
pip install discoutils
```

# MinimalEmbedHelp

[![https://github.com/Rishiraj0100/discoutils/blob/v0.0.3-beta/docs/img/Screenshot_20210309-130459.png](https://github.com/Rishiraj0100/discoutils/blob/v0.0.3-beta/docs/img/Screenshot_20210309-130459.png)](https://github.com/)

```py
import discord, discoutils
from discord import commands
from discoutils import MinimalEmbedHelp as MEH

bot = commands.Bot(command_prefix=".", help_command=MEH())

@bot.event
async def on_ready():
    print("bot is running")

bot.run("your token")
```
