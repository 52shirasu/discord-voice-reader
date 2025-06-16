import asyncio
import discord
import os
from bot.utils import tts

class TTSQueue:
    def __init__(self):
        self.queues = {}   # {guild_id: asyncio.Queue}
        self.playing = {}  # {guild_id: bool}

    async def add(self, guild_id: int, text: str, vc: discord.VoiceClient):
        """読み上げテキストを再生キューに追加"""
        if guild_id not in self.queues:
            self.queues[guild_id] = asyncio.Queue()
        await self.queues[guild_id].put((text, vc))

        if not self.playing.get(guild_id, False):
            asyncio.create_task(self._play_loop(guild_id))

    async def _play_loop(self, guild_id: int):
        self.playing[guild_id] = True
        queue = self.queues[guild_id]

        while not queue.empty():
            text, vc = await queue.get()
            try:
                audio_path = tts.generate_audio(text)
                audio = discord.FFmpegPCMAudio(audio_path)

                vc.play(audio)
                while vc.is_playing():
                    await asyncio.sleep(0.5)

                os.remove(audio_path)

            except Exception as e:
                print(f"⚠️ TTS再生中にエラー: {e}")

        self.playing[guild_id] = False
