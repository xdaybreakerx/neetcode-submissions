class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        res = []

        for i in range(0, len(nums)):
            if (target - nums[i]) in numMap:
                res = [numMap.get(target - nums[i]), i]
                return res
            numMap[nums[i]] = i