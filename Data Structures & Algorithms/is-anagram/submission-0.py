class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = Counter(s)
        set2 = Counter(t)
        return set1==set2