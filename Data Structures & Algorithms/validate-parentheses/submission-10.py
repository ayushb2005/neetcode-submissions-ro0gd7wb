class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', '}':'{', ']':'['}

        stack = []

        for i in range(len(s)):
            if(s[i] not in hashMap):
                stack.append(s[i])
            else:
                if(len(stack) == 0):
                    return False
                else:
                    if(hashMap[s[i]] != stack.pop()):
                        return False
                
        return len(stack) == 0