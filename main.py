from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)-1):
        for j in range(i, len(nums)):
            if (nums[i] + nums[j]) == target:
                indices = [i, j]
                return indices

nums = [2,7,11,15]
target = 22
print(twoSum(nums, target))