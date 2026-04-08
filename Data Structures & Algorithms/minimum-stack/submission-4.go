type MinStack struct {
    q  []int
    mq []int
}

func Constructor() MinStack {
    return MinStack{
        q:  []int{},
        mq: []int{},
    }
}

func (this *MinStack) Push(val int) {
    this.q = append(this.q, val)
    if len(this.mq) == 0 || val <= this.mq[len(this.mq)-1] {
        this.mq = append(this.mq, val)
    }
}

func (this *MinStack) Pop() {
    p := this.q[len(this.q)-1]
    this.q = this.q[:len(this.q)-1]

    if p == this.mq[len(this.mq)-1] {
        this.mq = this.mq[:len(this.mq)-1]
    }
}

func (this *MinStack) Top() int {
    return this.q[len(this.q)-1]
}

func (this *MinStack) GetMin() int {
    return this.mq[len(this.mq)-1]
}