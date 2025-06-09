from bot.instance import bot
from discord.ext import commands
from bot.utils.state import set_read_channel
import os

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()

        # 環境変数から読み上げ対象チャンネルIDを取得
        default_read_channel_id = int(os.getenv("DEFAULT_READ_CHANNEL_ID", 0))
        target_channel = None

        if default_read_channel_id:
            # 環境変数で指定されたチャンネルを取得
            target_channel = ctx.guild.get_channel(default_read_channel_id)

        if target_channel:
            # 環境変数で指定されたチャンネルが存在する場合
            set_read_channel(ctx.guild.id, target_channel.id)
            await target_channel.send("💬 このチャンネルが読み上げ対象になりました！")
            print(f"✅ 環境変数から設定された読み上げ対象チャンネル: {target_channel.name} (ID: {target_channel.id})")
        else:
            # 環境変数で指定されたチャンネルが存在しない場合、コマンドを入力したチャンネルを設定
            set_read_channel(ctx.guild.id, ctx.channel.id)
            await ctx.channel.send("💬 このチャンネルが読み上げ対象になりました！")
            print(f"⚠️ 環境変数で指定されたチャンネルが見つからないため、現在のチャンネルを設定: {ctx.channel.name} (ID: {ctx.channel.id})")

        # コンソールに情報を表示
        print(f"🎤 接続したボイスチャンネル: {channel.name} (ID: {channel.id})")
    else:
        await ctx.send("⚠️ まずはボイスチャンネルに入ってください！")
