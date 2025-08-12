# 全然わからん（泣）
import sys

def main():
    T = sys.stdin.readline().strip()  # 英小文字と?からなる文字列
    U = sys.stdin.readline().strip()  # 英小文字のみの文字列

    n, m = len(T), len(U)
    # U を T のどこに重ねられるか全探索
    for i in range(n - m + 1):
        ok = True
        for j in range(m):
            # T のこの位置が '?' ならどの文字でもよい（U[j]に合わせられる）
            # '?' でないなら、T[i+j] と U[j] が一致している必要がある
            if T[i + j] != '?' and T[i + j] != U[j]:
                ok = False
                break
        if ok:
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()
