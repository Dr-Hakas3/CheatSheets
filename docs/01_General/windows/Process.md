## プロセス確認
#### tasklist

### プロパティの確認方法

1. Get-Member を使用する
```bash
Get-Process | Get-Member
```

2. Select-Object -Property * を使用する
```bash
Get-Process | Select-Object -First 1 -Property *
```

### プロパティを確認してからの使用例

- 例1: Get-Process のプロパティを使用する
```bash
Get-Process | Select-Object -Property Name, CPU
```

- 例2: Where-Object で条件を指定する
```bash
Get-Process | Where-Object -FilterScript { $_.CPU -gt 0.1 }
```