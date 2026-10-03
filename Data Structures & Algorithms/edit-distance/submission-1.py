class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def rec(i,j):
            if dp.get((i,j)) is not None:
                return dp[(i,j)]
            if j >= len(word2) and i >= len(word1):
                return 0
            

            if i >= len(word1):
                cur_1 = ""
            else:
                cur_1 = word1[i]
            

            if j >= len(word2):
                cur_2 = ""
            else:
                cur_2 = word2[j]

            
            # if match, we just move forward
            if cur_1 == cur_2:
                a =  rec(i+1, j+1)
                dp[(i,j)] = a
                return a
            else:
                # we can only add when there is element in cur_2
                a = None
                if cur_2 != "":
                    a = 1 + rec(i, j+1)

                # 2. we can only remove is there is element in cur_1
                b = None
                if cur_1 != "":
                    b = 1 + rec(i+1, j)

                # 3. we can only replace if both element are present
                c = None
                if cur_1 != "" and cur_2 != "":
                    c = 1 + rec(i+1, j+1)
                
                ans = float('inf')
                if a:
                    ans = min(ans, a)
                if b:
                    ans = min(ans, b)
                if c:
                    ans = min(ans, c)
                

                dp[(i,j)] = ans
                return dp[(i,j)]
        
        return rec(0,0)



            

