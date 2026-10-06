class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        

        for ind, val in enumerate(nums):
            if ind > 0 and val == nums[ind - 1]:
                continue

            l, r = ind + 1, len(nums) - 1
            while l < r:

                if val + nums[l] + nums[r] > 0:
                    r -= 1

                elif val + nums[l] + nums[r] < 0:
                    l += 1

                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                
        return result
