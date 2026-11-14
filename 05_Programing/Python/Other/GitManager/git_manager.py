import subprocess
import os

def git(cmd):                   # Gitコマンドを実行する共通関数
                                # git(["status"])とすると、内部的にはgit statusが実行される
    result = subprocess.run(    # コマンドの終了を待ち、実行結果をresult二格納する
        ["git"] + cmd,
        capture_output=True,
        text=True
    )

    print(result.stdout)        # 標準出力

    if result.stderr:
        print(result.stderr)    # 標準エラー出力

    return result.returncode    # 終了コード（通常 0 は成功）

if __name__ == "__main__":
    ret = os.system('cd /home/kali/Desktop/Study/CheatSheets/')
    print(ret)
    cmd_result = subprocess.run(['pwd'])
    print(cmd_result)

    git(["status"])
    git(["--version"])
    git(["add ."])


