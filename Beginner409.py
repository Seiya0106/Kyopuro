import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

A.sort()
A.reverse()

top = 0
for i in range(N):
    if A[i] >= i + 1:
        top = i + 1
    else:
        break

print(top)
