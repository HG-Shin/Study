n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_value = int(-1e9)
min_value = int(1e9)

def solve(idx, num, add, sub, mul, div):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return
    
    if add>0:
        solve(idx+1, num+nums[idx], add-1, sub, mul, div)
    if sub>0:
        solve(idx+1, num-nums[idx], add, sub-1, mul, div)
    if mul>0:
        solve(idx+1, num*nums[idx], add, sub, mul-1, div)
    if div>0:
        solve(idx+1, int(num/nums[idx]), add, sub, mul, div-1)

solve(1, nums[0], oper[0], oper[1], oper[2], oper[3])

print(max_value)
print(min_value)