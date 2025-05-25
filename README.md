Discord TTS Bot

テキストチャットに入力された内容をボイスチャンネルで読み上げる Discord ボットです。

✅ 開発環境セットアップ（Windows + VSCode）

1. Python のインストール

推奨バージョン: Python 3.10.x

https://www.python.org/downloads/ よりインストール

インストール時に「Add Python to PATH」にチェックを入れる

2. 仮想環境の作成と有効化

# プロジェクトディレクトリ内で実行
python -m venv venv

# 仮想環境を有効化（PowerShell）
.\venv\Scripts\activate

3. 依存パッケージのインストール

pip install -r requirements.txt

または個別に：

pip install discord.py gTTS python-dotenv

4. .env ファイルの作成

.env ファイルをプロジェクトルートに作成し、以下の内容を記入：

DISCORD_TOKEN=あなたのDiscordBotトークン
DEFAULT_READ_CHANNEL_ID=読み上げ対象のテキストチャンネルID

.env.example をテンプレートとして同梱しておくと親切です。

5. ffmpeg のインストール

音声再生に必要な ffmpeg を以下よりダウンロード：

https://www.gyan.dev/ffmpeg/builds/ → Essentials build

解凍した bin フォルダ（例：C:\ffmpeg\bin）をシステム環境変数 Path に追加

🚀 実行方法

# 仮想環境を有効化した上で
python bot/main.py

📦 ディレクトリ構成（例）

discord-tts-bot/
├── bot/
│   └── main.py
├── venv/
├── .env
├── .env.example
├── requirements.txt
└── README.md

🛠 コマンド一覧

.join：VCに接続し、チャット内容を読み上げ開始

.bye：VCから退出

.setchannel [チャンネルID]：読み上げ対象のテキストチャンネルを変更