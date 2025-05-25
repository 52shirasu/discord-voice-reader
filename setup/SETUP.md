開発環境構築手順

1. 仕様

Python 3.10+ が必要

ffmpeg が必要

Pythonの確認

python --version

ffmpegの確認

ffmpeg -version

2. 仮想環境の作成

# ルートフォルダで実行
python -m venv venv

# Windows (bash)
source venv/Scripts/activate

# macOS/Linux
source venv/bin/activate

3. 依存パッケージのインストール

pip install -r requirements.txt

4. .env ファイルの作成

.envをルート直下に作成し、以下を記述:

DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
DEFAULT_READ_CHANNEL_ID=000000000000000000  # 初期の読上げ対象チャンネルID

チャンネルIDは「デバッグモード」を有効にすることで取得可能

5. Botの起動

python bot/main.py

Botが "Bot起動完了" と表示されればOK