def solution(k, dungeons):
    n = len(dungeons)
    visited = [False]*n
    
    def dfs(k, count):
        best = count
        
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                result = dfs(k- dungeons[i][1], count + 1)
                best = max(best, result)
                visited[i] = False
        return best
    
    answer = dfs(k, 0)
    
    return answer