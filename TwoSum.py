class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in number_map:
                return [i, number_map[diff]]
            
            number_map[num] = i