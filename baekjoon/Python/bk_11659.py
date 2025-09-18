# 입력 먼저 받고 (N과 M이 한줄에서 입력받을 수 있도록)
# 누적합 이용해보자
# N개의 수를 넣을 배열 만들자

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열
prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(str(prefix[j] - prefix[i-1]))

<<<<<<< HEAD
print("\n".join(result))
=======
print("\n".join(result))
>>>>>>> ed4a5351286870e2f69a28312bad850161d97c00
