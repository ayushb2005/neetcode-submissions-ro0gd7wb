class Solution:

    '''
    255HelloWorld
    5#Hello5#World
    1#A
    '''
    def encode(self, strs: List[str]) -> str:
        combinedStr = ""
        for string in strs:
            combinedStr += str(len(string))+"#"+string
        print(combinedStr)
        return combinedStr
    def decode(self, s: str) -> List[str]:
        # starting = s.index("#")
        # val = [0:starting] -> index = [starting+1: starting+5+2]
        # -> get new #
        outputArray = []
        pointer = 0 
        while(pointer < len(s)):
            findHash = s.index("#", pointer)
            count = int(s[pointer:findHash])
            word = s[findHash+1:(findHash+count+1)]
            outputArray.append(word)
            pointer = findHash+count+1
        return outputArray
