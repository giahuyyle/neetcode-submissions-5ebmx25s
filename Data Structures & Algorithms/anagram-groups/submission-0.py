def sortAnagram(a):
    result = []
    for i in range(len(a)):
        result.append(a[i])
    result.sort()
    return "".join(result)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        hash_map = {}
        result = []
        for i in range(len(strs)):
            key = sortAnagram(strs[i])
            if key not in hash_map.keys():
                hash_map[key] = [strs[i]]
            else:
                hash_map[key].append(strs[i])
        for key in hash_map.keys():
            result.append(hash_map[key])
        return result