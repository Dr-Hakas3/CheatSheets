
import re
from pathlib import Path
from urllib.parse import unquote

root = Path(".")
pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

count = 0
errors = 0

for md in root.rglob("*.md"):
    if any(p in {".git", "node_modules", "public"} for p in md.parts):
        continue

    try:
        content = md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"[!] UTF-8以外のためスキップ: {md}")
        errors += 1
        continue

    def replace(match):
        global count

        path = unquote(match.group(2))
        filename = Path(path).name

        if filename.startswith("Pasted image ") and filename.lower().endswith(".png"):
            count += 1
            return f"![[{filename}]]"

        return match.group(0)

    new_content = pattern.sub(replace, content)

    if new_content != content:
        md.write_text(new_content, encoding="utf-8")
        print(f"[+] {md}")

print(f"\n変換完了: {count} 件")
print(f"文字コードエラーによるスキップ: {errors} 件")
