def mapStringToChars(s: str):
    dic = {}
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 1
    dic = dict(sorted(dic.items()))
    return str(dic)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            s_map = mapStringToChars(s)

            if s_map in dic.keys():
                dic[s_map].append(s)
            
            else:
                dic[s_map] = [s]
        
        print(dic)
        result = [dic[key] for key in dic.keys()]

        return result