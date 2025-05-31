from bot.instance import bot, TOKEN
from bot.commands.join import join
from bot.commands.bye import bye
from bot.commands.setchannel import setchannel
from bot.events.on_ready import on_ready
from bot.events.on_message import on_message

def run_bot():
    if not TOKEN:
        raise ValueError("⚠️ DISCORD_TOKEN が設定されていません！.env ファイルを確認してね！")
    bot.run(TOKEN)