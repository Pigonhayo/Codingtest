# 백준 7576 토마토
# 큐이기 때문에 1인아이 먼저 큐에 넣고 익게한 토마토도 그 다음에 큐에 넣음 (처음에 1인 애 찾기 위해 for문, 근데 여기서 BFS는 쓰이지 않음)
# 만약 시작점이 여러개라면 보드에 있는 모든 1을 큐에 넣고 시작!!
# 큐 넣고 BFS 돌리면서 익게 함

from collections import deque
import sys

m, n = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1] # 행 이동 오른쪽 → 아래 → 왼쪽 → 위
dy = [1, 0, -1, 0] # 열 이동
Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j)) 
            
while Q:
    cur_x, cur_y = Q.popleft()
    
    for dir in range(4): 
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 0:
            # 새로 익는 토마토의 값은 현재 토마토의 일 수 + 1
            board[nx][ny] = board[cur_x][cur_y] + 1 
            Q.append((nx, ny))

max_day = 0 # 가장 늦게 익는 토마토의 일 수 (결과적으로 최소 일수가 됨)
is_possible = True # 모든 토마토가 익었는지 여부

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            # 0이 남아있으면 모든 토마토를 익힐 수 없는 상황입니다.
            is_possible = False
            break
        # 익은 토마토들 중에서 가장 큰 값(가장 늦게 익은 일 수)을 찾습니다.
        max_day = max(max_day, board[i][j])
    if not is_possible:
        break

if not is_possible:
    # 익지 않은 토마토(0)가 남아 있다면, -1 출력
    print(-1)
else:
    # board에 기록된 값은 1부터 시작하므로, 실제 걸린 일 수는 '가장 큰 값 - 1'
    print(max_day - 1)
