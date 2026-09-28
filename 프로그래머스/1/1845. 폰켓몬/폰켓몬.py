def solution(nums):
    answer = 0
    number = len(nums) // 2
    kinds = len(set(nums))
    
    answer = min(number, kinds)
    
    return answer