def my_sqrt(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
    return right


print(my_sqrt(2))
