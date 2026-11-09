def solution(want, number, discount):
    answer=0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        event_dict = {}
        for j in range(i, i+10):
            if discount[j] not in want_dict:
                break
            key = discount[j]
            event_dict[key] = event_dict.get(key, 0) + 1
            
        if event_dict == want_dict:
            answer += 1
            
        
    return answer