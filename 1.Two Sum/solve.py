class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        pairs = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in pairs:
                return [pairs[complement], i]
            pairs[num] = i
        return pairs
        
