import aiohttp
import json


async def xkcd(topic):
    print(repr(topic))
    async with aiohttp.ClientSession() as session:
        async with session.post("https://relevant-xkcd-backend.herokuapp.com/search", data={"search": topic}) as res:
            result = json.loads(await res.text())  # Mime-type is wrong, so res.json() fails
    assert result["success"]
    if not result["results"]:
        return "(no results found)"
    result = result["results"][0]
    title = result["title"]
    number = result["number"]
    titletext = result["titletext"]
    image = result["image"]
    image_path = await wget(image)
    await ctx.msg.respond(f'<b>{title}</b>\n<a href="https://xkcd.com/{number}">#{number}</a>\n\n<i>{titletext}</i>',
                          parse_mode="html", file=open(image_path, "rb"))
    await ctx.msg.delete()


def xkcd_trans(text):
    if text.startswith(".xkcd "):
        return f"xkcd({repr(text[6:])})"
    return text


tgpy.add_code_transformer("xkcd", xkcd_trans)
