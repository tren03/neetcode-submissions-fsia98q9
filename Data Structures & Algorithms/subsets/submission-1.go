//1,2,3
//
//[] i = 0
//[1] [] i = 1
//[1,2] [1] [2] [] i = 2
//[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
//
//at every index, we include and exclude the current index
//when we reach leaf i.e index = len(nums), add that to ans and 
//return ans
import "slices"
func subsets(nums []int) [][]int {
	n := len(nums)
	i := 0
	ans := [][]int{}
	temp := []int{}

	var rec func(int, []int)

	rec = func(i int, temp []int){
		if i == n{
			dst := make([]int, len(temp))
            copy(dst, temp)
            ans = append(ans, dst)
            return
		}
		temp = append(temp, nums[i])
		rec(i+1,temp)
		//delete(temp, nums[i])
		//temp = slices.Delete(temp, i, i+1)
		temp = slices.Delete(temp, len(temp)-1, len(temp))
		rec(i+1,temp)
	}
	
	rec(i,temp)

	return ans

}

