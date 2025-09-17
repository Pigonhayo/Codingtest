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
