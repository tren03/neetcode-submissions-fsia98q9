class MinStack:
    # whenever we push, pop we need to track changes to min
    # to do that, do we use another stack? - yes
    # when pushing, check if val smaller than top of 2nd stack
    # -> if yes, push to second stack
    # when pop(), check if pop() returns top() of second stack
    # if yes pop() that out of second stack 


    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) != 0:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        self.main_stack.append(val)
        

    def pop(self) -> None:
        if self.main_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        print(self.min_stack)
        print(self.main_stack)
        return self.min_stack[-1]

        
