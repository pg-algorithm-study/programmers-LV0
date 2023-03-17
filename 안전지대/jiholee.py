# https://school.programmers.co.kr/learn/courses/30/lessons/120866
from collections import deque
q = deque()
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

def bomb(vis, board, n, answer):
    while q:
        x, y = q.popleft()
        
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] or vis[nx][ny]:
                continue
            vis[nx][ny] = 1
            answer += 1
    return answer
    

def solution(board):
    answer = 0
    n = len(board)
    vis = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                q.append([i,j])
                vis[i][j] = 1
                answer += 1
    return n*n - bomb(vis, board, n, answer)
    