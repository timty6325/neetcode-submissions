class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) - 1


        while True:
            if numbers[beg] + numbers[end] == target:
                return [beg + 1, end + 1]

            if numbers[beg] + numbers[end] > target:
                end -=1

            elif numbers[beg] + numbers[end] < target:
                beg += 1
             
        
        