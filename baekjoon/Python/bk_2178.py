from collections import deque
import sys

# N과 M 입력
N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    # 공백 없이 붙은 문자열을 읽고 각 문자를 정수로 변환하여 리스트에 저장
    line = sys.stdin.readline().strip()
    row = list(map(int, list(line)))
    board.append(row)
    
vis = [[0] * M for _ in range(N)] 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Q = deque()
vis[0][0] = 1 
Q.append((0, 0))

while Q:
    cur_x, cur_y = Q.popleft()
    
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: 
            continue
            
        if board[nx][ny] != 1:
            continue
            
        if vis[nx][ny] != 0:
            continue
            
        vis[nx][ny] = vis[cur_x][cur_y] + 1
        Q.append((nx, ny))
    
print(vis[N-1][M-1])