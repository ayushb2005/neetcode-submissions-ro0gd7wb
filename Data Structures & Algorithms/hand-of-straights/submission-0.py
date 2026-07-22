class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hashmap = {}
        hand.sort()
        for i in hand:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        count = 1
        for i in sorted(hashmap.keys()):
            if hashmap[i] != 0:
                key = i
                value = hashmap[key]
                for _ in range(groupSize):
                    if key in hashmap and hashmap[key] >= value:
                        hashmap[key] -= value
                        key += 1
                    else:
                        return False
        return True


            

        