def main():
    n = int(input())
    dp = [[0] * 3 for _ in range(n + 1)]

    ans = [list(map(int, input().split())) for _ in range(n)]

    def chmax(a, b):
        if a > b:
            return a
        return b

    for i in range(n):
        for l in range(3):
            for k in range(3):
                if l != k:
                    dp[i + 1][k] = chmax(dp[i + 1][k], dp[i][l] + ans[i][k])

    print(max(dp[n]))

if __name__ == "__main__":
    main()

