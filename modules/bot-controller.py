import tgpy.api
from telethon import TelegramClient

bot = TelegramClient('bot', client.api_id, client.api_hash)
bot_token = tgpy.api.config.get('bot_token')
await bot.start(bot_token=bot_token)


async def bot_ping():
    await bot.send_message(ctx.msg.chat_id, 'Pong!')
