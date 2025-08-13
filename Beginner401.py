N = int(input())
S = [input() for _ in range(N)]
islogin = False
count = 0

for condition in S:
  if condition == "login":
    islogin = True
  elif condition == "logout":
    islogin = False
  elif islogin == False and condition == "private":
    count += 1
print(count)
