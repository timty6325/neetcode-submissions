class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]
        result = []
        

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            buckets[val].append(key)
        
        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                result.append(num)
                if len(result) == k: 
                    return result
                    

                

        



            
        
            
        