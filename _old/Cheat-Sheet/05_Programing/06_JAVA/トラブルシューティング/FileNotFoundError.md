`FileNotFoundError: [Errno 2] No such file or directory: 'weblogic.jar'`

### ✅ 原因

スクリプトがアップロードしようとしている `weblogic.jar` ファイルが、**ビルドされていないため見つからない**。エラー①と②の影響で `jar` ファイルが作成されなかった。

---

## 🔧 解決手順

### ① Javaのバージョン確認と変更

まずは現在の `javac` のバージョンを確認：

```bash
javac -version
```
もし `javac` が `--release` オプションに `7` をサポートしていない（例：OpenJDK 8未満など）、**Java 11以降をインストールして切り替える必要があります。**

例（KaliでJava 11に切り替え）：
```bash
sudo apt install openjdk-11-jdk sudo update-alternatives --config javac
```
選択肢から `javac` 11 を選びます。

---

### ② Javaソースの場所確認

スクリプトが以下のようなディレクトリを前提にしている可能性があります：
```bash
`weblogic/jndi/SomeClass.java`
```
- スクリプトが `.java` ファイルをコンパイルして `.class` に変換し、その `.class` を `weblogic.jar` に詰める設計なら、まず `weblogic/jndi` フォルダに `.java` ファイルがあることを確認してください。
    
- もしない場合、**スクリプトが配布された場所やGitHubにある`weblogic`ディレクトリを確認**してください。
    

---

### ③ JARファイル作成が成功するか手動で試す

```
`mkdir -p weblogic/jndi # ソースファイルを置く javac --release 7 weblogic/jndi/*.java jar cvf weblogic.jar weblogic/jndi/*.class`
```
成功すれば `weblogic.jar` が生成されるはずです。

---

## 📝 まとめ

|問題|対処|
|---|---|
|`release version 7 not supported`|Javaバージョンを11以上に上げる|
|`*.class : no such file`|Javaソースファイルがない／場所が違う|
|`weblogic.jar` not found|上記エラーでJARが作れなかったため|