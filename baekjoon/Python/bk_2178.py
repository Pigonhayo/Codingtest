from collections import deque
import sys

# N과 M 입력은 그대로 (예: 4 5)
N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
	
vis = [[False] * 502 for _ in range(502)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1,0]

Q = deque()
vis[0][0] = True
Q.append((0, 0))

while Q:
	cur = Q.popleft()
	for dir in range(4):
		nx = cur[0] + dx[dir]
		ny = cur[1] + dy[dir]

	if nx < 0 or nx >= n or ny < 0 or ny >= m:	
		continue
	if vis[nx][ny] or board[nx][ny] != 1:
		continue
	vis[nx][ny] = vis[cur[0]][cur[1]] + 1

	Q.append((nx, ny))


print(vis[i][j] -1 , end = " ")