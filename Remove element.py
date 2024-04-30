def remove_element(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


print(remove_element([1, 2, 3, 34, 2], 2))
