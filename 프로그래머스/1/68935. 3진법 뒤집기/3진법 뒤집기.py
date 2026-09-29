def solution(n):
    answer = 0
    base_3 = []
    while n > 0:
        base_3.append(n % 3)
        n = n // 3
    
    length = len(base_3)

    for i in range(0,length):
        answer += base_3[length-i-1] * (3 ** (i))
        
    return answer