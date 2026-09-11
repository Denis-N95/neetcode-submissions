class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        return [item[0] for item in d.most_common(k)]
            
                