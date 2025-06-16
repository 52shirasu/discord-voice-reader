from bot.instance import bot
from discord.ext import commands
from bot.utils.state import set_read_channel
import os
import discord  # 忘れずに追加

@bot.command()
async def join(ctx):
    voice_channel = None
    read_channel = None

    # 1. 環境変数からボイスチャンネルIDリストを取得して存在確認
    voice_channel_ids = os.getenv("DEFAULT_VOICE_CHANNEL_IDS", "")
    for cid in voice_channel_ids.split(","):
        cid = cid.strip()
        if not cid.isdigit():
            continue
        candidate = ctx.guild.get_channel(int(cid))
        if candidate and isinstance(candidate, discord.VoiceChannel):
            voice_channel = candidate
            print(f"✅ 接続対象のボイスチャンネルが見つかりました: {voice_channel.name} (ID: {voice_channel.id})")
            break

    # 2. 環境変数から読み上げ用テキストチャンネルIDリストを取得して存在確認
    read_channel_ids = os.getenv("DEFAULT_READ_CHANNEL_IDS", "")
    for cid in read_channel_ids.split(","):
        cid = cid.strip()
        if not cid.isdigit():
            continue
        candidate = ctx.guild.get_channel(int(cid))
        if candidate and isinstance(candidate, discord.TextChannel):
            read_channel = candidate
            print(f"✅ 読み上げ対象のテキストチャンネルが見つかりました: {read_channel.name} (ID: {read_channel.id})")
            break

    # 3. ボイスチャンネルが見つからなければ、ユーザーの現在のVCを確認
    if not voice_channel and ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        print(f"✅ ユーザーのボイスチャンネルに接続します: {voice_channel.name} (ID: {voice_channel.id})")

    # 4. チャンネルが見つからなければエラー
    if not voice_channel:
        await ctx.send("⚠️ 接続できるボイスチャンネルが見つかりませんでした。")
        return

    if not read_channel:
        await ctx.send("⚠️ 読み上げ対象のテキストチャンネルが見つかりませんでした。")
        return

    # 5. ボイスチャンネルに接続
    await voice_channel.connect()

    # 6. 読み上げチャンネルを記録し、通知
    set_read_channel(ctx.guild.id, read_channel.id)
    await read_channel.send("💬 このチャンネルが読み上げ対象になりました！")

    # ログ出力
    print(f"🎤 接続したボイスチャンネル: {voice_channel.name} (ID: {voice_channel.id})")
    print(f"💬 読み上げチャンネル: {read_channel.name} (ID: {read_channel.id})")
