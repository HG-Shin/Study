def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    for i in range(len(answers)):
        i1 = i % 5
        i2 = i % 8
        i3 = i % 10
        
        if num1[i1] == answers[i]:
            c1 += 1
        if num2[i2] == answers[i]:
            c2 += 1
        if num3[i3] == answers[i]:
            c3 += 1
            
    max_c = max(c1, c2, c3)
    answer = []
    
    if max_c == c1:
        answer.append(1)
    if max_c == c2:
        answer.append(2)
    if max_c == c3:
        answer.append(3)
        
    return answer