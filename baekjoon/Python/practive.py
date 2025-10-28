from collections import deque

board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

n, m = 7, 10
vis = [[False] * 502 for _ in range(502)]

dx = [-1, 1, 0, 0] # 상하좌우 순서대로 진행
dy = [0, 0, -1, 1]
Q = deque()

vis[0][0] = True
Q.append((0, 0))

while Q:
    cur = Q.popleft()
    print(f"({cur[0]}, {cur[1]}) -> ", end="")

    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]

        if nx < 0 or nx >=n or ny < 0 or ny >=m:
            continue
        if vis[nx][ny] or board[nx][ny] != 1:
            continue
        vis[nx][ny] = True
        Q.append((nx, ny))  

# 그림판 채우기에서 사용
