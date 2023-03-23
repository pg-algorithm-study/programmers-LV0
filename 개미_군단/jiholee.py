def solution(hp):
    answer = 0  
    for ant in [5, 3, 1]:
        cnt, hp = divmod(hp, ant)
        answer += cnt
    
    return answer

#################

def solution(hp):
    return (hp // 5) + (hp % 5 // 3) + (hp % 5 % 3)