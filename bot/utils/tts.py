from gtts import gTTS
import tempfile
import os
import discord
import asyncio

async def speak_text(text, vc):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang='ja')
        tts.save(fp.name)
        source = discord.FFmpegPCMAudio(fp.name)
        vc.play(source, after=lambda e: os.remove(fp.name))
        while vc.is_playing():
            await asyncio.sleep(1)