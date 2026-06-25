class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                numbers[i] += 1

        common = []

        for i in range(k):
            for ind, val in numbers.items():
                if numbers[ind] == max(numbers.values()) and ind not in common:
                    common.append(ind)
                    numbers[ind] = -1
                    break

        return common


            

