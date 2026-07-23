class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin = 0
        # leftMax = 0

        # for i in s:
        #     if i == "(":
        #         leftMin += 1
        #         leftMax += 1
        #     elif i == ")":
        #         leftMin -= 1
        #         leftMax -= 1
        #     elif i == "*":
        #         leftMin -= 1
        #         leftMax += 1
        #     if leftMin < 0:
        #         leftMin = 0
        #     if leftMax < 0:
        #         return False
        # if leftMin == 0:
        #     return True
        # else:
        #     return False
        lStack = []
        sStack = []

        for i in range(len(s)):
            if s[i] == "(":
                lStack.append(i)
            elif s[i] == "*":
                sStack.append(i)
            else:
                if lStack:
                    lStack.pop()
                elif sStack:
                    sStack.pop()
                else:
                    return False

        while sStack and lStack:
            if lStack.pop() > sStack.pop():
                return False
        if lStack:
            return False
        return True

