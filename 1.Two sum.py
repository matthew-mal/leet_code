def two_sum(nums: list[int], target: int) -> list[int]:
    """
    O(n)
    """
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
