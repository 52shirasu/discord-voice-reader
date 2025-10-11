# bot/events/on_voice_state_update.py

from bot.instance import bot
from bot.utils.state import get_read_channel
from discord import Member, TextChannel

@bot.event
async def on_voice_state_update(member: Member, before, after):
    """
    ボイスチャンネルの状態変化を監視し、
    - Bot自身の接続・退出メッセージ送信
    - Botだけ残った場合の自動退出
    を行う
    """
    if bot.user is None:
        print("⚠️ bot.user が未設定です。on_ready イベントが正しく動作しているか確認してください。")
        return

    guild = member.guild
    read_channel_id = get_read_channel(guild.id)
    if read_channel_id is None:
        # 読み上げ対象チャンネルが未設定なら何もしない
        return

    text_channel = guild.get_channel(read_channel_id)
    if not isinstance(text_channel, TextChannel):
        return

    # --- Bot自身の接続・退出メッセージ ---
    if member.id == bot.user.id:
        if before.channel is None and after.channel is not None:
            await text_channel.send(f"🎤 Botがボイスチャンネル `{after.channel.name}` に接続しました！")
            print(f"🎤 Botが接続: {after.channel.name} (ID: {after.channel.id})")
        elif before.channel is not None and after.channel is None:
            await text_channel.send(f"🛑 Botがボイスチャンネルから退出しました！")
            print(f"🛑 Botが退出: {before.channel.name} (ID: {before.channel.id})")

    # --- Botがいるチャンネルから誰もいなくなった場合、自動退出 ---
    # before.channel: 退出前のチャンネル
    if before.channel is not None and before.channel.guild.voice_client is not None:
        vc = before.channel.guild.voice_client
        # チャンネル内のメンバーがBotだけかチェック
        if all(m.bot for m in before.channel.members):
            await vc.disconnect()
            await text_channel.send(
                f"🛑 ボイスチャンネル `{before.channel.name}` に誰もいなくなったため、Botが退出しました！"
            )
            print(f"🛑 ボイスチャンネル `{before.channel.name}` に誰もいなくなったため、Botが退出しました！")
