class Solution:

    def encode(self, strs: List[str]) -> str:
        r = []
        for s in strs:
            l = len(s)
            r.append(f"{l}$")
            r.append(s)
        
        return "".join(r)

    def decode(self, s: str) -> List[str]:
        r = []

        i = 0
        last = 0
        length = len(s)

        while i < length:
            if s[i] == "$":
                start = i + 1

                l = ""
                while last < i:
                    l += s[last]
                    last += 1
                
                l = int(l)
                end = start + l

                r.append(s[start:end])

                i = end
                last = end

            else:
                i += 1

        return r