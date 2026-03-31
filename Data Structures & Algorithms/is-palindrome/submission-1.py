class Solution:
    def isPalindrome(self, s: str) -> bool:
        refactorS = ""
        for i in s:
            if i.isalnum():
                refactorS += i.lower()
        right = len(refactorS)-1
        for i in range(len(refactorS)//2):
            if refactorS[i] != refactorS[right]:
                return False
            else:
                right -= 1
        return True

