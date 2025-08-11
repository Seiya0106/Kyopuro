N = int(input())
A = list(map(int, input().split()))
result = set()
for num in A:
  result.add(num)
result_list = list(result)
result_list.sort()
  
print(len(result))
print(*result_list)
