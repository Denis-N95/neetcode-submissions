class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        k = 1
        for i in range(n):
            l[i] = k
            k *= nums[i]
        k = 1
        for i in range(n - 1, -1, -1):
            l[i] *= k
            k *= nums[i]
        return l