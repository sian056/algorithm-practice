def solution(n):
    answer = []
    
    def move(num, x, y, answer):
        if num > 1 :
            move(num-1, x, 6-x-y, answer)   # 시작 기둥에서 나머지 기둥으로
        
        answer.append([x,y])

        if num > 1 :
            move(num-1, 6-x-y, y, answer)   # 나머지 기둥에서 도착 기둥으로
        
    move(n, 1, 3, answer)
    
    return answer