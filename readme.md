# TGPy modules I use

These are some TGPy modules from my collection, made by my friends or myself.
Feel free to read sources and adjust some code parts to your needs.

### Installation

I include installation code for each module.
Just run it with TGPy — that is, send the code anywhere in Telegram.
The code downloads the>  source from this repo and adds it to
your modules.

### Dependencies

Some modules have pip dependencies. You can install them the way you prefer:

- Just run `pip install` on the machine where TGPy is running.
- Set up a way to run shell commands from Python
  (like [the example](https://tgpy.tmat.me/extensibility/transformers/?h=shell#code-transformers) from the docs) and run
  something like `shell('pip install ...')`.
- Use [pipdep](#pipdep-by-purplesyringa) module to automatically install imported pip packages.

### Contents

- Side tools
    - [Genius](#genius-by-purplesyringa)
    - [sed](#sed-by-purplesyringa)
- TGPy utils
    - [Dunder fix](#dunder-fix-by-vanutp)
    - [aiohttp](#aiohttp)
    - [Uptime](#uptime-by-irdkwmnsb)
    - [Bot controller](#bot-controller)
    - [pipdep](#pipdep-by-purplesyringa)
- Fun
    - [Shout](#shout)
    - [Name character](#name-character)
    - [Pin message](#pin-message)
    - [Animate message](#animate-message)

<br>

## 🌐 Side tools

### Genius by [@purplesyringa](https://t.me/purplesyringa)

**[Source](modules/genius.py)**

Searches song lyrics on genius.com.

Dependencies:

```shell
pip install html2text requests
```

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/genius.py'
modules.add('genius', urlopen(url).read())
restart()
```

Example:

```
.genius believer
```

<br>

### sed by [@purplesyringa](https://t.me/purplesyringa)

**[Source](modules/sed.py)**

Use sed tool on messages.
When you reply to a message from others, this just outputs a result of processing.
When you reply to your message, your message gets edited instead.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/sed.py'
modules.add('sed', urlopen(url).read())
restart()
```

Example: (in reply to a message)

```
s/yes/no/g
```

<br>

## 🛠 TGPy utils

### Dunder fix by [@vanutp](t.me/vanutp)

**[Source](modules/dunder-fix.py)**

Telegram app for Android has a flaw in formatting:
there is no way to prevent text surrounded by double underscores turning
into italic text. This annoys because you often want to use `__dunder__` methods in Python.

The module tries to restore the code by replacing the italic parts of the message with `__dunder__` parts.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/dunder-fix.py'
modules.add('dunder-fix', urlopen(url).read())
restart()
```

<br>

### aiohttp

**[Source](modules/http.py)**

One line. Starts `http`, a client session object that can be used to make requests.

Dependencies:

```shell
pip install aiohttp
```

Install:

```python
modules.add('http', 'import aiohttp \nhttp = aiohttp.ClientSession()')
restart()
```

Example of usage:

```python
async with http.get('https://python.org') as response:
    print("Status:", response.status)

    html = await response.text()
    print("Body:", html[:15], "...")
```

<br>

### Uptime by [@irdkwmnsb](https://t.me/irdkwmnsb)

**[Source](modules/uptime.py)**

A simple function that shows how long TGPy has been active.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/uptime.py'
modules.add('uptime', urlopen(url).read())
restart()
```

Example:

```
uptime()

TGPy> 2 days, 0:15:15.700456
```

<br>

### Bot controller

**[Source](modules/bot-controller.py)**

Use Telethon to control a bot like your account.

Install:

```python
from urllib.request import urlopen
import tgpy.api

tgpy.api.config.set('bot_token', 'YOUR_BOT_TOKEN_HERE')

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/bot-controller.py'
modules.add('bot-controller', urlopen(url).read())
restart()
```

Examples of usage:

```python
# Sends a message to the same group
# if the bot is in the group

await bot.send_message(msg.chat_id, 'hello world')
return
```

```python
# Sends a message with a button to personal messages to someone
# (works only if user started a dialog with the bot)

from telethon import Button

button = Button.url('Google', 'https://google.com')
await bot.send_message('User Full Name', 'Hey', buttons=button)
return
```

```python
# starts replying to all messages with their text

from telethon import events


@bot.on(events.NewMessage())
async def on_new_message(event):
    text = event.text
    await event.reply(text)
```

<br>

### pipdep by [@purplesyringa](https://t.me/purplesyringa)

**[Source](modules/genius.py)**

Automatically installs all pip packages imported in your saved modules.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/pipdep.py'
modules.add('pipdep', urlopen(url).read())
restart()
```

<br>

## 👾 Fun stuff

### Name character

**[Source](modules/name.py)**

Just a function I often use to find out the unicode name of a letter, symbol, or emoji.

Install:

```python
modules.add('name', 'from unicodedata import name')
restart()
```

Example of usage:

```
name('👺')

TGPy> JAPANESE GOBLIN
```

<br>

### Pin message

**[Source](modules/tgpy-pin.py)**

This module is used in [TGPy Flood chat](https://t.me/tgpy_flood) to allow all members to pin messages
(not only admins.)

When someone sends `/pin` to the chat, the person with this module
automatically pins their message.

If there are multiple people who has this module installed, only one gets to pin the message. So it becomes a random
race :)

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/tgpy-pin.py'
modules.add('tgpy-pin', urlopen(url).read())
restart()
```

<br>

### Animate message

**[Source](modules/anim.py)**

Send a message and edit it many times to create a typing animation.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/anim.py'
modules.add('anim', urlopen(url).read())
restart()
```

Example:

```python
anim('Magic typing effect ✨')
```

<br>

### Shout

**[Source](modules/shout.py)**

When used in reply to a message, shows its text "shouted".

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/shout.py'
modules.add('shout', urlopen(url).read())
restart()
```

Example:

```python
# in reply to "python"
shout()

TGPy> PYTHOOOOOON
```
