from typing import List
import ast

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i in range(len(nums)):
            val = nums[i]
            diff = target - val
            
            if val in cache:
                return [cache[val],i]
            cache[diff] = i
        return []

sol = Solution()
nums = ast.literal_eval(input())

target = int(input())

res = ','.join(map(str, sol.twoSum(nums, target)))

print('[%s]' % res)