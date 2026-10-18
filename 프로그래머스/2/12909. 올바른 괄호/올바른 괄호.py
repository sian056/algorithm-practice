def solution(s):
    stack = []
    
    for i in s:
        if stack and stack[-1] == '(':
            if i == ')':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    
    if stack:
        answer = False
    else:
        answer = True

    return answer