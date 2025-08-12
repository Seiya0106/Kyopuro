# 全然わからん（泣）
N = int(input())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

def rot90(grid):
    # 90度時計回り回転（各行を文字列で返す）
    return [''.join(row) for row in zip(*grid[::-1])]

def count_diff(A, B):
    # 同じ位置の文字の相違数（ハミング距離の2次元版）
    return sum(a != b for ra, rb in zip(A, B) for a, b in zip(ra, rb))

ans = 10**9
cur = S
for k in range(4):
    ans = min(ans, count_diff(cur, T) + k)
    cur = rot90(cur)

print(ans)
