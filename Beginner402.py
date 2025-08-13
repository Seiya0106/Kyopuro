Q = int(input())
wait = []

for i in range(Q):
  query = list(map(int, input().split()))
  if len(query) == 2:
    wait.append(query[1])
  else:
    print(wait[0])
    wait.pop(0)
