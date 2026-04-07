class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack problem
        use append and pop
        '''
        # stack1 = []
        # for i in s:
        #     if i in "([{":
        #         stack1.append(i)
        #     else:
        #         if not stack1:
        #             return False
        #         value = stack1.pop()
        #         if((value + i) != "{}" and (value + i) != "()" \
        #         and (value + i) != "[]"):
        #             return False
        # return len(stack1) == 0
        
        hashMap = {')':'(', '}': '{', ']':'['}
        stack = []
        for i in s:
            if i in hashMap:
                if not stack:
                    return False
                else:
                    value = stack.pop()
                    if(hashMap[i] != value):
                        return False
            else:
                stack.append(i)
        return len(stack) == 0