def solution(n):
    return sum([i for i in range(2, n+1) if i % 2 == 0])
    return sum([i for i in range(2, n+1, 2)])