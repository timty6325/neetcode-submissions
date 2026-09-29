class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for n in i:
                count[ord(n) - ord('a')] += 1
            hashmap[tuple(count)].append(i)

        return list(hashmap.values())
                

        