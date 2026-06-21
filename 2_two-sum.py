from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_solutions = {}
        for idx, num in enumerate(nums):
            if num in possible_solutions:
                return [possible_solutions[num], idx]
            else:
                possible_solutions[target - num] = idx
