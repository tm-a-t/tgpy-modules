# TGPy modules I use

These are some of my TGPy modules (made by me or something else).

## 🛠 TGPy utils

### Dunder fix

[By @vanutp](t.me/vanutp) • [Source](modules/dunder_fix.py)

Telegram app for Android has a flaw in formatting:
there is no way to prevent text surrounded by double underscores turning
into italic text. This annoys because you often want to use `__dunder__` methods in Python.

The module tries to restore the code by replacing the italic parts of the message with `__dunder__` parts.

Install:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/dunder_fix.py'
modules.add('dunder_fix', urlopen(url).read())
```

### HTTP

[Source](modules/http.py)

One line. Starts a client session object `http` that can be used to make requests.

First, install aihttp:

```shell
pip install aiohttp
```

Then the module:

```python
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/tm-a-t/tgpy-modules/main/modules/http.py'
modules.add('http', urlopen(url).read())
```

Example of usage:

```python
async with http.get('https://python.org') as response:
    print("Status:", response.status)
    print("Content-type:", response.headers['content-type'])

    html = await response.text()
    print("Body:", html[:15], "...")
```

### Uptime

### Control bot

## Sending stuff

### Genius

### GHCI

### sed

### xkcd

## Fun

### Animate message

### Name character

### Shout

### Pin message

