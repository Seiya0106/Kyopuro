N, M = map(int, input().split())
A = list(map(int, input().split()))
num = 0
flag = False

while True:
  for i in range(1, M + 1):
    if A.count(i) <= 0:
      flag = True
      break
  if flag:
    break
  num += 1
  del A[len(A) - 1]
print(num)
