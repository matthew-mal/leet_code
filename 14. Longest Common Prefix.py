class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[:i]
        return base


