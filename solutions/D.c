#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

static inline int min_int(int a, int b) {
    return a < b ? a : b;
}

int main(void) {
    int n, m, d;
    if (scanf("%d %d %d", &n, &m, &d) != 3) {
        return 1;
    }

    char **grid = malloc(n * sizeof(char *));
    if (!grid) return 1;
    for (int i = 0; i < n; i++) {
        grid[i] = malloc((m + 1) * sizeof(char));
        if (!grid[i]) return 1;
        scanf("%s", grid[i]);
    }

    int **dist = malloc(n * sizeof(int *));
    if (!dist) return 1;
    for (int i = 0; i < n; i++) {
        dist[i] = malloc(m * sizeof(int));
        if (!dist[i]) return 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char ch = grid[i][j];
            if (ch == 'X' || ch == 'x') {
                dist[i][j] = 0;
            } else {
                dist[i][j] = n + m;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i > 0) {
                dist[i][j] = min_int(dist[i][j], dist[i-1][j] + 1);
            }
            if (j > 0) {
                dist[i][j] = min_int(dist[i][j], dist[i][j-1] + 1);
            }
        }
    }

    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (i < n - 1) {
                dist[i][j] = min_int(dist[i][j], dist[i+1][j] + 1);
            }
            if (j < m - 1) {
                dist[i][j] = min_int(dist[i][j], dist[i][j+1] + 1);
            }
        }
    }

    int **dp = malloc(n * sizeof(int *));
    if (!dp) return 1;
    for (int i = 0; i < n; i++) {
        dp[i] = malloc(m * sizeof(int));
        if (!dp[i]) return 1;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int allowed = (dist[i][j] >= d) ? 1 : 0;
            if (i == 0 || j == 0) {
                dp[i][j] = allowed;
            } else if (allowed) {
                int min_val = dp[i-1][j];
                if (dp[i][j-1] < min_val)
                    min_val = dp[i][j-1];
                if (dp[i-1][j-1] < min_val)
                    min_val = dp[i-1][j-1];
                dp[i][j] = min_val + 1;
            } else {
                dp[i][j] = 0;
            }
            if (dp[i][j] > ans)
                ans = dp[i][j];
        }
    }

    printf("%d\n", ans);

    for (int i = 0; i < n; i++) {
        free(grid[i]);
        free(dist[i]);
        free(dp[i]);
    }
    free(grid);
    free(dist);
    free(dp);

    return 0;
}
