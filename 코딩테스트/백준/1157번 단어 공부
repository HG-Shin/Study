word = input().lower()
word_set = list(set(word))
cnt = []

for i in word_set:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_set[cnt.index(max(cnt))].upper())