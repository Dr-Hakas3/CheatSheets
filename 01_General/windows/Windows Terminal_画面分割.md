---
title: Windows Terminal 画面分割
---

**Windows Terminalは、Linuxのターミナル（tmuxやzsh環境）のように画面を分割できます。**

![[Pasted image 20261115162125.png]]

## **1. Windows Terminalの分割方法**

[Volets du Terminal Windows | Microsoft Learn](https://images.openai.com/static-rsc-4/WxE4cGapLnYRtwCAruw-mSaPfT6XgaPoOQycyAxlSE6GaUBwUdpAmKfgyTKEvt7VeKRSLl2fGFbHZsAq9uuHdJWdNuboTpOHBc-ntOX0lbHnFALbwNBHN5LGyJHlQy5Q6JbaKNF0JG12-qeaNdb6XTNlNOaIHiBAzyOOJWz_TpI?purpose=inline)

[learn.microsoft.com](https://learn.microsoft.com/fr-fr/windows/terminal/panes?utm_source=chatgpt.com)

標準ショートカットは以下です。

|操作|ショートカット|
|---|---|
|縦分割（左右）|`Alt + Shift + +`|
|横分割（上下）|`Alt + Shift + -`|
|分割ペイン間の移動|`Alt + 矢印キー`|
|ペインを閉じる|`Ctrl + Shift + W`|
|新しいタブ|`Ctrl + Shift + T`|

※ キーボード配列によって分割ショートカットの入力が異なる場合があります。

## **2. 分割イメージ**

例えば、以下のような使い方ができます。

**Windows Terminal**

分割例

![[Pasted image 20261115162221.png]]
左右・上下を組み合わせた3ペイン構成の例

## **3. 個人的におすすめの使い方**

現在のGitHub・CheatSheets管理なら、例えば次の構成が便利です。

- 左：PowerShell（Git操作）
    
- 右上：PowerShell（Quartzビルド）
    
- 右下：Git Bash（Linux系コマンドの確認）
    

**ちなみに、Windows Terminalならタブだけでなく、1つのウィンドウ内に複数のシェルを同時表示できます。**

tmuxのようなペイン分割を使いたいなら、Windows Terminalだけで十分実現できます。

---

立ち上がってない状態からショートカットキーでターミナル起動はWindowsのショートカットキーを設定する必要がある。

## **方法：ショートカットキーを割り当てる**

1. デスクトップを右クリック →「新規作成」→「ショートカット」
    
2. 項目の場所に以下を入力
    

```
wt.exe
```

3. 名前を「Windows Terminal」にする
    
4. 作成したショートカットを右クリック →「プロパティ」
    
5. 「ショートカットキー」に好きなキーを設定
    

例えば、

```
Ctrl + Alt + T
```

6. 「適用」をクリック

これで、Windows Terminalが起動していない状態でも `Ctrl + Alt + T` で起動できる。