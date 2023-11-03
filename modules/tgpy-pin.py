from telethon import events


@client.on(events.NewMessage())
async def func(event):
    if event.chat and event.chat.username == 'tgpy_flood':
        if event.text == '/pin':
            event.get_reply_message().await.pin().await
        elif event.text == '/unpin':
            event.get_reply_message().await.unpin().await
