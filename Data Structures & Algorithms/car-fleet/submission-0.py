class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       sortedArray = []
       for i in range(len(position)):
              sortedArray.append((position[i], speed[i]))
       sortedArray.sort()
       stack = []

       for i in range(len(sortedArray)):
              stack.append((target-sortedArray[i][0])/sortedArray[i][1])
       fleets = 1
       first = None
       for i in range(len(stack)-1, -1, -1):
              if(first is None):
                     first = stack[i]
              else:
                   if(first < stack[i]):
                     fleets += 1
                     first = stack[i]
       return fleets

