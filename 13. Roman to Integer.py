def roman_to_int(self, s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total + roman[s[-1]]


# second method
def roman_to_int2(self, s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    total = 0
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')
    for num in s:
        total += roman[num]
    return total


