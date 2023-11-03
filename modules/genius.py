import ast
import json
import html2text
import re
import requests


async def genius(query):
    data = requests.get("https://genius.com/api/search/multi", params={"q": query}).json()
    url = None
    for section in data["response"]["sections"]:
        if section["type"] == "song":
            url = section["hits"][0]["result"]["url"]
            break
    else:
        return "Song not found"

    data = requests.get(url).text
    data = re.search(r"__PRELOADED_STATE__ = JSON\.parse\((.*)\);$", data, flags=re.M).group(1)
    data = json.loads(ast.literal_eval(data).replace(r"\$", "$"))

    song = data["songPage"]

    conv = html2text.HTML2Text()
    conv.ignore_links = True

    title = "Unknown"
    artist = "Unknown"
    for item in song["dfpKv"]:
        if item["name"] == "song_title":
            title = item["values"][0]
        elif item["name"] == "artist_name":
            artist = ", ".join(item["values"])

    text = re.sub(r"<a.*?>", "", song["lyricsData"]["body"]["html"].replace("</a>", ""))
    text = text.replace("<br>", "")
    text = text.replace("<p>", "").replace("</p>", "")
    text = text.strip()

    text = f"<a href='{url}'><b>{title}</b></a> by {artist}\n\n" + text
    await ctx.msg.respond(text, parse_mode="html")
    await ctx.msg.delete()


def genius_trans(cmd):
    if cmd.startswith(".genius "):
        return f"await genius({repr(cmd[8:])})"
    return cmd


tgpy.add_code_transformer("genius", genius_trans)
