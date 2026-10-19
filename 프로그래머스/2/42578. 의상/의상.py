def solution(clothes):
    answer = 1
    numbs = {}
    for c in clothes:
        if c[1] in numbs.keys():
            numbs[c[1]] += 1
        else:
            numbs[c[1]] = 1
            
    for i in numbs.values():
        answer *= (i+1)
    
    answer = answer -1 
    return answer