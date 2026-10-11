def solution(left, right):
    answer = 0
    
    def divisor(n):
        div = 1
        num = 0
        while div <= n:
            if n%div == 0:
                num +=1
            div+=1
        return num
    
    for i in range(left, right+1):
        if divisor(i) %2 == 0:
            answer += i
        else:
            answer -= i
    
            
    return answer