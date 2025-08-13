N = int(input())
P = list(map(int, input().split()))
result = [0] * N
r = 1

while True:
  top = max(P)
  k = 0
  for i in range(N):
    if P[i] == top:
      k += 1
      result[i] = r
      P[i] = 0
  r += k
  if max(P) == 0:
    break
for num in result:
  print(num)
