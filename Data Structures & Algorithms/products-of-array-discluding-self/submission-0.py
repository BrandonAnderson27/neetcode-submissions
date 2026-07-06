class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        big = 1
        res = []

        for n in range(len(nums)):
            current = 1
            for i in range(len(nums)):
                if i != n:
                    current *= nums[i]
            res.append(current)

        return res