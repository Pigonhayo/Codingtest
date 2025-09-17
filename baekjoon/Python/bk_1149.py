# 행렬 초기화 먼저 해보자 
# N+1을 쓴 이유는, Java 코드처럼 인덱스를 1부터 쓰기 위함
# RGB 각각 처음에 선택된 케이스 (즉 케이스가 3개)
# 마지막에 케이스 3개 비교후 min 출력

N = int(input())
cost = [[0] * 3 for _ in range(N + 1)]
dp = [[0] * 3 for _ in range(N + 1)]

# 입력 받기
for i in range(1, N + 1):
    r, g, b = map(int, input().split())
    cost[i][0] = r  # R
    cost[i][1] = g  # G
    cost[i][2] = b  # B

# 초기값 설정
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

# DP 진행
for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

# 결과 출력
answer = min(dp[N][0], dp[N][1], dp[N][2])
print(answer)
