Description

I created this machine to help others learn some basic CTF hacking strategies and some tools. I aimed this machine to be very similar in difficulty to those I was breaking on the OSCP.

This is a boot-to-root machine will not require any guest interaction.

There are two designed methods for privilege escalation.

- 23/09/2015 == v1.0.1
- 22/09/2015 == v1.0

If you are having issues with VirtualBox, try the following:

- Downloaded LordOfTheRoot_1.0.1.ova (confirmed file hash)
- Downloaded and installed VMWare ovftool.
- Converted the OVA to OVF using ovftool.
- Modified the OVF using text editor, and did the following:  
replaced all references to "ElementName" with "Caption" replaced the single reference to "vmware.sata.ahci" with "AHCI"
- Saved the OVF. +Deleted the .mf (Manifest) file. If you don't you get an error when importing, saying the SHA doesn't match for the OVF (I also tried modifying the hash, but no luck).
- Try import the OVF file, and it should work fine.

Source: https://twitter.com/dooktwit/status/646840273482330112

このマシンは、他の人が基本的なCTFハッキング戦略とツールを学ぶのを助けるために作成しました。このマシンは、OSCPで壊したマシンと非常によく似た難易度を目指しました。

これはブートからルートへのマシンであり、ゲストとの対話は必要ありません。

特権エスカレーションには、2 つの方法があります。

• 2015 年 9 月 23 日 == v1.0.1

• 2015 年 9 月 22 日 == v1.0

VirtualBoxに問題がある場合は、次のことを試してください。

•ダウンロードLordOfTheRoot_1.0.1.ova(確認されたファイルハッシュ)

•VMWare ovftoolをダウンロードしてインストールしました。

• ovftool を使用して OVA を OVF に変換しました。

• テキストエディタを使用してOVFを修正し、次のことを行いました。

「ElementName」へのすべての参照を「Caption」に置き換え、「vmware.sata.ahci」への単一の参照を「AHCI」に置き換えました。

• OVFを保存しました。+.mf(マニフェスト)ファイルを削除しました。そうしないと、インポート時にSHAがOVFと一致しないというエラーが発生します(ハッシュの変更も試みましたが、うまくいきませんでした)。

•OVFファイルをインポートしてみると、正常に機能するはずです。

出典:https://twitter.com/dooktwit/status/646840273482330112