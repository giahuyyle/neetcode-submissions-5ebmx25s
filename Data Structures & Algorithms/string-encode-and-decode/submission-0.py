class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s))
            code += '#'
            code += s
        return code

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        n = 0
        while i < len(s):
            if s[i] == '#':
                l = s[n:i]
                n += (1 + len(l) + int(l))
                strs.append(s[i+1:n])
                i += (1 + int(l))
            else:
                i += 1
        return strs