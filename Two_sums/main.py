from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen :dict = {}
        for index,num in enumerate(nums):
            rest:int = target - num
            if rest in seen:
                return [seen[rest],index]
            seen[num] = index 







