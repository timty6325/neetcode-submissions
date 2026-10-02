class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        finish = len(numbers) - 1
        

        while True:
            if numbers[start] + numbers[finish] < target:
                start +=1 
            elif numbers[start] + numbers[finish] > target:
                finish -=1
            else:
                return [start + 1, finish + 1]
                