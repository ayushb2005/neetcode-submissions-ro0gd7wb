class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c)-ord('a')]+=1
            strApp = ""
            for i in range(26):
               strApp += chr(97+i)+str(freq[i])
            if strApp not in dict:
                dict[strApp] = []
            dict[strApp].append(word)
        return list(dict.values())