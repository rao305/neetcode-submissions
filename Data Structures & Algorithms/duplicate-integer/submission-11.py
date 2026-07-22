class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for element in nums:
            if element in hashset:
              return True
            hashset.add(element)
        return False  

