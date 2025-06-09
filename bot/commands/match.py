from bot.instance import bot
from discord.ext import commands
from bot.utils.state import get_read_channel
from bot.utils.tts import speak_text  # edge-tts を使用した speak_text 関数
import aiohttp
import datetime

def iso_to_unix(iso_str: str) -> int:
    """ISO8601文字列をUNIXタイムスタンプ（秒）に変換"""
    return int(datetime.datetime.fromisoformat(iso_str.replace("Z", "+00:00")).timestamp())

@bot.command()
async def match(ctx):
    guild_id = ctx.guild.id
    text_channel_id = get_read_channel(guild_id)
    target_channel = ctx.guild.get_channel(text_channel_id)

    if not target_channel:
        await ctx.send("⚠️ 読み上げ対象のチャンネルが設定されていません。`.join` や `.setchannel` で設定してください。")
        return

    vc = ctx.guild.voice_client
    if not vc or not vc.is_connected():
        await ctx.send("⚠️ VCに接続していません。まず `.join` を使ってボイスチャンネルに参加させてください。")
        return

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://spla3.yuu26.com/api/schedule") as res:
                data = await res.json()

        print("[DEBUG] .match コマンドのデータ:", data)

        result = data.get("result", {})
        regular = result.get("regular", [])
        bankara = result.get("bankara_challenge", [])
        fest = result.get("fest", [])

        if len(regular) < 2 or len(bankara) < 2:
            await ctx.send("⚠️ スケジュール情報が不足しています。")
            return
        message_lines = []


        if result.get("is_fest", False):
            fest_now = fest[0]
            fest_stages = [s.get("name", "不明") for s in fest_now.get("stages", [])]
            message_lines.append(
                f"現在、フェスマッチが開催中です！ステージは、{fest_stages[0]} と {fest_stages[1]} です。"
            )
        else:
            # 通常のナワバリバトル（Regular）
            now_regular = regular[0]
            next_regular = regular[1]

            now_rule = now_regular.get("rule", {}).get("name", "不明")
            now_maps = [stage.get("name", "不明") for stage in now_regular.get("stages", [])]


            next_time_str = "不明"
            try:
                next_time = iso_to_unix(next_regular.get("start_time", ""))
                next_time_str = datetime.datetime.fromtimestamp(next_time).strftime("%H時%M分")
            except Exception:
                pass

            # ガチマッチ（バンカラチャレンジ）
            now_bankara = bankara[0]
            next_bankara = bankara[1]

            bankara_now_rule = now_bankara.get("rule", {}).get("name", "不明")
            bankara_now_maps = [stage.get("name", "不明") for stage in now_bankara.get("stages", [])]

            bankara_next_rule = next_bankara.get("rule", {}).get("name", "不明")
            bankara_next_maps = [stage.get("name", "不明") for stage in next_bankara.get("stages", [])]

            message_lines.append(
                f"現在のガチマッチは、{bankara_now_rule}。ステージは、{bankara_now_maps[0]} と {bankara_now_maps[1]}。\n"
                f"次の更新は、{next_time_str}で"
                f"{bankara_next_rule}。ステージは、{bankara_next_maps[0]} と {bankara_next_maps[1]}。"
                f"今のナワバリバトルは、{now_rule}。ステージは、{now_maps[0]} と {now_maps[1]} です。\n"
            )
        # メッセージ送信と読み上げ
        full_message = "\n".join(message_lines)
        await speak_text(full_message, vc)
        await target_channel.send(full_message)

    except Exception as e:
        await ctx.send(f"❌ 取得に失敗しました: {e}")
        print(f"[ERROR] .match コマンド: {e}")
