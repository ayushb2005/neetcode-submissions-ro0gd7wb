class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack problem
        use append and pop
        '''
        stack1 = []
        for i in s:
            if i in "([{":
                stack1.append(i)
            else:
                if not stack1:
                    return False
                value = stack1.pop()
                if((value + i) != "{}" and (value + i) != "()" \
                and (value + i) != "[]"):
                    return False
        return len(stack1) == 0
        