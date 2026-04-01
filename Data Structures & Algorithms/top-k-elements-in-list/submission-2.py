class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1

        sorted_arr = sorted(count.items(),key=lambda item: item[1])
        ans = []
        for i in range(len(sorted_arr)-1,len(sorted_arr)-k-1,-1):
            ans.append(sorted_arr[i][0])
        return ans
        

            


        
        
        