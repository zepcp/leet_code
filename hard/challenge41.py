from typing import List


class Solution:
    """
    Runtime: 36 ms, faster than 66.86% of Python3 online submissions for First Missing Positive.
    Memory Usage: 14.3 MB, less than 50.47% of Python3 online submissions for First Missing Positive.
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for x in nums:
            if x <= 0:
                continue
            elif x > missing:
                return missing
            elif x == missing:
                missing += 1
        return missing


if __name__ == '__main__':
    print("Input: {}".format([1,2,0]))
    response = Solution().firstMissingPositive([1,2,0])
    print("Output: {}".format(response))

    print("Input: {}".format([3,4,-1,1]))
    response = Solution().firstMissingPositive([3,4,-1,1])
    print("Output: {}".format(response))

    print("Input: {}".format([1,1]))
    response = Solution().firstMissingPositive([1,1])
    print("Output: {}".format(response))
