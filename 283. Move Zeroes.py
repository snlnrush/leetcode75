class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        count = -10000
        while True:
            if left == right or count == len(nums):
                break
            if nums[left] == 0:
                nums.append(nums.pop(left))
            elif nums[right] == 0:
                nums.append(nums.pop(right))
                right -= 1
            else:
                left += 1
            count += 1


"""
283. Move Zeroes
Easy
13.7K
347
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""