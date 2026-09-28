class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = {}
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    if dp.get(i, -2) != -2 and dp.get(i - coin, -2) != -2:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    else:
                        if dp.get(i - coin, -2) != -2:
                            dp[i] = dp[i - coin] + 1

        # print(f"dp: {dp}")
        if dp.get(amount, -1) != -1:
            return dp[amount]
        else:
            return -1

        # dp[0] = 0

        # dp[1]:
        # 用 coin 1 => dp[0] + 1 = 1
        # 所以 dp[1] = 1

        # dp[2]:
        # 用 coin 1 => dp[1] + 1 = 2
        # 用 coin 2 => dp[0] + 1 = 1
        # 所以 dp[2] = 1

        # dp[3]:
        # 用 coin 1 => dp[2] + 1 = 2
        # 用 coin 2 => dp[1] + 1 = 2
        # 所以 dp[3] = 2

        # dp[4]:
        # 用 coin 1 => dp[3] + 1 = 3
        # 用 coin 2 => dp[2] + 1 = 2
        # 所以 dp[4] = 2

        # dp[5]:
        # 用 coin 1 => dp[4] + 1 = 3
        # 用 coin 2 => dp[3] + 1 = 3
        # 用 coin 5 => dp[0] + 1 = 1
        # 所以 dp[5] = 1