from bot.instance import bot
from bot.utils import tts, state

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # コマンド処理を実行
    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
        print(f"⚠️ コマンドメッセージをスキップ: {message.content}")
        return

    if not message.guild:
        return

    # テキスト以外のメッセージをスキップ
    if not message.content.strip():
        print(f"⚠️ テキスト以外のメッセージをスキップ: {message}")
        return

    read_channel_id = state.get_read_channel(message.guild.id)
    read_channel = message.guild.get_channel(read_channel_id) if read_channel_id else None
    if read_channel:
        print(f"🔍 読み上げ対象チャンネル: {read_channel.name} (ID: {read_channel.id})")
    else:
        print("⚠️ 読み上げ対象チャンネルが設定されていません")

    # 読み上げ対象じゃないチャンネルの場合
    if not read_channel or message.channel.id != read_channel.id:
        print(f"⚠️ 読み上げ対象外のチャンネル: {message.channel.name} (ID: {message.channel.id})")
        return

    vc = message.guild.voice_client
    # Botがボイスチャンネルに接続されていない場合
    if not vc or not vc.is_connected():
        print("⚠️ Botがボイスチャンネルに接続されていません")
        await message.channel.send("⚠️ Botがボイスチャンネルに接続されていません。`.join` コマンドで接続してください！")
        return

    # テキストを読み上げ
    try:
        await tts.speak_text(message.content, vc)  # 音声再生
    except Exception as e:
        print(f"⚠️ 音声再生中にエラーが発生: {e}")
        await message.channel.send("⚠️ メッセージの読み上げ中にエラーが発生しました！")