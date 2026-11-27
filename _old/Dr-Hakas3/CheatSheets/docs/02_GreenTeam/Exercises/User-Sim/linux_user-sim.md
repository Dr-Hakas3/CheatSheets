---
title: Linux User Simulation
parent: Execises
grand_parent: Green Team
---
# Web
```bash
#!/bin/bash

# Chromeの実行ファイル
CHROME="/usr/bin/google-chrome"

# アクセス先一覧
SITES=(
    "https://example.com"
    "https://www.wikipedia.org"
    "https://news.example.local"
    "https://portal.example.local"
)

while true
do
    # ランダムにサイトを選択
    INDEX=$((RANDOM % ${#SITES[@]}))
    URL="${SITES[$INDEX]}"

    echo "$(date) Access: $URL"

    # 新しいタブで開く
    $CHROME --new-tab "$URL" >/dev/null 2>&1

    # 30～300秒待機
    sleep $((RANDOM % 271 + 30))
    # Chromeを終了
    pkill -x chrome
    pkill -x google-chrome

    # 次のアクセスまで10～60秒待機
    sleep $((RANDOM % 51 + 10))
done
```

---
# Mail

## swaks

■ 単発送信スクリプト（基本形）

```bash
#!/bin/bash

FROM="user1@lab.local"
TO="user2@lab.local"
SERVER="mail.lab.local"

SUBJECT="Test mail"
BODY="Hello from swaks script"

swaks \
  --to "$TO" \
  --from "$FROM" \
  --server "$SERVER" \
  --header "Subject: $SUBJECT" \
  --body "$BODY"
```

■ ランダム送信スクリプト 「ユーザー行動模擬」に寄せたバージョン

```bash
#!/bin/bash

SERVER="mail.lab.local"
FROM_LIST=("user1@lab.local" "user2@lab.local" "user3@lab.local")
TO_LIST=("user1@lab.local" "user2@lab.local" "user3@lab.local")

SUBJECTS=("Report" "Question" "Update" "FYI")
BODIES=("Hello" "Please check" "No issues" "See attached (mock)")

# ランダム待機（人間っぽさ）
sleep $((RANDOM % 181 + 30))

FROM=${FROM_LIST[$RANDOM % ${#FROM_LIST[@]}]}
TO=${TO_LIST[$RANDOM % ${#TO_LIST[@]}]}
SUBJECT=${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}
BODY=${BODIES[$RANDOM % ${#BODIES[@]}]}

echo "$(date) sending: $FROM -> $TO"

swaks \
  --server "$SERVER" \
  --from "$FROM" \
  --to "$TO" \
  --header "Subject: $SUBJECT" \
  --body "$BODY"
```

■ 添付付き（ログっぽさ強化）

```bash
swaks \
  --server "$SERVER" \
  --from "$FROM" \
  --to "$TO" \
  --header "Subject: $SUBJECT" \
  --body "$BODY" \
  --attach-type text/plain \
  --attach @/tmp/sample.txt
```

■ 認証付きSMTP（実運用）

```bash
swaks \
  --to "$TO" \
  --from "$FROM" \
  --server "$SERVER" \
  --auth LOGIN \
  --auth-user "user1@lab.local" \
  --auth-password "password"
```

■ cronで回す例

```bash
*/10 * * * * /opt/user_sim/swaks_send.sh
```

## xdoを使用した場合

```bash
#!/bin/bash

THUNDERBIRD="thunderbird"

# 送信先リスト
RECIPIENTS=(
    "user1@lab.local"
    "user2@lab.local"
    "user3@lab.local"
    "admin@lab.local"
)

SUBJECTS=(
    "Daily report"
    "Check this"
    "Question"
    "Status update"
)

BODIES=(
    "Hello"
    "Please check."
    "This is an automated message."
    "No issues found."
)

# ランダム待機（人間っぽさ）
sleep $((RANDOM % 181 + 30))

# Thunderbird起動
$THUNDERBIRD &
TB_PID=$!

# 起動待ち
sleep 8

# ランダムに送信内容決定
TO=${RECIPIENTS[$RANDOM % ${#RECIPIENTS[@]}]}
SUBJECT=${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}
BODY=${BODIES[$RANDOM % ${#BODIES[@]}]}

# Thunderbirdフォーカス
wmctrl -a "Thunderbird" 2>/dev/null

sleep 2

# 新規メール作成（Ctrl+N）
xdotool key ctrl+n
sleep 2

# 宛先
xdotool type "$TO"
xdotool key Tab
sleep 1

# 件名
xdotool type "$SUBJECT"
xdotool key Tab
sleep 1

# 本文
xdotool type "$BODY"
sleep 1

# 送信（Ctrl+Enter）
xdotool key ctrl+Return

# 少し待機
sleep $((RANDOM % 60 + 10))

# Thunderbird終了
kill $TB_PID 2>/dev/null
wait $TB_PID 2>/dev/null
```

---

# File


■ ① シンプル版（毎ループ mount/unmount）

```bash
#!/bin/bash

SHARE="//fileserver.lab.local/share"
MOUNT="/mnt/share"
USER="user1"
PASS="password"

FILES=("a.txt" "b.txt" "c.txt" "report.docx")

while true
do
    sleep $((RANDOM % 120 + 10))

    sudo mount -t cifs $SHARE $MOUNT -o username=$USER,password=$PASS

    FILE=${FILES[$RANDOM % ${#FILES[@]}]}

    echo "$(date) access file: $FILE"

    # 読み取り
    cat "$MOUNT/$FILE" >/dev/null 2>&1

    # たまにコピー
    if (( RANDOM % 2 == 0 )); then
        cp "$MOUNT/$FILE" /tmp/
    fi

    sleep $((RANDOM % 60 + 10))

    sudo umount $MOUNT
done
```

■ ② 推奨版（mountは1回だけ・現実的）

実運用・ユーザー挙動的にはこっちが自然。

```bash
#!/bin/bash

SHARE="//fileserver.lab.local/share"
MOUNT="/mnt/share"
USER="user1"
PASS="password"

FILES=("a.txt" "b.txt" "c.txt" "report.docx")
```

```bash
# 最初だけマウント
sudo mount -t cifs $SHARE $MOUNT -o username=$USER,password=$PASS

while true
do
    sleep $((RANDOM % 120 + 10))

    FILE=${FILES[$RANDOM % ${#FILES[@]}]}

    echo "$(date) access file: $FILE"

    # 読み取り（ユーザー行動）
    cat "$MOUNT/$FILE" >/dev/null 2>&1

    # コピー（たまに）
    if (( RANDOM % 3 == 0 )); then
        cp "$MOUNT/$FILE" /tmp/
    fi

    # たまに長い離席
    sleep $((RANDOM % 300 + 20))
done
```

■ ③ さらにリアル（業務っぽさ）

追加すると一気に“人間っぽくなる要素”：

● ファイル操作の種類を増やす

```
ACTION=$((RANDOM % 3))

case $ACTION in
    0)
        cat "$MOUNT/$FILE" >/dev/null
        ;;
    1)
        cp "$MOUNT/$FILE" /tmp/
        ;;
    2)
        ls "$MOUNT" >/dev/null
        ;;
esac
● 業務時間制御
HOUR=$(date +%H)

if (( HOUR < 8 || HOUR > 19 )); then
    sleep 600
    continue
fi
```