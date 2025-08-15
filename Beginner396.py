Q = int(input())
card = [0] * 100

for _ in range(Q):
  query = input().split()
  if query[0] == "1":
    card.append(query[1])
  else:
    print(card.pop())
