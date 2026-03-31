class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = -1

        while l < r:
            h = min(height[l], height[r])
            a = h * (r - l)

            if a > ans:
                ans = a
            
            # case 1: go l += 1
            if height[l] <= height[r]:
                l += 1
            
            # case 2: go r -= 1
            else:
                r -= 1

        return ans