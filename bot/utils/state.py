# 読み上げ対象チャンネルIDを保持する変数
read_channel_map = {}  # guild_id: channel_id

def set_read_channel(guild_id, channel_id):
    """読み上げ対象チャンネルを設定"""
    read_channel_map[guild_id] = channel_id
    print(f"✅ チャンネル設定: guild_id={guild_id}, channel_id={channel_id}")

def get_read_channel(guild_id):
    """読み上げ対象チャンネルを取得"""
    channel_id = read_channel_map.get(guild_id)
    print(f"🔍 チャンネル取得: guild_id={guild_id}, channel_id={channel_id}")
    return channel_id