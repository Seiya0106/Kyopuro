N, Q = map(int, input().split())
X = list(map(int, input().split()))
result = []
box = [0] * N
count = 0

for num in X:
  if num > 0:
    result.append(num)
    box[num - 1] += 1
  else:
    min_box = box.index(min(box))
    result.append(min_box + 1)
    box[min_box] += 1

for ball in result:
  print(ball, end=" ")
print()
