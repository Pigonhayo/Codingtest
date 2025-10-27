# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

N = int(input())
MOD = 10007

# DP 테이블 초기화
D = [0] * (N + 2)
D[0] = 1
D[1] = 1  

for i in range(2, N + 1):
    D[i] = (D[i - 1] + 2 * D[i - 2]) % MOD

print(D[N] % MOD)
