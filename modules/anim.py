import asyncio


async def anim(text='Hello World'):
    chat = ctx.msg.chat_id
    rep = await ctx.msg.get_reply_message()
    await ctx.msg.delete()
    message = await client.send_message(chat, '...', reply_to=rep)
    for i in range(len(text)):
        for state in range(2):
            await message.edit(text[:i + 1] + '▓░'[state])
            await asyncio.sleep(0.1)
    await message.edit(text)
    return message
