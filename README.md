# Discord TTS Bot

テキストチャットに入力された内容をボイスチャンネルで読み上げる Discord ボットだよ！  
簡単にカスタマイズできるし、コマンドやイベントを追加して機能を拡張できるよ～！

---

## ✅ 開発環境セットアップ（Windows + VSCode）

### 1. Python のインストール

推奨バージョン: Python 3.10.x

[公式サイト](https://www.python.org/downloads/) からインストールしてね！  
インストール時に「Add Python to PATH」にチェックを入れるのを忘れないで！

---

### 2. 仮想環境の作成と有効化

```bash
# プロジェクトディレクトリ内で実行
python -m venv venv

# 仮想環境を有効化（PowerShell）
.\venv\Scripts\activate
```

---

### 3. 依存パッケージのインストール

以下のコマンドで必要なパッケージをインストールしてね：

```bash
pip install -r requirements.txt
```

---

### 4. .env ファイルの作成

プロジェクトルートに `.env` ファイルを作成して、以下の内容を記入してね：

```
DISCORD_TOKEN=あなたのDiscordBotトークン
DEFAULT_READ_CHANNEL_ID=読み上げ対象のテキストチャンネルID
```

---

### 5. ffmpeg のインストール

音声再生に必要な ffmpeg を以下からダウンロードしてね：

[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) → Essentials build

解凍した `bin` フォルダ（例：`C:\ffmpeg\bin`）をシステム環境変数 `Path` に追加するのを忘れないで！

---

## 🚀 実行方法

仮想環境を有効化した上で以下を実行してね：

```bash
python application.py
```

---

## 📂 ディレクトリ構成

```
discord-voice-reader/
├── bot/                # Botのメインロジック
│   ├── __init__.py     # パッケージ化用（空でOK）
│   ├── commands/       # コマンド関連の処理
│   │   ├── __init__.py
│   │   ├── join.py     # `.join` コマンド
│   │   ├── bye.py      # `.bye` コマンド
│   │   └── setchannel.py # `.setchannel` コマンド
│   ├── events/         # イベントハンドラー
│   │   ├── __init__.py
│   │   ├── on_ready.py  # `on_ready` イベント
│   │   ├── on_message.py # `on_message` イベント
│   │   └── on_voice_state_update.py # `on_voice_state_update` イベント
│   ├── utils/          # ユーティリティ関数
│   │   ├── __init__.py
│   │   ├── tts.py      # 音声合成関連
│   │   └── channel.py  # チャンネル関連の処理
├── watcher/            # 開発用のコード変更監視
│   ├── watcher.py      # ファイル変更時にBotを再起動
├── config/             # 設定ファイル
│   ├── __init__.py
│   └── settings.py     # 環境変数や設定値の管理
├── application.py      # エントリーポイント
├── requirements.txt    # 必要なPythonパッケージ
├── .env                # 環境変数（トークンやチャンネルID）
├── .gitignore          # Gitで無視するファイル
└── README.md           # プロジェクトの説明
```

---

## 🛠 コマンド一覧

- **`.join`**：VCに接続し、チャット内容を読み上げ開始
- **`.bye`**：VCから退出
- **`.setchannel [チャンネルID]`**：読み上げ対象のテキストチャンネルを変更

---

## 📦 拡張性

- **コマンドの追加**:
  - `bot/commands/` に新しいファイルを作成して、コマンドを実装するだけで簡単に追加可能！
- **イベントの追加**:
  - `bot/events/` に新しいファイルを作成して、イベントハンドラーを実装。
- **ユーティリティ関数の追加**:
  - `bot/utils/` に関数を追加して、再利用性を高める。

---

## 📝 注意事項

- `.env` ファイルには、以下のように Bot トークンやチャンネル ID を記載してね：
  ```
  DISCORD_TOKEN=あなたのDiscordBotトークン
  DEFAULT_READ_CHANNEL_ID=読み上げ対象のテキストチャンネルID
  ```
- `ffmpeg` をインストールし、システム環境変数にパスを追加してね。

---