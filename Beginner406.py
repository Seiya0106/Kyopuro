N, K = map(int, input().split())
A = list(map(int, input().split()))
calc = 1

for num in A:
  calc *= num
  if calc >= 10 ** K:
    calc = 1
    
print(calc)
