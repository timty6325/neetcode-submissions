class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        elements = [[] for i in range(len(nums)+ 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for key, val in count.items():
            elements[val].append(key)
        
        for i in range(len(nums), 0, -1):
            for n in elements[i]:
                if len(result) == k:
                    return result
                result.append(n)
        return result
            

            

        
        