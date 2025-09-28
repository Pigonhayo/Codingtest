# 점화식 생각
# 테스트 케이스 처리 (join 사용) 

import sys

input = sys.stdin.readline

MAX_N = 10
D = [0] * (MAX_N + 1)

D[1] = 1  
D[2] = 2  
D[3] = 4

for i in range(4, MAX_N + 1):
    D[i] = D[i-1] + D[i-2] + D[i-3]

T = int(input())

results = []
for _ in range(T):
    n = int(input())
    results.append(D[n])

sys.stdout.write('\n'.join(map(str, results)) + '\n')