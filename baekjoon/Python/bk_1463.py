# D 배열 선언 먼저 이는 필요한 최소 연산 횟수가 있는 배열임
# 인덱스는 0 사용안하니까 N+1 크기로 만들었음 (0으로 초기화)

import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())

D = [0] * (N + 1)

for i in range(2, N+1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)

print(D[N])