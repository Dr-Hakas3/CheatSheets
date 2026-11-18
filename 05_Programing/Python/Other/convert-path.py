import re
from pathlib import Path
from urllib.parse import unquote

root = Path(".")

pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

count = 0

for md in root.rglob("*.md"):
    content = md.read_text(encoding="utf-8")

    def replace(match):
        global count

        alt = match.group(1)
        path = unquote(match.group(2))

        filename = Path(path).name

        # Pasted image のPNGだけを対象にする
        if filename.startswith("Pasted image ") and filename.lower().endswith(".png"):
            count += 1
            return f"![[{filename}]]"

        return match.group(0)

    new_content = pattern.sub(replace, content)

    if new_content != content:
        md.write_text(new_content, encoding="utf-8")
        print(f"[+] {md}")

print(f"\n変換完了: {count} 件")