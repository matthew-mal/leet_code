def str_str(haystack, needle):
    return haystack.find(needle)


def strStr(haystack, needle):
    lps = [0] * len(needle)
    pre = 0
    for i in range(1, len(needle)):
        while pre > 0 and needle[i] != needle[pre]:
            pre = lps[pre - 1]
        if needle[pre] == needle[i]:
            pre += 1
            lps[i] = pre

    n = 0
    for h in range(len(haystack)):
        while n > 0 and needle[n] != haystack[h]:
            n = lps[n - 1]
        if needle[n] == haystack[h]:
            n += 1
        if n == len(needle):
            return h - n + 1
    return -1
