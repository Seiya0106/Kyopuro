X, Y = map(int, input().split())
count = 0
for i in range(1, 7):
  for j in range(1, 7):
    total = i + j
    if i > j:
      sub = i - j
    else:
      sub = j - i
    if total >= X or sub >= Y:
      count += 1
print(count / 36)
