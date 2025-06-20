from bot.instance import bot, TOKEN
from bot.commands.join import join
from bot.commands.bye import bye
from bot.commands.match import match
from bot.commands.setchannel import setchannel
from bot.events.on_ready import on_ready
from bot.events.on_message import on_message
from bot.events.on_voice_state_update import on_voice_state_update

def run_bot():
    if not TOKEN:
        raise ValueError("⚠️ DISCORD_TOKEN が設定されていません！.env ファイルを確認してね！")
    bot.run(TOKEN)