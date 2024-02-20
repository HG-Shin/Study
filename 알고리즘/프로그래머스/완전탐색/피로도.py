from itertools import permutations

def solution(k, dungeons):
    result = []
    
    for dungeon in permutations(dungeons, len(dungeons)):
        count = 0
        hp = k
        
        for tmp in dungeon:
            if hp >= tmp[0]:
                hp -= tmp[1]
                count += 1
                
        result.append(count)
                   
    return max(result)