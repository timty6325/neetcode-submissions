class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = 1
        while ind1 != len(numbers) - 1:
            if numbers[ind1] + numbers[ind2] == target:
                return [ind1 + 1, ind2 + 1]
            else:
                if ind2 == len(numbers) - 1:
                    ind2 = ind1 + 2
                    ind1 += 1
                else:
                    ind2 += 1

        return [ind1 + 1, ind2 + 1]