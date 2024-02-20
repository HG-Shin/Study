def solution(number, k):
    stack = []
    arr = list(number)
    
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
            continue
        if k > 0:
            while stack[-1] < i:
                stack.pop()
                k -= 1
                if len(stack) == 0 or k <= 0:
                    break
        stack.append(i)

    stack = stack[:-k] if k > 0 else stack
    
    return ''.join(stack)