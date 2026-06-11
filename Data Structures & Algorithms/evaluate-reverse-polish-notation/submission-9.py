class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or i.lstrip('-').isdigit():
                stack.append(i)
            else:
                var2 = int(stack.pop())
                var1 = int(stack.pop())
                print(var2)
                print(var1)
                print(i)
                if(i == "+"):
                   stack.append(var1+var2)
                elif(i == "*"):
                    stack.append(var1*var2)
                elif(i == "-"):
                    stack.append(var1-var2)
                elif(i == "/"): 
                    stack.append(math.trunc(var1/var2))
        return int(stack[-1])
