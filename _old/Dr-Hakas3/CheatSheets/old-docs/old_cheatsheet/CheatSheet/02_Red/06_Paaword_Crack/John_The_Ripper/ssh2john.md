`ssh2john`は、SSHプライベートキーからJohn the Ripperが使用できる形式に変換するためのツールです。このツールを使用することで、SSHプライベートキーをクラックするためにJohn the Ripperを使えるようになります。

### 基本的な使い方

1. **SSHプライベートキーをJohn形式に変換**
   
   まず、`ssh2john`を使ってSSHプライベートキーをJohn the Ripperで扱える形式に変換します。

   ```bash
   ssh2john id_rsa > ssh_hash.txt
   ```
   - `id_rsa`: クラック対象のSSHプライベートキー。
   - `ssh_hash.txt`: 出力されるJohn形式のハッシュファイル。

2. **John the Ripperでクラック**

   変換したハッシュファイルをJohn the Ripperでクラックします。
   ```bash
   john ssh_hash.txt
   ```
   - `ssh_hash.txt`: 先ほど生成したJohn形式のハッシュファイル。

### 実際の手順

1. まず、SSHプライベートキー（例: `id_rsa`）が手元にあると仮定します。

2. `ssh2john`を使って、SSHキーをJohn形式に変換します。
   ```bash
   ssh2john id_rsa > ssh_hash.txt
   ```

3. 変換された`ssh_hash.txt`ファイルを使ってJohn the Ripperでパスワードをクラックします。
   ```bash
   john ssh_hash.txt
   ```

4. クラックされたパスワードを表示します。
   ```bash
   john --show ssh_hash.txt
   ```

### 注意点

- `ssh2john`はJohn the Ripperに含まれるスクリプトなので、John the Ripperをインストールしていれば利用可能です。
- クラックを行うには、対象のSSHキーが暗号化されている必要があります。もしキーが暗号化されていない場合、そもそもパスワードクラックの対象にはなりません。
---