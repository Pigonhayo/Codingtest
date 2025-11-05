import java.util.*;

public class bk_1149 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] cost = new int[N + 1][3];
        int[][] dp = new int[N + 1][3];

        // 입력 받기
        for (int i = 1; i <= N; i++) {
            cost[i][0] = sc.nextInt(); // R
            cost[i][1] = sc.nextInt(); // G
            cost[i][2] = sc.nextInt(); // B
        }

        // 초기값 설정
        dp[1][0] = cost[1][0];
        dp[1][1] = cost[1][1];
        dp[1][2] = cost[1][2];

        // DP 진행
        for (int i = 2; i <= N; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1];
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2];
        }

        // 결과 출력
        int answer = Math.min(dp[N][0], Math.min(dp[N][1], dp[N][2]));
        System.out.println(answer);
    }
}




