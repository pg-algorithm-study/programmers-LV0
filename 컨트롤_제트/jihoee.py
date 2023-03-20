def solution(s):
    sum = 0

    stack = list(s.split())

    for i in range(0, len(stack)):
        if stack[i] == 'Z':
            sum -= int(stack[i-1])
        else:
            sum += int(stack[i])

    return sum

#####################################


def solution(s):
    stack = []
    
    s = list(s.split())
    for i in s:
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))
    
    return sum(stack)