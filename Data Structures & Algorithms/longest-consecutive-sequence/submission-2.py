class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        ans = 0

        for i in nums:
            s.add(i)
        
        for i in nums:
            prev = i - 1
            if prev in s:
                continue
            
            t = i
            count = 0
            while t in s:
                count += 1
                ans = max(ans, count)
                t += 1
        return ans
                
        