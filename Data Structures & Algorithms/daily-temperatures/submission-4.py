class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        stack = []
        n = len(temp)
        result = [0] * n 

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                cold_day = stack.pop()
                result[cold_day] = i - cold_day # warmer day 

            stack.append(i)

        return result


        