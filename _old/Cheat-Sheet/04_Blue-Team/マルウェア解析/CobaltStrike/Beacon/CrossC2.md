
## アンパック手順

正しく展開するには以下のようにします。

1. 末尾コンフィグの位置を特定して削除
- CrossC2 のコンフィグは固定サイズではなく、生成時の設定に依存
- 通常は Beacon 本体の末尾にシグネチャ的な文字列や構造体があるので、そこを境に切り取る

2. UPX で解凍
```bash
upx -d beacon_no_config.bin -o beacon_unpacked.bin
```

3. 展開後のバイナリ末尾に元のコンフィグを再度結合
```bash
cat beacon_unpacked.bin config_data.bin > beacon_final.bin
```
こうすることで、元と同じ動作をするアンパック済み Beacon が得られます。

4. セキュリティ上の注意
- アンパックした Beacon を実際に実行すると、正規の TeamServer に接続を試みますので、実運用環境では絶対に実行しないこと
- 解析は オフライン・隔離環境（VM、ネットワーク遮断）で行うこと
- コンフィグのフォーマットは CrossC2 や Beacon のバージョンで変わるため、解析スクリプトは都度調整が必要

## アンパック後の解析フロー

1. UPXアンパック済みBeaconを取得
- 末尾のコンフィグを削除
- upx -d で展開
- コンフィグを再付与（動作確認用） or 付与せず（静的解析用）

2. 静的解析（逆アセンブル・逆コンパイル）
- IDA Pro / Ghidra / Radare2 などに読み込む
- 関数テーブル、API呼び出し、文字列、暗号ルーチンの特定
- 特に WinInet / WinHTTP / WSA 系 API 呼び出しを重点的に見る（C2通信部）

3. コンフィグ解析
- 末尾のバイナリデータを切り出して独立解析
- 通信先IP/ドメイン、ポート、プロトコル、暗号鍵などを抽出
- これにより C2サーバや通信方式が特定できる

4. 動的解析（必要な場合）
- 完全に隔離されたVM（ネットワークは偽装C2サーバにのみ接続）で実行
- API Hook（API Monitor / x64dbg）で実行時のC2通信をキャプチャ
- SysmonやProcmonでプロセスのファイル・レジストリ操作を確認

ポイント
- アンパック前に逆アセンブリすると、UPXのデコードルーチンばかりで本体ロジックが見えません
→ 必ずアンパック後に解析
- CrossC2 Beacon はCobalt Strikeベースなので、内部構造はBeaconに近いが、関数オフセットや文字列配置が異なることがあります
- コンフィグの暗号化/難読化がかかっている場合は、Beacon本体のデコード関数を特定し、逆アセンブルで復号ロジックを抽出します

## 自動切り分け再編集スクリプト
CrossC2 の末尾コンフィグを自動検出 → 切り出し → UPXアンパック → コンフィグ再付与までワンコマンドで行うPythonスクリプト
### スクリプト仕様
- 入力: CrossC2生成のBeaconファイル（beacon.bin）
- 処理内容:
  1. ファイル末尾からコンフィグ境界を検出（マジックバイトを利用）
  2. 本体とコンフィグを分離
  3. 本体を一時ファイルとして保存し、upx -d で解凍
  4. 解凍後にコンフィグを末尾に再付与
- 出力:
  - beacon_no_config.bin（UPX解凍前の本体）
  - config_data.bin（コンフィグ）
  - beacon_unpacked.bin（UPX解凍済み＋コンフィグ再付与）

```python
import os
import subprocess

# === 設定 ===
INPUT_FILE = "beacon.bin"
CONFIG_MAGIC = b"\x00\x01\x00\x00"  # CrossC2末尾付近でよく見られるパターン（要調整）
TEMP_NO_CONFIG = "beacon_no_config.bin"
CONFIG_FILE = "config_data.bin"
OUTPUT_FILE = "beacon_unpacked.bin"

def find_config_offset(data):
    # マジックバイトで末尾コンフィグの開始位置を探す
    idx = data.rfind(CONFIG_MAGIC)
    if idx == -1:
        raise ValueError("コンフィグ境界が見つかりません")
    return idx

def main():
    with open(INPUT_FILE, "rb") as f:
        data = f.read()

    # コンフィグ位置検出
    offset = find_config_offset(data)
    print(f"[+] コンフィグ開始オフセット: {offset} (0x{offset:X})")

    # 分割保存
    beacon_core = data[:offset]
    config_data = data[offset:]
    with open(TEMP_NO_CONFIG, "wb") as f:
        f.write(beacon_core)
    with open(CONFIG_FILE, "wb") as f:
        f.write(config_data)
    print("[+] 本体とコンフィグを分離しました")

    # UPXアンパック
    print("[+] UPXで解凍中...")
    subprocess.run(["upx", "-d", TEMP_NO_CONFIG], check=True)

    # 再結合
    with open(TEMP_NO_CONFIG, "rb") as f:
        unpacked_data = f.read()
    with open(OUTPUT_FILE, "wb") as f:
        f.write(unpacked_data + config_data)
    print(f"[+] 完了: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

```
## 注意点
- CONFIG_MAGIC は CrossC2 のバージョンや設定によって変わる可能性があります
→ 実際のサンプルに合わせて調整が必要です
- このスクリプトは解析用であり、絶対に実行しないこと（隔離環境必須）
- upx コマンドは事前にインストールしておく必要があります