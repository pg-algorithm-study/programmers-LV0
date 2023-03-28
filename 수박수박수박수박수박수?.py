def solution(n):
    res = ''
    for i in range(n):
        res += '수' if i % 2 == 0 else '박'
    return res
  
########

def solution(n):
    return ''.join(['수박'[i%2] for i in range(n)])
