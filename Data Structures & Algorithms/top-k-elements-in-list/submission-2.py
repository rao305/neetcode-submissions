class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter

        freq = Counter(nums)

        top_k = freq.most_common(k)

        result = []

        for item in top_k:
            number = item[0]
            result.append(number)

        return result
            

