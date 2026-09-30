class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def rec(i, cur_amt):
            if cur_amt == amount:
                return 1
            if cur_amt > amount:
                return 0
            if dp.get((i,cur_amt)) is not None:
                return dp[(i, cur_amt)]
            
            temp = 0

            for j in range(i, len(coins)):
                temp += rec(j, cur_amt+coins[j])
            dp[(i, cur_amt)] = temp
            return temp
        
        return rec(0, 0)

        