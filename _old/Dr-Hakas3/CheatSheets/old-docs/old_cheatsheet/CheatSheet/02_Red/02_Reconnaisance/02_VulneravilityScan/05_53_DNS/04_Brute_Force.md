# DNS ブルートフォース攻撃手法の自動化
1. ホスト名リストを作成する
2. ワンライナーを使用して各ホスト名の解決
```bash
for ip in $(cat list.txt); do host $ip.megacorpone.com; done
```

# 逆引き検索 を用いてこの範囲をスキャンし、 各IPのホスト名を要求
```bash
for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not found"
```
