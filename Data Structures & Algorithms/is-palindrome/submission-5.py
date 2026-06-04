class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanumeric = ""

        for i in s:
            if(i.isalnum()):
                alphanumeric += i
        left = 0
        right = len(alphanumeric)-1
        alphanumeric = alphanumeric.lower()
        while(left < right):
            if(alphanumeric[left] != alphanumeric[right]):
                return False
            left += 1
            right -= 1
        return True