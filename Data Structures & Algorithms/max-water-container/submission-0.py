class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        most = 0
        while l < r:
            water = min(heights[l], heights[r]) * (r-l)
            if water > most:
                most = water
            else:
                if heights[l] < heights[r]:
                    l += 1
                elif heights[r] < heights[l]:
                    r -= 1
                elif heights[l] == heights[r]:
                    l += 1
        return most