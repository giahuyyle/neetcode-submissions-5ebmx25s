class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = []
        prod = 1
        l = len(nums)

        r = [0 for _ in range(l)]

        for i in range(l):
            if nums[i] == 0:
                zeroes.append(i)
                continue
            prod *= nums[i]
        
        if len(zeroes) > 1:
            return r
        
        if len(zeroes) == 1:
            r[zeroes[0]] = prod
            return r
        
        if len(zeroes) == 0:
            return [prod//num for num in nums]