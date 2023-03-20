from collections import deque
def solution(numbers, direction):
    q = deque(numbers)
    
    if direction == "right":
        q.rotate(1)
    else:
        q.rotate(-1)
    
    return list(q)