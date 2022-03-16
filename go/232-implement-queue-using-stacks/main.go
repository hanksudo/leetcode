package main

type MyQueue struct {
	stack1 []int
	stack2 []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Push(x int) {
	this.stack1 = append(this.stack1, x)
}

func (this *MyQueue) Pop() int {
	if this.Empty() {
		return 0
	}
	if len(this.stack2) > 0 {
		pop := this.stack2[len(this.stack2)-1]
		this.stack2 = this.stack2[:len(this.stack2)-1]
		return pop
	} else {
		for len(this.stack1) > 0 {
			pop := this.stack1[len(this.stack1)-1]
			this.stack1 = this.stack1[:len(this.stack1)-1]
			this.stack2 = append(this.stack2, pop)
		}
		pop := this.stack2[len(this.stack2)-1]
		this.stack2 = this.stack2[:len(this.stack2)-1]
		return pop
	}
}

func (this *MyQueue) Peek() int {
	if len(this.stack2) > 0 {
		return this.stack2[len(this.stack2)-1]
	} else {
		for len(this.stack1) > 0 {
			pop := this.stack1[len(this.stack1)-1]
			this.stack1 = this.stack1[:len(this.stack1)-1]
			this.stack2 = append(this.stack2, pop)
		}
		return this.stack2[len(this.stack2)-1]
	}
}

func (this *MyQueue) Empty() bool {
	return len(this.stack1) == 0 && len(this.stack2) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
