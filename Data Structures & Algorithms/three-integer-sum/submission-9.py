class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #lets sort arr
        sorted_array = sorted(nums)
        print(sorted_array)
        answer = []

        for index,cur in enumerate(sorted_array):
            if index != 0:
                if sorted_array[index] == sorted_array[index-1]:
                    continue

            l = index + 1
            r = len(sorted_array) -1
            if l == r:
                break

            while l<r:
                to_check = sorted_array[l] + sorted_array[r]
                if to_check == -cur:
                    # we found answer
                    print(l,r)
                    answer.append([cur,sorted_array[l],sorted_array[r]])
                    prev = sorted_array[r]
                    r-=1
                    while(r > l and sorted_array[r] == prev):
                        r-=1

                
                if to_check > -cur:
                    r -= 1
                if to_check < -cur:
                    l+=1

        return answer



            

            