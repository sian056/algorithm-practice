def solution(nums):
    answer = 0
    number = len(nums)
    kinds = len(set(nums))
    
    if number//2 > kinds:
        answer = kinds
    else:
        answer = number//2
    
    return answer