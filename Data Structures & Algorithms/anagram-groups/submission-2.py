class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for acronym in strs:
            count = [0] * 26

            for letter in acronym:
                count[ord(letter) - ord('a')] += 1

            result[tuple(count)].append(acronym)

        return list(result.values())

        


            
        