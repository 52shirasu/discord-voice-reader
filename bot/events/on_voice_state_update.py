from bot.instance import bot
from bot.utils.state import get_read_channel
from discord import Member, TextChannel

@bot.event
async def on_voice_state_update(member: Member, before, after):
    # bot.user が None の場合はスキップ
    if bot.user is None:
        print("⚠️ bot.user が未設定です。on_ready イベントが正しく動作しているか確認してください。")
        return

    # Bot自身の状態が変化した場合のみ処理
    if member.id != bot.user.id:
        return

    guild = member.guild
    # state から読み上げ対象チャンネルIDを取得
    read_channel_id = get_read_channel(guild.id)

    # チャンネルIDが None の場合は処理をスキップ
    if read_channel_id is None:
        print(f"⚠️ 読み上げ対象のチャンネルIDが設定されていません: guild_id={guild.id}")
        return

    text_channel = guild.get_channel(read_channel_id)

    # チャンネルが TextChannel であることを確認
    if not isinstance(text_channel, TextChannel):
        print(f"⚠️ 読み上げ対象のチャンネルが TextChannel ではありません: guild_id={guild.id}, channel_id={read_channel_id}")
        return

    if before.channel is None and after.channel is not None:
        # Botがボイスチャンネルに参加した場合
        await text_channel.send(f"🎤 Botがボイスチャンネル `{after.channel.name}` に接続しました！")
        print(f"🎤 Botが接続: {after.channel.name} (ID: {after.channel.id})")
    elif before.channel is not None and after.channel is None:
        # Botがボイスチャンネルから退出した場合
        await text_channel.send("🛑 Botがボイスチャンネルから退出しました！")
        print(f"🛑 Botが退出: {before.channel.name} (ID: {before.channel.id})")

    # チャンネルから誰もいなくなった場合、Botが退出
    if before.channel is not None and len(before.channel.members) == 1 and before.channel.members[0].id == bot.user.id:
        await before.channel.guild.voice_client.disconnect()
        await text_channel.send(f"🛑 ボイスチャンネル `{before.channel.name}` に誰もいなくなったため、Botが退出しました！")
        print(f"🛑 ボイスチャンネル `{before.channel.name}` に誰もいなくなったため、Botが退出しました！")