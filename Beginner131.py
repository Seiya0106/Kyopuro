N, L = map(int, input().split())
apple = []
result = 0
dif = 0
ori = 0
for i in range(1, N + 1):
    apple.append(L)
    L += 1
result = sum(apple)
dif = abs(apple[0])
for j in range(1, N):
    if dif > abs(apple[j]):
        dif = abs(apple[j])
        ori = apple[j]
if ori >= 0:
    print(result - dif)
else:
    print(result + dif)
    
