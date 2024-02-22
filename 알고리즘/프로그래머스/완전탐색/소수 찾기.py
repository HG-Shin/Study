from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False   
    return True

def solution(numbers):
    num_list = list(numbers)
    answer = set()
    
    for i in range(1, len(num_list)+1):
        pm = permutations(num_list, i)
        for p in pm:
            num = int(''.join(p))
            if is_prime(num):
                answer.add(num)
                
    return len(answer)