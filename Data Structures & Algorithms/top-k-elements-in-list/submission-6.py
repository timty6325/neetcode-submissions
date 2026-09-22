class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        max = 0
        result = []
        count = k

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if max < hashmap[num]:
                max = hashmap[num]

        while count != 0:
            for key, value in hashmap.items():
                if value == max and key not in result:
                    result.append(key)
                    count -= 1
            max -=1
        return result
        
            
