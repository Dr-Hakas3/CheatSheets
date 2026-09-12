---
title: Wi-FI Password Viewer Japanese Windows Version
parent: Python
grand_parent: Programming
---
```python
import subprocess

# Wi-Fiプロファイル一覧を取得
profiles_raw = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"]
)

profiles = profiles_raw.decode("utf-8")

names = []

for line in profiles.splitlines():
    if ":" in line:
        name = line.split(":", 1)[1].strip()

        # Wi-Fiプロファイル名らしい行だけ取得
        if name and name != "<なし>":
            names.append(name)

if not names:
    print("Wi-Fiプロファイルが見つかりませんでした。")
    exit()

print("保存されているWi-Fiプロファイル:")
print()

for i, name in enumerate(names, 1):
    print(f"[{i}] {name}")

ch = int(input("\nChoose WiFi number: "))

if ch < 1 or ch > len(names):
    print("番号が正しくありません。")
    exit()

wifi = names[ch - 1]

print(f"\n選択したWi-Fi: {wifi}")

result_raw = subprocess.check_output(
    ["netsh", "wlan", "show", "profile", wifi, "key=clear"]
)

result = result_raw.decode("utf-8", errors="replace")

print("\n" + result)
```