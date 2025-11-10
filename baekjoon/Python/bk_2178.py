from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    
# vis 배열을 N x M 크기로 동적 설정하고 거리를 저장하기 위해 0으로 초기화
vis = [[0] * M for _ in range(N)] 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Q = deque()
# 시작점 (0, 0)의 거리를 1로 설정
vis[0][0] = 1 
Q.append((0, 0))

while Q:
    cur_x, cur_y = Q.popleft()
    
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        # 범위 체크 (소문자 n, m 대신 N, M 사용)
        if nx < 0 or nx >= N or ny < 0 or ny >= M: 
            continue
            
        # 이동 불가능 칸 (0) 체크
        if board[nx][ny] != 1:
            continue
            
        # 방문 여부 체크 (0이면 미방문)
        if vis[nx][ny] != 0:
            continue
            
        # 거리 기록 및 큐에 추가
        vis[nx][ny] = vis[cur_x][cur_y] + 1
        Q.append((nx, ny))
    
# 도착점 (N-1, M-1)의 최소 거리를 출력
print(vis[N-1][M-1])