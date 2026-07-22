class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            
            # What am I looking for?
            complement = target - num

            # Have I seen it?

            if complement in lookup:
                return [lookup[complement], i]

            # Store for next iteration

            lookup[num] = i
        return []


       