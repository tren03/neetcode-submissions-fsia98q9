func hammingWeight(n int) int {
	/*
	23/2 = 11 r - 1
	11/2 = 5 r - 1
	5/2 = 2 r - 1
	2/2 = 1 r - 0
	1/2 = 0 r - 1
	*/

	ans := 0
	for n != 0{
		rem := n % 2
		n = n / 2 
		if rem == 1{
			ans += 1
		}
	}
	return ans


}
