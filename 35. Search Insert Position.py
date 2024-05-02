def search_insert(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return l


print(search_insert([1, 3, 4, 5, 6, 7, 8], 2))