class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        at each char of the answer
        it can belong to either s1, s2 or both
        if belongs to s1 only - consider as s1 part
        if belongs to s2 only - consider as s2 part
        if belongs to both - we need to recurse on both options
        state defined by (ptr1, ptr2) - where ptr represents the 
        current element to process in s1 and s3 respectively
        """
        dp = {}
        def dfs(p1, p2):
            ans_ptr = p1 + p2
            if ans_ptr >= len(s3) and p1 >= len(s1) and p2 >= len(s2):
                dp[(p1,p2)] = True
                return True
            if ans_ptr >= len(s3) and (p1 < len(s1) or p2 < len(s2)):
                dp[(p1,p2)] = False
                return False
            if dp.get((p1,p2)) is not None:
                return dp[(p1,p2)]
            
            if p1 >= len(s1):
                cur_1 = ""
            else:
                cur_1 = s1[p1]
            if p2 >= len(s2):
                cur_2 = ""
            else:
                cur_2 = s2[p2]
            
            ans_val = s3[ans_ptr]
            if cur_1 == ans_val and cur_2 == ans_val:
                print("cur1 cur2, match", cur_1, cur_2)
                a = dfs(p1+1, p2)
                b = dfs(p1, p2+1)
                dp[(p1,p2)] = a or b
                return a or b
            if cur_1 == ans_val:
                dp[(p1,p2)] = dfs(p1+1, p2)
                return dp[(p1,p2)]
            if cur_2 == ans_val:
                dp[(p1,p2)] = dfs(p1, p2+1)
                return dp[(p1,p2)]
            # ans cur value does not match with any value 
            # so this means its false for sure
            return False
            
        return dfs(0,0)
            
                    


                


            