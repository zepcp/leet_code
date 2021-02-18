from re import fullmatch


class Solution:
    """
    Runtime: 64 ms, faster than 42.57% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14.5 MB, less than 34.72% of Python3 online submissions for Regular Expression Matching.
    """
    def isMatch(self, s: str, p: str) -> bool:
        return True if fullmatch(p, s) else False


if __name__ == '__main__':
    print("Input: {} {}".format("aa", "a"))
    response = Solution().isMatch("aa", "a")
    print("Output: {}".format(response))

    print("Input: {} {}".format("mississippi", "mis*is*p*."))
    response = Solution().isMatch("mississippi", "mis*is*p*.")
    print("Output: {}".format(response))
