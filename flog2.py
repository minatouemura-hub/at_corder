def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    dp = [float("inf")]*n

    dp[0] = 0

    def chmin(a,b):
        if a > b:
            return b
        return a
    
    for i in range(n):
        for l in range(1,k+1):
            if i+l < n:
                dp[i+l] = chmin(dp[i+l],dp[i]+abs(h[i]-h[i+l]))
    
    print(dp[n-1])
if __name__ == "__main__":
    main()