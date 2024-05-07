def add_binary(a: str, b: str) -> str:
    res = ''
    carry = 0

    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_b + digit_a + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = '1' + res

    return res

print(add_binary('11', '1'))
