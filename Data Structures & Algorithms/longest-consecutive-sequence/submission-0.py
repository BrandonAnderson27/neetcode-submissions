class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in nums:
            length = 0
            if (n - 1) not in numsSet:
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest