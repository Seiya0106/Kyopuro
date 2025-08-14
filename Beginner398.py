# AI生成
import sys
from collections import Counter

A = list(map(int, sys.stdin.read().split()))
A = A[:7]  # 念のため7個に制限

cnt = Counter(A)

vals_ge3 = [v for v, c in cnt.items() if c >= 3]
vals_ge2 = [v for v, c in cnt.items() if c >= 2]
print(vals_ge3)
print(vals_ge2)

ok = any(x != y for x in vals_ge3 for y in vals_ge2)
print("Yes" if ok else "No")
