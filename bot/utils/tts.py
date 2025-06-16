from gtts import gTTS
import uuid
import os

def generate_audio(text: str) -> str:
    """テキストをgTTSで音声ファイルに変換して、ファイルパスを返す"""
    path = f"temp_{uuid.uuid4().hex}.mp3"
    try:
        tts = gTTS(text=text, lang="ja")
        tts.save(path)
    except Exception as e:
        print(f"⚠️ gTTS生成エラー: {e}")
        raise e
    return path
