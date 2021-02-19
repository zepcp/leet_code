class Solution:
    """
    Runtime: 36 ms, faster than 59.95% of Python3 online submissions for Valid Number.
    Memory Usage: 14.3 MB, less than 33.57% of Python3 online submissions for Valid Number.
    """
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True if "nf" not in s else False
        except:
            return False


if __name__ == '__main__':
    print("Input: {}".format("e"))
    response = Solution().isNumber("e")
    print("Output: {}".format(response))

    print("Input: {}".format("75e1"))
    response = Solution().isNumber("75e1")
    print("Output: {}".format(response))
