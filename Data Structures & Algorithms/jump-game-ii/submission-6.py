class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[x] = 1 + min(dp[i]) // dp[i] is list of all probable range jumps

        n = len(nums)
        dp = [0] * n
        dp[n-1] = 0

        for i in range(n-2,-1,-1):
            prob_jumps = []

            for j in range(i+1, i+nums[i]+1):
                if j >= n:
                    continue
                prob_jumps.append(dp[j])
            print(prob_jumps)

            if len(prob_jumps) == 0:
                prob_jumps.append(float('inf'))

            min_j = min(prob_jumps)
            dp[i] = 1 + min_j

        print(dp)
        return dp[0]

        