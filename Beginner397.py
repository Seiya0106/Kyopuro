words = input()
count = 0
num = len(words)

for c, n in enumerate(words, 1):
   if (c + count) % 2 == 1:
      if n == "o":
         count += 1
   else:
      if n == "i":
         count += 1
if (num + count) % 2 == 1:
   count += 1
print(count)
