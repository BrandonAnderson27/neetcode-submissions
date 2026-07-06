class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preTotal = 1
        pre = []
        suffTotal = 1
        suff = []
        res = []

        for n in range(len(nums)):
            preTotal *= nums[n]
            pre.append(preTotal)

        for n in range(len(nums)-1, -1, -1):
            suffTotal *= nums[n]
            suff.insert(0, suffTotal)

        for n in range(len(nums)):
            resTotal = 1
            if n == 0:
                resTotal *= suff[n+1]
            elif n == len(nums) - 1:
                resTotal *= pre[n-1]
            else:
                resTotal *= pre[n-1]
                resTotal *= suff[n+1]
            res.append(resTotal)

        return res