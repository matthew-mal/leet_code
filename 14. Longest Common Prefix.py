class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        """
            O(n^2)
        """
        if len(strs) == 1:
            return strs[0]

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[:i]
        return base


class Solution2:
    def longest_common_prefix2(self, strs: list[str]) -> str:
        """
            O(n)
        """
        mn, mx = min(strs), max(strs)

        for i in range(len(mn)):
            if mn[i] != mx[i]:
                return mn[:i]

        return mn
