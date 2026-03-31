class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashSet = Counter(nums).most_common()
        print(hashSet)
        i = 0
        while i < k:
            ans.append(hashSet[i][0])
            i += 1
        return ans