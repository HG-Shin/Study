def dfs(node, graph, visited, check_link):
    visited[node] = True
    cnt = 1
    
    for i in graph[node]:
        if visited[i] == False and check_link[node][i]:
            cnt += dfs(i, graph, visited, check_link)
    
    return cnt

def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n+1)]
    check_link = [[True]*(n+1) for _ in range(n+1)]
    
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:                                
        visited = [False]*(n+1)
        check_link[a][b] = False
        cnt_a = dfs(a, graph, visited, check_link) 
        cnt_b = dfs(b, graph, visited, check_link)
        check_link[a][b] = True
        
        answer = min(answer, abs(cnt_a - cnt_b))

    return answer