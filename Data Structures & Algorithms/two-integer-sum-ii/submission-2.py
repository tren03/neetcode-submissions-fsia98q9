class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have 2 pointers l,r, if sum big, move r, else move l

        l = 0
        r = len(numbers) - 1

        to_check = numbers[l] + numbers[r]
        while(1):
            if to_check == target:
                return [l+1,r+1]
            
            if to_check > target:
                r -= 1

            if to_check < target:
                l += 1
            
            to_check = numbers[l] + numbers[r]
                



        