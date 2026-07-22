class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for elements in nums:
                ans.append(elements)
        return ans