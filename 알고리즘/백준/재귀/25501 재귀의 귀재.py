def recursion(s, l, r):
    global re_count
    re_count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
word = []
re_count = 0

for i in range(n):
    word.append(input())

for w in word:
    print(isPalindrome(w), re_count)
    re_count = 0