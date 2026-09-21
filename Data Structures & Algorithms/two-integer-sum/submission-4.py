class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for ind, val in enumerate(nums):
            match = target - val

            if match in hashmap:
                return [hashmap[match], ind]
            hashmap[val] = ind
            


            
            
        