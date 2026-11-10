from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []
    for i in range(n):
        left = 100 - progresses[i]
        days.append((left + speeds[i] - 1) // speeds[i])
    
    q = deque(days)
    while q:
        standard = q.popleft()
        count = 1
        while q and q[0] <= standard:
            q.popleft()
            count += 1
        answer.append(count)
        
    return answer