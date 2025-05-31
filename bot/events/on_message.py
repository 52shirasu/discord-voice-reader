from bot.instance import bot
from bot.utils import tts, state

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

    if not message.guild:
        return

    read_channel_id = state.get_read_channel(message.guild.id)
    print(f"🔍 読み上げ対象チャンネルID: {read_channel_id}")
    if read_channel_id and message.channel.id == read_channel_id:
        vc = message.guild.voice_client
        if not vc or not vc.is_connected():
            print("⚠️ Botがボイスチャンネルに接続されていません")
            return

        await tts.speak_text(message.content, vc)