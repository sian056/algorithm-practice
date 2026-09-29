def solution(k, m, score):
    new_score = sorted(score, reverse=True)
    answer = 0
    
    for i in range(m-1, len(new_score), m):
        answer += new_score[i] * m 
            
    return answer
