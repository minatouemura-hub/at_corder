# 入力
N, W = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

# DPテーブル
dp = [[0] * (W + 1) for _ in range(N + 1)]

# DPループ
for i in range(N):
    for sum_w in range(W + 1):

        # i 番目の品物を選ぶ場合
        if sum_w - weight[i] >= 0:
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w - weight[i]] + value[i])

        # i 番目の品物を選ばない場合
        dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w])

# 最適値の出力
print(dp[N][W])
# 入力
N, W = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

# DPテーブル
dp = [[0] * (W + 1) for _ in range(N + 1)]

# DPループ
for i in range(N):
    for sum_w in range(W + 1):

        # i 番目の品物を選ぶ場合
        if sum_w - weight[i] >= 0:
            dp[i + 1][sum_w] = max(dp[i][sum_w], dp[i+1][sum_w - weight[i]] + value[i+1])

        # i 番目の品物を選ばない場合
        dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w])

# 最適値の出力
print(dp[N][W])
