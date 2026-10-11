def solution(s):
    p_num = 0
    y_num = 0
    
    for a in s.lower():
        if a == 'p':
            p_num += 1
        if a == 'y':
            y_num += 1

    return p_num == y_num