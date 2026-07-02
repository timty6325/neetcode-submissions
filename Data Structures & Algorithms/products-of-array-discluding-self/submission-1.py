class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        def helper_func(array, index):
            result = []
            product = 1
            for ind in range(len(array)):
                if ind == index:
                    continue
                else:
                    result.append(array[ind])
            for i in result:
                product *= i
            return product


        for i in range(len(nums)):
            result.append(helper_func(nums, i))

        return result
        



            
            
        

        