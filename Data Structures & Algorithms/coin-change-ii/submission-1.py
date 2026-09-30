class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def rec(i, cur_amt):
            if cur_amt == amount:
                return 1
            if cur_amt > amount:
                return 0
            if i >= len(coins):
                return 0
            if dp.get((i,cur_amt)) is not None:
                return dp[(i, cur_amt)]
            # take coin
            a = rec(i, cur_amt+coins[i])
            b = rec(i + 1, cur_amt)
            dp[(i, cur_amt)] = a+b
            return a+b


        return rec(0, 0)

        