class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for ind, val in enumerate(nums):
            match = target - val

            if match in table: 
                return [table[match], ind]
            table[val] = ind


            
            
        