from bot.instance import bot
from bot.utils.state import set_read_channel
import os
from dotenv import load_dotenv
from discord import VoiceChannel, StageChannel  # 型ヒント用にインポート

load_dotenv()
default_read_channel_id = int(os.getenv("DEFAULT_READ_CHANNEL_ID", 0))  # デフォルトのチャンネルIDを設定

@bot.event
async def on_ready():
    print(f"✅ Bot起動完了: {bot.user}")

    # デフォルトの読み上げ対象チャンネルを設定
    for guild in bot.guilds:
        if default_read_channel_id:
            set_read_channel(guild.id, default_read_channel_id)

            # テキストチャンネル名を取得して表示
            text_channel = guild.get_channel(default_read_channel_id)
            if text_channel:
                print(f"💬 読み上げ対象テキストチャンネル: {text_channel.name} (ID: {text_channel.id})")
            else:
                print(f"⚠️ テキストチャンネルが見つかりません: ID={default_read_channel_id}")
        else:
            print(f"⚠️ デフォルトチャンネルIDが設定されていません")
