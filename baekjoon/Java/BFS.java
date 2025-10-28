import java.util.*;

public class BFS {

    public static void main(String[] args) {
        int[][] board = {
                {1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
                {1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
                {1, 1, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
        };

        boolean[][] vis = new boolean[502][502]; // nxn으로 들어올때 +2해서 잡는게 좋음. 여기서는 500
        int n = 7, m = 10;
        int[] dx = {1, 0, -1, 0}; // x 좌표에 얘를 더할거임
        int[] dy = {0, 1, 0, -1}; // 아래, 오른쪽, 위, 왼쪽 (시계반대방향)
        Deque<int[]> Q = new ArrayDeque<>();

        vis[0][0] = true;
        Q.addLast(new int[]{0, 0});

        while (!Q.isEmpty()) {
            int[] cur = Q.removeFirst(); // 지금 살펴볼 값이 cur
            System.out.print("(" + cur[0] + ", " + cur[1] + ") -> ");

            for (int dir = 0; dir < 4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (vis[nx][ny] || board[nx][ny] != 1) continue;

                vis[nx][ny] = true;
                Q.addLast(new int[]{nx, ny});
            }
        }
    }
}