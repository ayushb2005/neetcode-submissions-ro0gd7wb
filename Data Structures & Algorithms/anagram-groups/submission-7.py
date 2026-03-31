class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        create one hashmap where i have a sublist of words
        the key can be the word hashed with a tuple

        '''
        hashMap = {}
        for word in strs:
            array = [0]*26
            # combinedStr = ""
            for letter in word:
                array[ord(letter)-ord('a')] += 1
            # for letter in word:
            #     array[ord(letter)-97] += 1
            # for i in range(26):
            #     combinedStr += chr(97+i) + str(array[i])
            hashedStr = tuple(array)
            if(hashedStr in hashMap):
                hashMap[hashedStr].append(word)
            else:
                hashMap[hashedStr] = [word]
        return list(hashMap.values())
        
            
        
