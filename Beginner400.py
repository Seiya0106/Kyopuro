def calc(N, M, limit=10**9):
  sum = 0
  for i in range(M + 1):
    sum += N ** i
    if sum > limit:
      print("inf")
      exit()
  return sum

N, M = map(int, input().split())
print(calc(N, M))
