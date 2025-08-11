from collections import deque

N = int(input())
queue = deque()
sum = 0
flag = True
for i in range(N):
  c, l = map(str, input().split())
  num = int(l)
  queue.append((c, num))
  sum += num
if flag and sum <= 100:
  for c, num in queue:
      print(c * num, end="")
  print()
else:
  print("Too Long")
