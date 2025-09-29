S = input()
max = 0
for i in range(len(S)):
    for j in range(len(S), 0, -1):
        R = S[i:j]
        reverse = R[::-1]
        if R == reverse and max < len(R):
            max = len(R)
if max <= 0:
    print(1)
else:
    print(max)
