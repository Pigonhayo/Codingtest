# 점화식 생각

import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())

D = [0] * (N + 1)

D[0] = 2
D[1] = 3
D[2] = 5

for i in range(3, N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N] % 10007)
