def fibonacci_number(n):
    if n <= 1:
        return n
    return fibonacci_number(n-1)+fibonacci_number(n-2)

n = int(input())
print(fibonacci_number(n))