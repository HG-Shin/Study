S = input()
count = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        count.add(S[i:j+1])

print(len(count))