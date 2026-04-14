class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        expand outwards
        from each letter and check if there is a palindrome
        '''
        maxString = ""
        resLen = 0
        for i in range(len(s)):
            #odd length
            left = i
            right = i
            while(0<= left and right <len(s) and s[left] == s[right]):
                if(right-left+1 > resLen):
                    maxString = s[left:right+1]
                    resLen = right-left+1
                left -= 1
                right += 1
            #even length
            left = i
            right = i+1
            while(0<= left and right < len(s) and s[left] == s[right]):
                if(right - left + 1 > resLen):
                    maxString = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return maxString


