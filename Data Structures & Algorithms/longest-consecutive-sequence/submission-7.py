class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(set(nums))
        result = set()
        longest = 0
    
        for num in numbers:
            if len(result) == 0:
                result.add(num)

            elif num - 1 in result:
                result.add(num)

            else:
                longest = max(longest, len(result))
                result = set()
                if len(result) == 0:
                    result.add(num)
                elif num - 1 in result:
                    result.add(num)

        return max(longest, len(result))