def solution(n):
    answer = 2
    
    while True:
        if (n-1) % answer == 0:
            break
        answer += 1
        
    return answer