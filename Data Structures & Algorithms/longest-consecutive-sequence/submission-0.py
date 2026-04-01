class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s  = set()
        for i in nums:
            s.add(i)
        
        count = 0
        for i in nums:
            if i-1 in s:
                continue
            
            temp_count = 1
            # assume i is smallest
            temp_nos = i
            while True:
                if temp_nos+1 in s:
                    temp_count += 1
                    temp_nos += 1
                else:
                    break
            count = max(count,temp_count)
            print(count)

        return count



        