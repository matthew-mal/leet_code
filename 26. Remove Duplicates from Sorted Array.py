class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        replace = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace
