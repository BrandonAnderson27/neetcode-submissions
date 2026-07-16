class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack, istack = [], []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures): 
            if len(tempstack) ==  0:
                tempstack.append(t)
                istack.append(i)
            else: 
                while len(tempstack) > 0 and t > tempstack[-1]:
                    tempstack.pop()
                    spot = istack.pop()
                    res[spot] = i - spot
                if len(tempstack) == 0 or t <= tempstack[-1]:
                    tempstack.append(t)
                    istack.append(i)

        return res