def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []
    for i in range(n):
        left = 100 - progresses[i]
        days.append((left + speeds[i] - 1) // speeds[i])
    
    standard = 0
    for day in days:
        if standard >= day :
            answer[-1] += 1
        else:
            standard = day
            answer.append(1)
        
    return answer