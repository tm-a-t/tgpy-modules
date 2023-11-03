import asyncio
import subprocess


async def sed(s):
    orig = await ctx.msg.get_reply_message()
    proc = await asyncio.create_subprocess_exec("sed", s, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, _ = await proc.communicate(orig.text.encode())
    text = stdout.decode()
    if text == orig.text:
        return "(no changes)"
    if orig.from_id == ctx.msg.from_id:
        await orig.edit(text)
        await ctx.msg.delete()
    else:
        return text


def sed_trans(text):
    if text.startswith("s/"):
        return f"sed({repr(text)})"
    return text


tgpy.add_code_transformer("sed", sed_trans)
