class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        z_index = -1
        prod = 1
        l = len(nums)

        r = [0 for _ in range(l)]

        for i in range(l):
            if nums[i] == 0:
                zeroes += 1
                z_index = i
                continue
            prod *= nums[i]
        
        if zeroes > 1:
            return r
        
        if zeroes == 1:
            r[z_index] = prod
            return r
        
        if zeroes == 0:
            return [prod//num for num in nums]