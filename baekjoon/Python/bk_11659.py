# 입력 먼저 받고 (N과 M이 한줄에서 입력받을 수 있도록)
# 누적합 이용해보자
# N개의 수를 넣을 배열 만들자

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 만들기
prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

# M개의 구간에 대해 합 출력
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])