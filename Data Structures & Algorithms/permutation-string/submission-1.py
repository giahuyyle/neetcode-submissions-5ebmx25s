class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        leng = len(s1)
        perm = Counter(s1)

        l = 0
        r = leng

        while r <= len(s2):
            s3 = s2[l:r]
            if perm == Counter(s3):
                return True
            l += 1
            r += 1
        
        return False