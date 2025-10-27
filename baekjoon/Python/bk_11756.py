# 점화식 생각
# 끝이 1 x 2 두개로 끝나는 경우, 2 x 1 한개로 끝나는 경우 생각
# 

import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())

D = [0] * (N + 1)

D[0] = 2
D[1] = 3

for i in range(2, N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N] % 10007)
