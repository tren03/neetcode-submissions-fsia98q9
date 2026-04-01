type MinStack struct {
	s []int
	sMin []int
}

func Constructor() MinStack {
	m := MinStack{
		s: []int{},
		sMin: []int{},
	}
	return m
}

func (this *MinStack) Push(val int) {
	this.s = append(this.s, val)
	if len(this.sMin) == 0 {
		this.sMin = append(this.sMin, val)
	}else{
		if this.sMin[len(this.sMin)-1] >= val{
			this.sMin = append(this.sMin, val)
		}
	}
}

func (this *MinStack) Pop() {
	val := this.s[len(this.s)-1]
	this.s = this.s[:len(this.s)-1]
	if len(this.sMin) > 0 && this.sMin[len(this.sMin)-1] >= val{
		this.sMin = this.sMin[:len(this.sMin)-1]
	}
}

func (this *MinStack) Top() int {
	return this.s[len(this.s)-1]

}

func (this *MinStack) GetMin() int {
	return this.sMin[len(this.sMin)-1]
}
