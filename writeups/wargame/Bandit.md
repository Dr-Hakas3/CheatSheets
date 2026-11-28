-をオプションとしない

cat -- -file07

6　 ファイルの所有者、グループ、サイズを指定

find / -user bandit7 -group bandit6 -size 33c -type f 2>/dev/null

z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

7　 ファイルから特定の文字列を含む行を抽出

grep millionth data.txt

TESKZC0XvTetK0S9xNwm25STk5iWrBvP

８　ファイル内のユニークな文字列の抽出

sort data.txt | uniq -u

-u, --unique          only print unique lines

EN632PlfYiZbn3PhVK3XOGSlNInNE00t

９　バイナリファイルの中から＝を含む可読文字の抽出

strings data.txt  | grep =

G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

１０　base64のデコード

cat data.txt | base64 -d

6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

１１　ROT13

echo WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi | tr $(printf %13s | tr ' ' '.' | tac)\a-z a-za-z | tr $( printf %13s | tr ' ' '.' | tac)\A-Z A-ZA-Z

※

別解　１(python）

echo WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi | python -c 'print(raw_input().encode("rot13"))'

別解　２(alias)

alias rot13='tr a-zA-Z n-za-mN-ZA-M'

cat data.txt | rot13

JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

１２　16進数hexdump

2  cd /tmp/ax

3  ls

4* bzip2 -d data2.

5  ls

6  file data2.out

7  gzip -d data2.oout

8  gzip -d data2.out

9  file data.txt

10  xxd -r data.txt data.out

11  file data.out

12  gzip -d data.out

13  mv data.out data.gz

14  gzip -d data.gz

15  ls

16  ls -la

17  file data

18  bzip2 -d data

19  ls

20  bzip2 -d data.out

21  ls -la

22  file data.txt

23  cat data.txt

24  xxd -r data.txt

25  xxd -r data.txt data.out

26  ls -la

27  file data.out

28  mv data.out dat.gz

29  mv dat.gz data.gz

31  gzip -d data.gz

32  ls -la

33  file data

34  bzip2 -d data

35  ls

36  ls -la

37  file data.out

38  mv data.out data.gz

39  gzip -d data.gz

40  ls

41  file data

42  tar -xf data

43  file data

44  ls

45  file data5.bin

46  tar -xf data5.bin

47  ls

48  file data6.bin

49  bzip -d data6.bin

50  bzip2 -d data6.bin

51  ls

52  file data6.bin.out

53  tar -xf data6.bin.out

54  ls

55  ls -la

56  file data8.bin

57  mv data8.bin data8.gz

58  gzip -d data8.gz

59  ls

60  file data8

61  cat data8

bandit12@bandit:/tmp/ax$ cat data8

The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw