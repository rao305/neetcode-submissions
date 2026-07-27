class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temps)

        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                cold_day = stack.pop()
                result[cold_day] = i - cold_day
            stack.append(i)
        return result

        