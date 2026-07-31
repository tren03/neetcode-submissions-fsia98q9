class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        while f != None:
            s = nums[s]
            f = nums[nums[f]]
            print(s,f)
            if s == f:
                break
        
        head = 0
        while head != s:
            s = nums[s]
            head = nums[head]
        
        return head
        